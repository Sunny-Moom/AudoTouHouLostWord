import subprocess
from configparser import ConfigParser

path = './config/settings.ini'  # 配置文件路径

config = ConfigParser()
config.read(path)
adb_config = config.get('bin', 'adb')


def adb_call(call):
    """
    无输出地执行adb命令
    :call: 要执行的指令
    :return: 无输出
    """
    subprocess.call(adb_config + call, shell=True, stdout=subprocess.DEVNULL)


def adb_image():
    """
    使用adb截图
    :return: 将截图输出至.img/screen.png
    """
    adb_call("adb shell screencap -p /sdcard/screen.png")
    adb_call("adb pull /sdcard/screen.png ./data/img/screen.png")


def adb_touch(x, y):
    """
    adb模拟点击
    :param x: x坐标
    :param y: y坐标
    :return: 无输出
    """
    adb_call("adb shell input tap {} {}".format(x, y))
