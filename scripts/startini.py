import subprocess
from configparser import ConfigParser
import sys

path = './config/settings.ini'  # 配置文件路径


def adb_config(section, option, value):
    # 创建一个ConfigParser实例
    config = ConfigParser()
    # 如果配置文件存在则读取，不存在则创建新文件
    try:
        config.read(path)
    except FileNotFoundError:
        # 文件不存在，创建一个新文件
        with open(path, 'w') as f:
            config.write(f)

    # 确保section存在
    if not config.has_section(section):
        config.add_section(section)

    # 设置或覆盖option 'adb'
    config.set(section, option, value)

    # 将更新后的配置写回文件
    with open(path, 'w') as configfile:
        config.write(configfile)


def main_config():
    """
    检测系统类型以初始化配置文件,当系统非win,mac,linux时中断程序
    :return 无输出
    """
    if sys.platform.startswith('win'):
        adb_bin = ".\\adb_binary\\win32\\"
    elif sys.platform.startswith('linux'):
        adb_bin = ".\\adb_binary\\linux\\"
    elif sys.platform.startswith('darwin'):
        adb_bin = ".\\adb_binary\\macos\\"
    else:
        print('当前系统是其他操作系统,请在main.cofig的adb项填入adb工具目录')
        exit()
    adb_config('bin', 'adb', str(adb_bin))


def adb_check():
    """
    检查adb连接状态，并打印出已连接的设备信息
    :return: 无输出
    """
    config = ConfigParser()
    config.read(path, encoding='UTF-8')

    adb_path = config.get('bin', 'adb')

    print("正在检查adb连接：")
    devices_output = subprocess.check_output(f"{adb_path}adb devices", shell=True).decode('utf-8')

    devices = [line.split("\t") for line in devices_output.splitlines()[1:-1]]
    num_devices = len(devices)

    if num_devices == 0:
        print("未检测到任何设备，请检查模拟器或手机是否开启adb并连接成功。")
    else:
        print(f"检测到了{num_devices}台设备：")
        for device_name, connection_status in devices:
            print(f"设备名：{device_name}  连接状态：{connection_status}")


def start_ini():
    print("您的系统架构为：" + sys.platform)
    print("正在写入配置文件。。。")
    main_config()
    adb_check()
