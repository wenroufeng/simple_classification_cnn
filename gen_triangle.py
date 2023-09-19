import random
from PIL import Image, ImageDraw
import os




def left_triangle():
    os.makedirs('data/triangles/left', exist_ok=True)
    for i in range(1000):
        # 创建一张白色背景的图像，大小为300x300像素
        width, height = 300, 300
        image = Image.new('RGB', (width, height), 'white')
        draw = ImageDraw.Draw(image)
        x1, y1 = random.randint(0, width // 2 - 100), random.randint(100, 200)
        x2, y2 = x1 + random.randint(20, 50), y1 + random.randint(20, 50)
        x3, y3 = x2 + random.randint(10, width // 2 - 50), y1 - random.randint(10, height // 2 - 50)

        # 绘制锐角三角形，可以修改颜色
        draw.polygon([(x1, y1), (x2, y2), (x3, y3)], outline='black', fill=None)

        # 保存生成的图像
        image.save(f'data/triangles/left/{i}_left_triangle.png')


def right_triangle():
    os.makedirs('data/triangles/right', exist_ok=True)
    for i in range(1000):
        # 创建一张白色背景的图像，大小为300x300像素
        width, height = 300, 300
        image = Image.new('RGB', (width, height), 'white')
        draw = ImageDraw.Draw(image)
        x1, y1 = random.randint(width // 2, width // 2 + 50), random.randint(100, 200)
        x2, y2 = x1 + random.randint(20, 50), y1 + random.randint(20, 50)
        x3, y3 = x2 + random.randint(10, 50), y1 - random.randint(10, height // 2 - 50)

        # 绘制锐角三角形，可以修改颜色
        draw.polygon([(x1, y1), (x2, y2), (x3, y3)], outline='black', fill=None)

        # 保存生成的图像
        image.save(f'data/triangles/right/{i}_right_triangle.png')
        # break


if __name__ == '__main__':
    left_triangle()
    right_triangle()
