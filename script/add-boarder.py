from PIL import Image, ImageOps

def add_border(image_path, border_width, border_color):
    # 打开图片
    image = Image.open(image_path)

    # 添加边框
    bordered_image = ImageOps.expand(image, border=border_width, fill=border_color)

    return bordered_image

# 使用示例
import sys, os, argparse



if __name__ == '__main__':
    for i in range(len(sys.argv)):
        if i == 0:
            continue
        img = sys.argv[i]
        borded = add_border(img, border_width=5, border_color=(0, 0, 0))
    
        borded.save(img)
