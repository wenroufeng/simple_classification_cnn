from turtle import position
import fiftyone as fo
import sys


shape = sys.argv[1]
position = sys.argv[2]

dataset = fo.Dataset.from_images_dir(f'data/{shape}/{position}')

session = fo.launch_app(dataset, address="10.158.99.23", port=8000)
session.wait()

# while True:
#     a = input('>>>>>>')
#     if a:
#         if not session.view:
#             print("请确定过滤")
#             continue
#         with open('del.txt', 'wt') as f:
#             for s in session.view:
#                 f.write(s.filepath + '\n')
#                 print(s.filepath)
