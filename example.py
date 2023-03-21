from caffe2darknet import Caffe2Darknet

if __name__ == '__main__':
    net_path = './ResNet18/resnet18.prototxt'
    weight_path = './ResNet18/resnet18.caffemodel'
    out_file_path = './ResNet18/resnet18'
    c2d = Caffe2Darknet(net=net_path,
                        weight=weight_path,
                        out_file=out_file_path)
    c2d.convert()
