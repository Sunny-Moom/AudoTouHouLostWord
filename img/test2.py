# 导入PIL和pytesseract模块
from PIL import Image
import pytesseract


# 定义一个函数，接受一个图片路径和一个词作为参数
def get_word_coordinates(image_path, word):
    # 打开图片文件
    img = Image.open(image_path)

    # 设置tesseract命令行参数
    config = ("-l chi_sim --oem 1 --psm 3")

    # 调用image_to_data方法，返回一个字典列表
    data = pytesseract.image_to_data(img, config=config, output_type=pytesseract.Output.DICT)

    # 遍历字典列表，检查是否有匹配的词
    for i in range(len(data["text"])):
        if data["text"][i] == word:
            # 返回词的坐标，格式为(x,y,w,h)
            return (data["left"][i], data["top"][i], data["width"][i], data["height"][i])

    # 如果没有匹配，返回None
    return None


# 测试函数，使用一个示例图片和词
image_path = "screen.png"
word = "距离"
coordinates = get_word_coordinates(image_path, word)
print(f"{word}: {coordinates}")