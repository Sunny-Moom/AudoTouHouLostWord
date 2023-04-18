adb shell screencap -p /sdcard/screen.png
adb pull /sdcard/screen.png ./img/screen.png
adb shell rm /sdcard/screen.png