from datetime import datetime
import time
import main_functions


# 每日任务，领取邮件
def day_mail():
    main_functions.match_image("mail", 1, 1)
    time.sleep(2)
    main_functions.match_image("mail", 2, 1)
    time.sleep(2)
    main_functions.match_image("mail", 3, 1)
    time.sleep(2)
    main_functions.match_image("mail", 4, 1)
    time.sleep(2)


# 每日任务，领取好友金币
def day_friends():
    main_functions.match_image("friends", 1, 1)
    time.sleep(2)
    main_functions.search_tap("friends", 2, 5, 2)
    time.sleep(2)
    main_functions.search_tap("friends", 3, 5, 2)
    time.sleep(2)
    main_functions.match_image("friends", 4, 1)
    time.sleep(2)


# 每日任务，补充食物
def day_siziwu():
    main_functions.match_image("siziwu", 1, 1)
    time.sleep(2)
    main_functions.match_image("siziwu", 2, 1)
    time.sleep(2)
    main_functions.match_image("siziwu", 3, 1)
    time.sleep(2)
    main_functions.press(main_functions.search_image("siziwu", 4, 5), 5)
    main_functions.search_tap("siziwu", 7, 5, 3)
    main_functions.match_image("siziwu", 5, 1)
    time.sleep(2)
    main_functions.match_image("siziwu", 6, 1)
    time.sleep(2)


# 每日任务，技能升级
def day_dao():
    main_functions.match_image("dao", 1, 1)
    time.sleep(2)
    main_functions.match_image("dao", 2, 1)
    time.sleep(2)
    while True:
        center = main_functions.search_image("dao", 3, 5)
        if center:
            main_functions.tap(center)
            main_functions.search_tap("dao", 4, 5, 3)
            main_functions.search_tap("dao", 5, 5, 3)
            main_functions.search_tap("dao", 6, 5, 3)
            main_functions.match_image("dao", 7, 1)
            time.sleep(2)
            main_functions.match_image("dao", 3, 1)
            time.sleep(2)
        else:
            main_functions.match_image("dao", 8, 1)
            time.sleep(2)
            break


def day_fight():
    main_functions.match_image("fight", 1, 2)
    time.sleep(1)
    main_functions.match_image("fight", 2, 2)
    time.sleep(1)
    main_functions.match_image("fight", 3, 2)
    time.sleep(1)
    main_functions.match_image("fight", 4, 2)
    time.sleep(1)
    main_functions.match_image("day", 12, 1)
    time.sleep(1)
    main_functions.match_image("fight", 5, 2)
    time.sleep(1)
    main_functions.match_image("fight", 6, 2)
    time.sleep(1)
    main_functions.match_image("fight", 7, 2)
    time.sleep(1)
    main_functions.match_image("fight", 8, 2)
    time.sleep(1)
    main_functions.match_image("fight", 9, 2)
    time.sleep(60)
    main_functions.match_image("fight", 10, 10)


def day_1():
    main_functions.match_image("day", 3, 1)
    time.sleep(2)
    center = main_functions.search_image("day", 6, 5)
    if center:
        main_functions.row(center, 0, -800, 1)
        time.sleep(2)
    main_functions.match_image("day", 9, 1)
    day_fight()


def day_2():
    main_functions.match_image("day", 4, 1)
    time.sleep(2)
    center = main_functions.search_image("day", 7, 5)
    if center:
        main_functions.row(center, 0, -800, 1)
        time.sleep(2)
    main_functions.match_image("day", 10, 1)
    day_fight()


def day_3():
    main_functions.match_image("day", 5, 1)
    time.sleep(2)
    center = main_functions.search_image("day", 8, 5)
    if center:
        main_functions.row(center, 0, -800, 1)
        time.sleep(2)
    main_functions.match_image("day", 11, 1)
    day_fight()


# 每日任务，每日关卡
def day_day():
    main_functions.match_image("day", 1, 1)
    time.sleep(2)
    main_functions.search_tap("day", 2, 5, 3)
    d = datetime.now().weekday()
    if d == 0 or d == 3:
        day_1()
    elif d == 1 or d == 4:
        day_2()
    elif d == 2 or d == 5:
        day_3()
    main_functions.match_image("day", 13, 1)


# 每日任务，任务提交
def day_task():
    main_functions.match_image("task", 1, 1)
    time.sleep(3)
    center = main_functions.search_image("task", 2, 5)
    while center:
        main_functions.tap(center)
        time.sleep(2)
        main_functions.match_image("task", 3, 1)
        center = main_functions.search_image("task", 2, 5)
    main_functions.match_image("task", 4, 1)


# 启动游戏
def day_start():
    center = main_functions.search_image("start", 1, 5)
    stop = main_functions.search_image("start", 2, 1)
    fd = main_functions.search_image("friends", 1, 1)
    while stop == False or fd == False:
        main_functions.tap(center)
        stop = main_functions.search_image("start", 2, 1)
        fd = main_functions.search_image("friends", 1, 1)
    if stop:
        main_functions.tap(stop)


# 每日任务，抽卡
def day_chou():
    main_functions.match_image("start", 3, 1)
    time.sleep(2)
    main_functions.match_image("start", 4, 1)
    time.sleep(2)
    main_functions.match_image("start", 5, 1)
    time.sleep(2)
    main_functions.match_image("start", 6, 1)
    time.sleep(2)
    center = main_functions.search_image("start", 7, 5)
    stop = main_functions.search_image("start", 8, 1)
    while not stop:
        main_functions.tap(center)
        stop = main_functions.search_image("start", 8, 1)
    main_functions.tap(stop)
