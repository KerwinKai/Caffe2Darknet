# Caffe2Darknet

A model conversion tool written in python3, supports caffe2darknet.

> This project is adapted based on [pytorch-caffe-darknet-convert](https://github.com/linzhi123/pytorch-caffe-darknet-convert), hoping to support the model conversion to [darknet](https://github.com/AlexeyAB/darknet). We look forward to your forking this project and submitting an improved [pr](https://github.com/KerwinKai/Caffe2Darknet/pulls), and improving the details of model conversion so that it can better adapt to [darknet](https://github.com/AlexeyAB/darknet).

## Start

Activate the conda environment of Python and the corresponding library dependencies

```
conda create -n py37 python=3.7
conda activate py37
pip install brocolli-caffe
git clone https://github.com/KerwinKai/Caffe2Darknet.git
```

## Use

example

```
if __name__ == '__main__':
    net_path = './ResNet18/resnet18.prototxt'
    weight_path = './ResNet18/resnet18.caffemodel'
    out_file_path = './ResNet18/resnet18'
    c2d = Caffe2Darknet(net = net_path, weight = weight_path, out_file = out_file_path)
    c2d.convert()
```

## Log

```
Loading caffemodel:  ./ResNet18/resnet18.caffemodel
0 conv1 Convolution
1 bn1_bn BatchNorm
2 bn1 Scale
3 relu ReLU
4 maxpool Pooling
5 layer1_0_conv1 Convolution
6 layer1_0_bn1_bn BatchNorm
7 layer1_0_bn1 Scale
8 layer1_0_relu ReLU
9 layer1_0_conv2 Convolution
10 layer1_0_bn2_bn BatchNorm
11 layer1_0_bn2 Scale
12 add Eltwise
14 layer1_1_conv1 Convolution
15 layer1_1_bn1_bn BatchNorm
16 layer1_1_bn1 Scale
17 layer1_1_relu ReLU
18 layer1_1_conv2 Convolution
19 layer1_1_bn2_bn BatchNorm
20 layer1_1_bn2 Scale
21 add_1 Eltwise
23 layer2_0_conv1 Convolution
24 layer2_0_bn1_bn BatchNorm
25 layer2_0_bn1 Scale
26 layer2_0_relu ReLU
27 layer2_0_conv2 Convolution
28 layer2_0_bn2_bn BatchNorm
29 layer2_0_bn2 Scale
30 layer2_0_downsample_0 Convolution
31 layer2_0_downsample_1_bn BatchNorm
32 layer2_0_downsample_1 Scale
33 add_2 Eltwise
35 layer2_1_conv1 Convolution
36 layer2_1_bn1_bn BatchNorm
37 layer2_1_bn1 Scale
38 layer2_1_relu ReLU
39 layer2_1_conv2 Convolution
40 layer2_1_bn2_bn BatchNorm
41 layer2_1_bn2 Scale
42 add_3 Eltwise
44 layer3_0_conv1 Convolution
45 layer3_0_bn1_bn BatchNorm
46 layer3_0_bn1 Scale
47 layer3_0_relu ReLU
48 layer3_0_conv2 Convolution
49 layer3_0_bn2_bn BatchNorm
50 layer3_0_bn2 Scale
51 layer3_0_downsample_0 Convolution
52 layer3_0_downsample_1_bn BatchNorm
53 layer3_0_downsample_1 Scale
54 add_4 Eltwise
56 layer3_1_conv1 Convolution
57 layer3_1_bn1_bn BatchNorm
58 layer3_1_bn1 Scale
59 layer3_1_relu ReLU
60 layer3_1_conv2 Convolution
61 layer3_1_bn2_bn BatchNorm
62 layer3_1_bn2 Scale
63 add_5 Eltwise
65 layer4_0_conv1 Convolution
66 layer4_0_bn1_bn BatchNorm
67 layer4_0_bn1 Scale
68 layer4_0_relu ReLU
69 layer4_0_conv2 Convolution
70 layer4_0_bn2_bn BatchNorm
71 layer4_0_bn2 Scale
72 layer4_0_downsample_0 Convolution
73 layer4_0_downsample_1_bn BatchNorm
74 layer4_0_downsample_1 Scale
75 add_6 Eltwise
77 layer4_1_conv1 Convolution
78 layer4_1_bn1_bn BatchNorm
79 layer4_1_bn1 Scale
80 layer4_1_relu ReLU
81 layer4_1_conv2 Convolution
82 layer4_1_bn2_bn BatchNorm
83 layer4_1_bn2 Scale
84 add_7 Eltwise
86 avgpool Pooling
87 flatten Flatten
unknown type Flatten
88 fc InnerProduct
done
Save to  ./ResNet18/resnet18.weights
[net]
batch=1
channels=3
height=224
width=224

[convolutional]
filters=64
size=7
stride=2
pad=1
batch_normalize=1
activation=relu

[maxpool]
size=3
stride=2
pad=1

[convolutional]
filters=64
size=3
stride=1
pad=1
batch_normalize=1
activation=relu

[convolutional]
filters=64
size=3
stride=1
pad=1
batch_normalize=1
activation=linear

[shortcut]
from=-3
activation=relu

[convolutional]
filters=64
size=3
stride=1
pad=1
batch_normalize=1
activation=relu

[convolutional]
filters=64
size=3
stride=1
pad=1
batch_normalize=1
activation=linear

[shortcut]
from=-3
activation=relu

[convolutional]
filters=128
size=3
stride=2
pad=1
batch_normalize=1
activation=relu

[convolutional]
filters=128
size=3
stride=1
pad=1
batch_normalize=1
activation=linear

[route]
layers=-3

[convolutional]
filters=128
size=1
stride=2
pad=1
batch_normalize=1
activation=linear

[shortcut]
from=-3
activation=relu

[convolutional]
filters=128
size=3
stride=1
pad=1
batch_normalize=1
activation=relu

[convolutional]
filters=128
size=3
stride=1
pad=1
batch_normalize=1
activation=linear

[shortcut]
from=-3
activation=relu

[convolutional]
filters=256
size=3
stride=2
pad=1
batch_normalize=1
activation=relu

[convolutional]
filters=256
size=3
stride=1
pad=1
batch_normalize=1
activation=linear

[route]
layers=-3

[convolutional]
filters=256
size=1
stride=2
pad=1
batch_normalize=1
activation=linear

[shortcut]
from=-3
activation=relu

[convolutional]
filters=256
size=3
stride=1
pad=1
batch_normalize=1
activation=relu

[convolutional]
filters=256
size=3
stride=1
pad=1
batch_normalize=1
activation=linear

[shortcut]
from=-3
activation=relu

[convolutional]
filters=512
size=3
stride=2
pad=1
batch_normalize=1
activation=relu

[convolutional]
filters=512
size=3
stride=1
pad=1
batch_normalize=1
activation=linear

[route]
layers=-3

[convolutional]
filters=512
size=1
stride=2
pad=1
batch_normalize=1
activation=linear

[shortcut]
from=-3
activation=relu

[convolutional]
filters=512
size=3
stride=1
pad=1
batch_normalize=1
activation=relu

[convolutional]
filters=512
size=3
stride=1
pad=1
batch_normalize=1
activation=linear

[shortcut]
from=-3
activation=relu

[avgpool]

[Flatten]

[connected]
output=1000
activation=linear

layer     filters    size              input                output
    0 conv     64  7 x 7 / 2   224 x 224 x   3   ->   112 x 112 x  64
    1 max          3 x 3 / 2   112 x 112 x  64   ->    56 x  56 x  64
    2 conv     64  3 x 3 / 1    56 x  56 x  64   ->    56 x  56 x  64
    3 conv     64  3 x 3 / 1    56 x  56 x  64   ->    56 x  56 x  64
    4 shortcut 1
    5 conv     64  3 x 3 / 1    56 x  56 x  64   ->    56 x  56 x  64
    6 conv     64  3 x 3 / 1    56 x  56 x  64   ->    56 x  56 x  64
    7 shortcut 4
    8 conv    128  3 x 3 / 2    56 x  56 x  64   ->    28 x  28 x 128
    9 conv    128  3 x 3 / 1    28 x  28 x 128   ->    28 x  28 x 128
   10 route  7
   11 conv    128  1 x 1 / 2    56 x  56 x  64   ->    28 x  28 x 128
   12 shortcut 9
   13 conv    128  3 x 3 / 1    28 x  28 x 128   ->    28 x  28 x 128
   14 conv    128  3 x 3 / 1    28 x  28 x 128   ->    28 x  28 x 128
   15 shortcut 12
   16 conv    256  3 x 3 / 2    28 x  28 x 128   ->    14 x  14 x 256
   17 conv    256  3 x 3 / 1    14 x  14 x 256   ->    14 x  14 x 256
   18 route  15
   19 conv    256  1 x 1 / 2    28 x  28 x 128   ->    14 x  14 x 256
   20 shortcut 17
   21 conv    256  3 x 3 / 1    14 x  14 x 256   ->    14 x  14 x 256
   22 conv    256  3 x 3 / 1    14 x  14 x 256   ->    14 x  14 x 256
   23 shortcut 20
   24 conv    512  3 x 3 / 2    14 x  14 x 256   ->     7 x   7 x 512
   25 conv    512  3 x 3 / 1     7 x   7 x 512   ->     7 x   7 x 512
   26 route  23
   27 conv    512  1 x 1 / 2    14 x  14 x 256   ->     7 x   7 x 512
   28 shortcut 25
   29 conv    512  3 x 3 / 1     7 x   7 x 512   ->     7 x   7 x 512
   30 conv    512  3 x 3 / 1     7 x   7 x 512   ->     7 x   7 x 512
   31 shortcut 28
   32 avg                        7 x   7 x 512   ->      512
unknown type Flatten
   34 connected                            512  ->      1000
Hash of Darknet model has been published:  fc7ccc2dc0e8966994cc28ac0841cddd
True
```

## code style check

In the local development environment, we use `pre-commit` to check the code style to ensure the uniformity of the code style. Before submitting code, you can install pre-commit first, or you can submit directly, I will maintain the code style regularly.
