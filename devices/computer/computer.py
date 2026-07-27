"""
detect_lock.py - 检测 Windows 锁屏状态
"""
import ctypes
import subprocess


def check_lock_screen():
    # 检查是否有锁屏
    import subprocess
    result = subprocess.run(
        ['tasklist', '/FI', 'IMAGENAME eq LogonUI.exe'],
        capture_output=True, text=True,
        creationflags=subprocess.CREATE_NO_WINDOW  # 后台运行时不弹窗
    )
    return 'LogonUI.exe' in result.stdout


def lock_screen_win32():
    # 锁屏
    ctypes.windll.user32.LockWorkStation()


def start_remote_control():
    # 启动远程控制
    remote_control_path = "C:/Program Files/TeamViewer/TeamViewer.exe"
    subprocess.Popen(remote_control_path, creationflags=subprocess.CREATE_NO_WINDOW)

def get_host_name():
    import socket
    return socket.gethostname()

def get_system_name():
    import platform
    return platform.system()

if __name__ == "__main__":
    # import time
    # while True:
    #     time.sleep(2)
    #     readTimeCn = time.strftime("%H:%M:%S", time.localtime())
    #     print(readTimeCn, check_lock_screen())
    lock_screen_win32()
    # start_remote_control()
    # print(get_host_name())
    # print(get_system_name())
    pass
