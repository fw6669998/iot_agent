"""
printer.py - Windows 打印机控制脚本

功能:
  - 列出系统可用打印机
  - 打印文件(PDF / 图片 / Office / 文本 等任意格式)
  - 可指定打印机,不指定则用系统默认打印机

依赖(可选):  pip install pywin32
  安装后: 支持列出打印机、指定打印机、纯文本直发后台(无弹窗)
  未安装: 仍可打印, 但只能用系统默认打印机

命令行用法:
  python printer.py                       # 列出所有打印机
  python printer.py <文件路径>             # 用默认打印机打印
  python printer.py <文件路径> -p <打印机> # 用指定打印机打印

作为模块导入:
  from printer import list_printers, print_file
"""

import os
import sys
import argparse
import time

try:
    import win32print
    import win32api

    _HAS_PYWIN32 = True
except ImportError:
    _HAS_PYWIN32 = False

# 直接发送到打印机后台的文本类后缀(无需启动应用程序)
_RAW_TEXT_EXT = {'.txt', '.log', '.csv', '.ini', '.conf', '.md', '.bat', '.py'}


def list_printers():
    """返回 (打印机名列表, 默认打印机名)。

    未安装 pywin32 时返回 ([], None)。
    """
    if not _HAS_PYWIN32:
        return [], None
    flags = win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS
    names = [p[2] for p in win32print.EnumPrinters(flags)]
    default = win32print.GetDefaultPrinter()
    return names, default


def _resolve_printer(printer_name):
    """确定要使用的打印机名。传入 None 时返回系统默认打印机。"""
    if not _HAS_PYWIN32:
        if printer_name:
            print('⚠️ 未安装 pywin32,无法指定打印机,将使用系统默认打印机')
        return None
    if printer_name is None:
        return win32print.GetDefaultPrinter()
    return printer_name


def _print_via_shell(file_path, printer_name):
    """通过 ShellExecute 调用关联程序打印。

    有 pywin32 时: 优先用 printto 动作(可指定打印机), 失败则回退 print。
    无 pywin32 时: 用标准库 os.startfile 的 print 动作(只能用默认打印机)。

    注意: 部分程序不支持 printto, 会忽略指定打印机而使用默认打印机。
    """
    dir_ = os.path.dirname(file_path) or '.'

    if not _HAS_PYWIN32:
        # 无 pywin32: 只能用默认打印机打印
        os.startfile(file_path, 'print')
        return

    verb_args = f'"{printer_name}"' if printer_name else None
    verb = 'printto' if printer_name else 'print'
    try:
        win32api.ShellExecute(0, verb, file_path, verb_args, dir_, 0)  # 0 = SW_HIDE
    except Exception as e:
        try:
            # printto 不支持时回退到 print(使用系统默认打印机)
            win32api.ShellExecute(0, 'print', file_path, verb_args, dir_, 0)
        except Exception as e2:
            print(f'⚠️ 打印失败: {e}')


def _print_text_raw(file_path, printer_name):
    """把文本文件直接发送到打印机后台, 无弹窗、速度快。

    返回打印任务 ID。注意: 中文能否正确打印取决于文件编码与打印机字库设置,
    若出现乱码, 可改用 print_file(..., raw=False) 走关联程序(如记事本)打印。
    """
    with open(file_path, 'rb') as f:
        data = f.read()

    handle = win32print.OpenPrinter(printer_name)
    try:
        job_id = win32print.StartDocPrinter(handle, 1, ('Python 打印任务', None, 'RAW'))
        try:
            win32print.StartPagePrinter(handle)
            win32print.WritePrinter(handle, data)
            win32print.EndPagePrinter(handle)
        finally:
            win32print.EndDocPrinter(handle)
    finally:
        win32print.ClosePrinter(handle)
    return job_id


def print_file(file_path, printer_name=None, wait=False, raw=None):
    """打印文件。

    Args:
        file_path:    要打印的文件路径
        printer_name: 打印机名; None 表示使用系统默认打印机
        wait:         发送打印请求后是否短暂等待(关联程序打印时较有用)
        raw:          是否强制走文本直发后台;
                      None 表示按后缀自动判断(.txt 等走直发, 其余走关联程序)

    Returns:
        文本直发时返回打印任务 ID; 否则返回 None
    """
    file_path = os.path.abspath(file_path)
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f'文件不存在: {file_path}')

    target = _resolve_printer(printer_name)
    ext = os.path.splitext(file_path)[1].lower()

    # 判断是否走文本直发
    use_raw = raw if raw is not None else (ext in _RAW_TEXT_EXT)
    if use_raw and not _HAS_PYWIN32:
        use_raw = False  # 没有 pywin32 只能走关联程序
        print('⚠️ 未安装 pywin32,文本将改由关联程序打印')

    if use_raw:
        if target is None:
            raise RuntimeError('文本直发需要 pywin32 以获取默认打印机')
        job_id = _print_text_raw(file_path, target)
        print(f'✅ 文本已发送至打印机 [{target}], 任务ID: {job_id}')
        return job_id

    # 富格式(PDF/图片/Office等): 交给关联程序打印
    _print_via_shell(file_path, target)
    label = f'[{target}]' if target else '[默认打印机]'
    print(f'✅ 已发送打印请求 {label}: {os.path.basename(file_path)}')
    if wait:
        time.sleep(2)
    return None


def main():
    parser = argparse.ArgumentParser(description='控制打印机打印文件')
    parser.add_argument('file', nargs='?', help='要打印的文件路径(不提供则列出打印机)')
    parser.add_argument('-p', '--printer', default=None, help='指定打印机名(默认用系统默认打印机)')
    parser.add_argument('--wait', action='store_true', help='发送后等待片刻(关联程序打印时)')
    parser.add_argument('--no-raw', action='store_true', help='文本文件也走关联程序打印, 不直发后台')
    args = parser.parse_args()

    if not args.file:
        names, default = list_printers()
        if not names:
            print('未检测到打印机(或未安装 pywin32)。')
            return
        print('可用打印机:')
        for n in names:
            tag = ' (默认)' if n == default else ''
            print(f'  - {n}{tag}')
        return

    try:
        print_file(args.file, args.printer, args.wait, raw=False if args.no_raw else None)
    except Exception as e:
        print(f'❌ 打印失败: {e}')
        sys.exit(1)


if __name__ == '__main__':
    main()
