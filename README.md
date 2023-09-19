## 生成三角形、方形、圆形数据
```
gen_circle.py、gen_square.py、gen_triangle.py 会在data目录下分别生成圆形、方形、三角形。
```

## 可视化data
```
view_data.py 用于可视化gen_circle.py、gen_square.py、gen_triangle.py生成的图片。
例如 python view_data.py triangles left 可视化三角形在图片左边的图片。
```

## 生成训练数据集
```
make_shape_dataset.py 用于生成训练形状的数据集；
make_pos_dataset.py 用于生成训练位置的数据集。
```

## 训练数据
```
train_shape.py 用于训练形状；
train_pos.py 用于训练位置。
```

## 验证以及可视化训练出来的模型效果
```
use_shape_model.py 用于验证形状模型效果；
use_pos_model.py 用于验证位置模型效果。
注意脚本里面的model参数加载的模型要替换成自己训练的效果最好的模型。
```
