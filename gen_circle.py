import random
from PIL import Image, ImageDraw
import os


def left_circle():
    os.makedirs('data/circles/left', exist_ok=True)
    for i in range(1000):
        # 创建一张白色背景的图像，大小为300x300像素
        width, height = 300, 300
        image = Image.new('RGB', (width, height), 'white')
        draw = ImageDraw.Draw(image)
        x1, y1 = random.randint(0, width // 2 - 100), random.randint(0, 200)
        diameter = random.randint(30, 100)
        x2, y2 = x1 + diameter, y1 + diameter

        draw.ellipse([(x1, y1), (x2, y2)], outline='black', fill=None)

        # 保存生成的图像
        image.save(f'data/circles/left/{i}_left_circle.png')


def right_circle():
    os.makedirs('data/circles/right', exist_ok=True)
    for i in range(1000):
        # 创建一张白色背景的图像，大小为300x300像素
        width, height = 300, 300
        image = Image.new('RGB', (width, height), 'white')
        draw = ImageDraw.Draw(image)
        x1, y1 = random.randint(width // 2, width // 2 + 50), random.randint(0, 200)
        diameter = random.randint(30, 100)
        x2, y2 = x1 + diameter, y1 + diameter

        draw.ellipse([(x1, y1), (x2, y2)], outline='black', fill=None)

        # 保存生成的图像
        image.save(f'data/circles/right/{i}_right_circle.png')
        # break


if __name__ == '__main__':
    left_circle()
    right_circle()
