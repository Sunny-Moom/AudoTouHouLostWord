import subprocess
import time

import cv2
import numpy as np
import os

# 角色池路径
player_path = "img/player_1"

# 关卡图路径
level_path = 'img/level'


# 图像识别并点击
def match_image(template_file, num, cold):
    # 使用adb截图
    subprocess.call("adb shell screencap -p /sdcard/screen.png", shell=True)
    subprocess.call("adb pull /sdcard/screen.png ./img/screen.png", shell=True)
    subprocess.call("adb shell rm /sdcard/screen.png", shell=True)

    # 加载图像
    img_rgb = cv2.imread('./img/screen.png')
    img_template = cv2.imread('./img/' + template_file + '/' + str(num) + '.png')
    w, h = img_template.shape[:-1]

    # 使用OpenCV进行模板匹配
    result = cv2.matchTemplate(img_rgb, img_template, cv2.TM_CCOEFF_NORMED)

    # 匹配图像的坐标
    loc = np.where(result >= 0.8)

    if len(loc[0]) > 0:
        # 计算匹配图像的中心点
        center = (loc[1][0] + w // 2, loc[0][0] + h // 2)
        print("找到匹配图像，中心点坐标为：", center)
        # 模拟点击
        subprocess.call("adb shell input tap {} {}".format(center[0], center[1]), shell=True)
    else:
        print("未找到匹配图像，1秒后重新查找")
        time.sleep(cold)
        match_image(template_file, num, cold)


# 加载上场角色池，关卡图
def rename_files(path):
    # 获取所有文件名
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    # 对文件名进行重命名，后缀名为txt，因为直接重命名可能会导致文件名重复而报错
    for i, file in enumerate(files):
        os.rename(os.path.join(path, file), os.path.join(path, str(i) + '.txt'))

    # 获取所有文件名
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    # 将文件后缀名命名回png
    for i, file in enumerate(files):
        os.rename(os.path.join(path, file), os.path.join(path, str(i) + '.png'))

    # 返回文件数量
    return len(files)


match_image("level", 1, 1)
