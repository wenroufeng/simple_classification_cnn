import os
import torch
from PIL import Image
import torchvision
from torch import nn
from train_shape import Residual
import fiftyone as fo
from shape_map import cls_map
import random

transform = torchvision.transforms.Compose([torchvision.transforms.Resize((300, 300)),
                                            torchvision.transforms.ToTensor()])

device = 'cuda' if torch.cuda.is_available() else 'cpu'

model = torch.load("shape_models/model_10.pth", map_location=torch.device(device))

v_c_map = {}
for c in cls_map:
    v_c_map[cls_map[c]] = c


triangles_left = [f'data/triangles/left/{i}' for i in os.listdir('data/triangles/left')[-100: ]]
triangles_right = [f'data/triangles/right/{i}' for i in os.listdir('data/triangles/right')[-100: ]]
squares_left = [f'data/squares/left/{i}' for i in os.listdir('data/squares/left')[-100: ]]
squares_right = [f'data/squares/right/{i}' for i in os.listdir('data/squares/right')[-100: ]]
circles_left = [f'data/circles/left/{i}' for i in os.listdir('data/circles/left')[-100: ]]
circles_right = [f'data/circles/right/{i}' for i in os.listdir('data/circles/right')[-100: ]]


data = triangles_left + triangles_right + squares_left + squares_right + circles_left + circles_right
random.shuffle(data)

dataset = fo.Dataset()
for im in data:
    dataset.add_sample(fo.Sample(im))

with torch.no_grad():
    j = 0
    for sample in dataset.iter_samples(autosave=True):
        try:
            image = Image.open(sample.filepath)
            image = image.convert('RGB')
            image = transform(image)
            image = torch.reshape(image, (1, 3, 300, 300)).to(device)
        except Exception as e:
            continue
        model.eval()
        output = model(image)
        # print('***********out: ', output.softmax(dim=1))
        sample['形状'] = fo.Classification(label=v_c_map[output.argmax(1).tolist()[0]], confidence=output.softmax(dim=1).flatten().tolist()[1])

session = fo.launch_app(dataset, address="10.158.99.23", port=8000)
session.wait()


