import threading
import time

import daily_task
import main_functions
import pai

lock = threading.Lock()
evn = True  # 初始化公共变量evn为True
def worker():
    while True:
        global evn
        # 线程执行的代码
        time.sleep(10)
        evn=False
        print("tttt")

# 创建并启动工作线程
t = threading.Thread(target=worker)
t.start()
while evn:
    main_functions.search_tap("fight", 10, 1, 5)
if not evn:
    main_functions.press(main_functions.search_image("evn", 1, 5), 5)