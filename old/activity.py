import os
import threading
import time

import main_functions
import pai

evn = True  # 初始化公共变量evn为True
def worker():
    while True:
        global evn
        # 线程执行的代码
        time.sleep(4000)
        evn=False

# 创建并启动工作线程
t = threading.Thread(target=worker)
t.start()

# 主程序
filename = input("请输入角色池槽位：")
# 角色池路径
player_path = "img/player_" + str(filename)
os.system('cls')
print("##############脚本已启动##############")
print("#         正在加载上场角色池         #")
player_count = main_functions.rename_files(player_path)
print(f"角色池载入成功，本次战斗角色一共有 {player_count} 位")
print("#   关卡加载成功，脚本将在5秒后运行  #")
print("##############脚本已启动##############")
time.sleep(5)
player = 0
xh = 1
while evn:
    print("\033[32m" + f"战斗中，这是第 {xh} 次循环" + "\033[0m")
    main_functions.match_image("fight", 11, 2, 0.9)
    time.sleep(1)
    main_functions.match_image("fight", 1, 2)
    time.sleep(1)
    main_functions.match_image("fight", 2, 2)
    time.sleep(1)
    main_functions.match_image("fight", 3, 2)
    time.sleep(1)
    main_functions.match_image("fight", 4, 2)
    time.sleep(1)
    main_functions.match_image("player_" + str(filename), player, 1)
    player += 1
    if player == player_count:
        player = 0
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
    while evn:
        main_functions.search_tap("fight", 10, 1, 60)
    if not evn:
        main_functions.press(main_functions.search_image("evn", 1, 5), 5)
        time.sleep(6)
        main_functions.match_image("fight", 10, 4)
        time.sleep(2)
        main_functions.match_image("evn", 2, 4)
        time.sleep(2)
        pai.day_pai()
        time.sleep(2)
        main_functions.match_image("evn", 3, 4)
        time.sleep(2)
        evn=True
    xh += 1
