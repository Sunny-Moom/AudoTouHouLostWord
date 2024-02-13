import sys
import time

import cv2
import utils.adb_lw as adb
import numpy as np


def cmd_clear():
    sys.stdout.write("\033[F")  # 光标上移一行
    sys.stdout.write("\033[K")  # 清除当前行


def image(template_file, num):
    # 加载图像
    adb.adb_image()
    img_rgb = cv2.imread('./data/img/screen.png')
    img_template = cv2.imread('./data/img/' + template_file + '/' + str(num) + '.png')
    w, h = img_template.shape[:-1]

    # 使用OpenCV进行模板匹配
    result = cv2.matchTemplate(img_rgb, img_template, cv2.TM_CCOEFF_NORMED)

    # 匹配图像的坐标
    loc = np.where(result >= 0.8)
    re = [w, h, loc]
    return re


def match_image(template_file, num, cold):
    """
    使用opencv实现图像识别并点击
    :param template_file: img文件夹内图像所处的文件夹名
    :param num: 需要点击的图像的编号
    :param cold: 未找到图像后暂停时间
    :return: 无输出
    """
    while True:
        re = image(template_file, num)
        w = re[0]
        h = re[1]
        loc = re[2]
        if len(loc[0]) > 0:
            # 计算匹配图像的中心点
            center = (loc[1][0] + w // 2, loc[0][0] + h // 2)
            print("\033[32m" + "找到匹配图像，中心点坐标为：" + "\033[0m", center)
            cmd_clear()
            # 模拟点击
            adb.adb_touch(center[0], center[1])
            break
        else:
            print("\033[31m" + f"未找到匹配图像，{cold} 秒后重新查找" + "\033[0m")
            cmd_clear()
            time.sleep(cold)


def search_image(template_file, num, tim):
    """
    查找屏幕内是否出现指定图像
    :param template_file: img文件夹内图像所处的文件夹名
    :param num: 需要查找的图像的编号
    :param tim: 查找的次数（1秒1次）
    :return: 如果找到，输出坐标，如果没找到,输出False
    """
    t = True
    while t:
        re = image(template_file, num)
        w = re[0]
        h = re[1]
        loc = re[2]

        if len(loc[0]) > 0:
            # 计算匹配图像的中心点
            center = (loc[1][0] + w // 2, loc[0][0] + h // 2)
            print("\033[32m" + "找到匹配图像，中心点坐标为：" + "\033[0m", center)
            cmd_clear()
            t = False
            return center
        else:
            if tim == 0:
                print("\033[31m" + "未找到匹配图像，直接进行下一步" + "\033[0m")
                cmd_clear()
                t = False
                return False
            tim -= 1
            time.sleep(1)


def search_tap(template_file, num, tim, cold):
    """
    搜索图片，如果有就点击，无就略过
    :param template_file:
    :param num:
    :param tim:
    :param cold:
    :return:
    """
    center = search_image(template_file, num, tim)
    if center:
        adb.adb_touch(center[0],center[1])
        time.sleep(cold)
