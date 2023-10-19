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
    parser = argparse.ArgumentParser()
    # parser.add_argument("other_args", nargs="*", type=str, required=True)
    parser.add_argument("inputfile")
    parser.add_argument("-w", "--width", type=int, help='input the desired boarder width', 
                        required=True, default=5)
    # parser.add_argument("-o", "--outputfile", )

    args = parser.parse_args()

    image_path = args.inputfile

    border_width = args.width
    print(f'get arg of width: {border_width}')
    border_color = (0, 0, 0)  # 边框颜色，RGB格式，例如红色为(255, 0, 0)

    bordered_image = add_border(image_path, border_width, border_color)

    bordered_image.save('new1.png')