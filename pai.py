import time

import numpy as np

import main_functions


def day_pai1():
    center = main_functions.search_image("pai", 4, 5)
    while center:
        main_functions.tap(center)
        time.sleep(2)
        main_functions.match_image("pai", 5, 1)
        time.sleep(2)
        main_functions.match_image("pai", 6, 1)
        time.sleep(2)
        main_functions.match_image("pai", 8, 1)
        time.sleep(2)
        center = main_functions.search_image("pai", 4, 5)


def day_pai2():
    main_functions.search_tap("pai", 0, 5, 2)
    main_functions.search_tap("pai", 9, 5, 2)
    day_pai1()
    main_functions.match_image("pai", 7, 1)
    day_pai1()

def day_num():
    coords = []
    coords = main_functions.search_image_all("pai", 11, 5)
    if coords:
        # 按 y 轴坐标排序
        coords = sorted(coords, key=lambda coord: coord[1])
        # 将坐标按照 y 轴坐标归为一类
        classes = {}
        class_idx = 0
        for coord in coords:
            if not classes:
                classes[class_idx] = [coord]
            else:
                last_coord = classes[class_idx][-1]
                if abs(coord[1] - last_coord[1]) < 100:
                    classes[class_idx].append(coord)
                else:
                    class_idx += 1
                    classes[class_idx] = [coord]
        # 输出每个类别中的坐标和平均坐标
        mean_coords = []
        for class_idx, class_coords in classes.items():
            # 计算平均坐标，并四舍五入为整数
            x_mean = int(np.round(np.mean([coord[0] for coord in class_coords])))
            y_mean = int(np.round(np.mean([coord[1] for coord in class_coords])))
            mean_coords.append((x_mean, y_mean))
        return mean_coords
    else:
        return False
def day_pai3(num):
    cd = True
    cd=main_functions.search_image("pai", 15, 5, 0.9)
    coords = []
    coords = main_functions.search_image_all("pai", num, 5)
    if coords and not cd:
        # 按 y 轴坐标排序
        coords = sorted(coords, key=lambda coord: coord[1])
        # 将坐标按照 y 轴坐标归为一类
        classes = {}
        class_idx = 0
        for coord in coords:
            if not classes:
                classes[class_idx] = [coord]
            else:
                last_coord = classes[class_idx][-1]
                if abs(coord[1] - last_coord[1]) < 100:
                    classes[class_idx].append(coord)
                else:
                    class_idx += 1
                    classes[class_idx] = [coord]
        # 输出每个类别中的坐标和平均坐标
        mean_coords = []
        for class_idx, class_coords in classes.items():
            # 计算平均坐标，并四舍五入为整数
            x_mean = int(np.round(np.mean([coord[0] for coord in class_coords])))
            y_mean = int(np.round(np.mean([coord[1] for coord in class_coords])))

            mean_coords.append((x_mean, y_mean))
        center = main_functions.search_image("pai", 3, 5, 0.9)
        if center:
            mean_coords = [coord for coord in mean_coords if abs(coord[1] - center[1]) >= 100]
        xii=day_num()
        if xii:
            for xi in xii:
                mean_coords = [coord for coord in mean_coords if abs(coord[1] - xi[1]) >= 100]
        xii=False
        return mean_coords
    else:
        return False


def day_pai4(num):
    mean = day_pai3(num)
    cd = True
    cd = main_functions.search_image("pai", 15, 5, 0.9)
    if mean and not cd:
        main_functions.tap(mean[0])
        time.sleep(2)
        main_functions.match_image("pai", 12, 1)
        time.sleep(2)
        main_functions.match_image("pai", 13, 1)
        time.sleep(2)
        main_functions.match_image("pai", 11, 1)
        time.sleep(2)
    mean = False


def day_pai5(num):
    ba = (774, 809)
    ab = (774, 309)
    time.sleep(3)
    day_pai4(num)
    main_functions.row(ba, 0, -500, 2)
    time.sleep(3)
    day_pai4(num)
    main_functions.row(ab, 0, 500, 2)
    time.sleep(3)
    main_functions.match_image("pai", 10, 1)
    day_pai4(num)
    main_functions.row(ba, 0, -500, 2)
    time.sleep(3)
    day_pai4(num)
    main_functions.row(ab, 0, 500, 2)
    time.sleep(3)
    main_functions.match_image("pai", 7, 1)


def day_pai():
    cd = True
    cd = main_functions.search_image("pai", 15, 5, 0.9)
    ad=[1,17,2,14]
    day_pai2()
    if not cd:
        for da in ad:
            day_pai5(da)
    main_functions.match_image("pai", 16, 1)
