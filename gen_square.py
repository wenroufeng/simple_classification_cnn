import random
from PIL import Image, ImageDraw
import os


def left_square():
    os.makedirs('data/squares/left', exist_ok=True)
    for i in range(1000):
        # 创建一张白色背景的图像，大小为300x300像素
        width, height = 300, 300
        image = Image.new('RGB', (width, height), 'white')
        draw = ImageDraw.Draw(image)
        x1, y1 = random.randint(0, width // 2 - 100), random.randint(100, 200)
        x2, y2 = x1 + random.randint(20, 150), y1 + random.randint(20, 50)

        draw.rectangle([(x1, y1), (x2, y2)], outline='black', fill=None)

        # 保存生成的图像
        image.save(f'data/squares/left/{i}_left_square.png')


def right_square():
    os.makedirs('data/squares/right', exist_ok=True)
    for i in range(1000):
        # 创建一张白色背景的图像，大小为300x300像素
        width, height = 300, 300
        image = Image.new('RGB', (width, height), 'white')
        draw = ImageDraw.Draw(image)
        x1, y1 = random.randint(width // 2, width // 2 + 50), random.randint(100, 200)
        x2, y2 = x1 + random.randint(20, 100), y1 + random.randint(20, 50)

        draw.rectangle([(x1, y1), (x2, y2)], outline='black', fill=None)

        # 保存生成的图像
        image.save(f'data/squares/right/{i}_right_square.png')
        # break


if __name__ == '__main__':
    left_square()
    right_square()
