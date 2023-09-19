import os
import json


def mkd(pos, val):
    for shape in ['triangles', 'squares', 'circles']:
        for i, img in enumerate(os.listdir(f'data/{shape}/{pos}')):
            if i < 200:
                os.system(f"cp data/{shape}/{pos}/{img} pos_dataset/train/")
                ft.write(f'pos_dataset/train/{img} {val}\n')
            elif i < 250:
                os.system(f"cp data/{shape}/{pos}/{img} pos_dataset/val/")
                fv.write(f'pos_dataset/val/{img} {val}\n')


if __name__ == '__main__':
    os.makedirs('pos_dataset/train/', exist_ok=True)
    os.makedirs('pos_dataset/val/', exist_ok=True)

    ft = open('pos_dataset/train.txt', 'wt')
    fv = open('pos_dataset/val.txt', 'wt')

    from pos_map import cls_map
    for pos in cls_map:
        mkd(pos, cls_map[pos])

    ft.close()
    fv.close()

