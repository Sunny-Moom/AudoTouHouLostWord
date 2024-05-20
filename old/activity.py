import os
import time

import main_functions


def main_run():
    # 主程序
    player_path = "img/player"
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
    while True:
        print("\033[32m" + f"战斗中，这是第 {xh} 次循环" + "\033[0m")
        main_functions.match_image("fight", 11, 2)
        time.sleep(1)
        main_functions.match_image("fight", 1, 2)
        time.sleep(1)
        main_functions.match_image("fight", 2, 2)
        time.sleep(1)
        main_functions.match_image("fight", 3, 2)
        time.sleep(1)
        main_functions.match_image("fight", 4, 2)
        time.sleep(1)
        main_functions.match_image("player", 1, 1)
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
        main_functions.search_tap("fight", 10, 1, 60)
        xh += 1
