import sys
import time
import cv2
import numpy as np
import utils.adb_lw as adb


def clear_console():
    """清除控制台输出。"""
    sys.stdout.write("\033[F")  # 光标上移一行。
    sys.stdout.write("\033[K")  # 清除当前行。


def load_and_match_image(template_folder, image_num):
    """加载屏幕和模板图像，并使用OpenCV进行匹配。"""
    adb.adb_image()
    screen_path = './data/img/screen.png'
    template_path = f'./data/img/{template_folder}/{image_num}.png'
    screen_img = cv2.imread(screen_path)
    template_img = cv2.imread(template_path)
    if screen_img is None or template_img is None:
        raise FileNotFoundError("未找到屏幕或模板图像。")
    template_height, template_width = template_img.shape[:-1]
    result = cv2.matchTemplate(screen_img, template_img, cv2.TM_CCOEFF_NORMED)
    return template_width, template_height, np.where(result >= 0.8)


def find_and_act_on_image(template_folder, image_num, cooldown, action, max_attempts=None):
    """在屏幕上找到图像并执行操作（点击或返回坐标）。"""
    attempts = 0
    while max_attempts is None or attempts < max_attempts:
        attempts += 1
        width, height, locations = load_and_match_image(template_folder, image_num)
        if locations[0].size > 0:
            center = (locations[1][0] + width // 2, locations[0][0] + height // 2)
            if action == 'click':
                adb.adb_touch(center[0], center[1])
                time.sleep(cooldown)
                return True
            elif action == 'report':
                return center
        else:
            if max_attempts is not None and attempts >= max_attempts:
                print("\033[31m" + "在尝试限制内未找到图像，继续下一步。" + "\033[0m")
            else:
                print("\033[31m" + f"未找到图像，{cooldown}秒后重试..." + "\033[0m")
            clear_console()
            time.sleep(cooldown)
    return False


def search_and_tap(template_folder, image_num, search_time, cooldown):
    """搜索一定时间的图像，如果找到则点击。"""
    result = find_and_act_on_image(template_folder, image_num, cooldown, 'report', max_attempts=search_time)
    if result:
        adb.adb_touch(result[0], result[1])
        time.sleep(cooldown)
