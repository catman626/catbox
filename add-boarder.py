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
    image_pth = sys.argv[1]
    
    bordered_image = add_border(image_pth, border_width=5, border_color=(0, 0, 0))

    bordered_image.save(image_pth)