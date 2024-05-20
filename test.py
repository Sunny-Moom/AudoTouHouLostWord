import utils.cv_lw as cv
import utils.ocr_lw as ocr
import utils.adb_lw as adb
import utils.other_lw as ot

if __name__ == '__main__':
    ptd = 0
    xyd = 0
    adb.cls()
    players = 0
    numb = 0
    while True:
        numb = numb + 1
        if players >= 14:
            players = 0
        cv.clear_console()
        print(f"现在是第{numb}次轮换,获得了{ptd}活动点，{xyd}稀有活动点")
        while not ocr.find_text_in_image('逆流而上的是'):
            print('未找到关卡文字，将在5秒后重新查找')
            ot.progress_bar(5)
            cv.clear_console()
            cv.clear_console()

        # 遍历寻找并点击特定图像
        for i in range(15):
            while True:
                image_result = cv.find_and_act_on_image('ft', i, 1, 'report', 4)
                if i == 5:
                    player_result = cv.find_and_act_on_image('pl', players, 1, 'report', 4)
                    if player_result:
                        adb.adb_touch(player_result[0], player_result[1])
                    else:
                        cv.find_and_act_on_image('ft', i - 1, 1, 'click', 4)
                if image_result:
                    adb.adb_touch(image_result[0], image_result[1])
                    break
                elif i == 0:
                    continue
                else:
                    cv.find_and_act_on_image('ft', i - 1, 1, 'click', 4)
        # 点击第15个图像
        while True:
            image_14_result = cv.find_and_act_on_image('ft', 15, 1, 'report', 4)
            if image_14_result:
                ot.crop_image(625, 410, 275, 113, "fs/" + str(1))
                ptd = ptd + int(ocr.find_num_in_image('./data/img/fs/1.png'))
                ot.crop_image(1103, 410, 275, 113, "fs/" + str(2))
                xyd = xyd + int(ocr.find_num_in_image('./data/img/fs/2.png'))
                adb.adb_touch(image_14_result[0], image_14_result[1])
                break
            else:
                print('战斗中')
                ot.progress_bar(60)
                cv.clear_console()
                cv.clear_console()

        players += 1
