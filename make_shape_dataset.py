import os
import json


def mkd(shape, val):
    for i, img in enumerate(os.listdir(f'data/{shape}/left')):
        if i < 200:
            os.system(f"cp data/{shape}/left/{img} shape_dataset/train/")
            ft.write(f'shape_dataset/train/{img} {val}\n')
        elif i < 250:
            os.system(f"cp data/{shape}/left/{img} shape_dataset/val/")
            fv.write(f'shape_dataset/val/{img} {val}\n')

    for i, img in enumerate(os.listdir(f'data/{shape}/right')):
        if i < 200:
            os.system(f"cp data/{shape}/right/{img} shape_dataset/train/")
            ft.write(f'shape_dataset/train/{img} {val}\n')
        elif i < 250:
            os.system(f"cp data/{shape}/right/{img} shape_dataset/val/")
            fv.write(f'shape_dataset/val/{img} {val}\n')


if __name__ == '__main__':
    os.makedirs('shape_dataset/train/', exist_ok=True)
    os.makedirs('shape_dataset/val/', exist_ok=True)

    ft = open('shape_dataset/train.txt', 'wt')
    fv = open('shape_dataset/val.txt', 'wt')

    from shape_map import cls_map
    for shape in cls_map:
        mkd(shape, cls_map[shape])

    ft.close()
    fv.close()

