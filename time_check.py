"""
Check Pytorch time for inference
"""
import argparse
import numpy as np
import torch, torchvision
import torch.nn as nn
import torch.optim as optim
from torchvision import transforms, datasets
import torchvision.models as models
from EfficientNet_PyTorch.efficientnet_pytorch.model import EfficientNet
import time, os, copy, random, json
import pandas as pd


# python3 --weights [가중치 위치], --model[resnet은 0, efficient는 1입니다.] --data-path [test데이터 위치를 두시면 됩니다. ex)tmp/test] --img-size[160, 224] --csv-name [원하는 csv 이름 적어주시면 됩니다. ex)my_csv.csv]

def time_synchronized():
    # pytorch-accurate time
    if torch.cuda.is_available():
        torch.cuda.synchronize()
    return time.time()


def ready_data(root, img_size, batch_size=1):
    test_data_path = root

    my_dataset = datasets.ImageFolder(test_data_path,
                                      transforms.Compose([
                                          transforms.Resize((img_size, img_size)),
                                          transforms.ToTensor(),
                                          transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
                                      ]))

    dataloaders = {}
    dataloaders['test'] = torch.utils.data.DataLoader(my_dataset,
                                                      batch_size=batch_size, shuffle=False,
                                                      num_workers=4)

    return dataloaders['test']


def time_check(device, model, dataloaders):
    time_check_list = []
    starter, ender = torch.cuda.Event(enable_timing=True), torch.cuda.Event(enable_timing=True)
    repetitions = 300
    timings = np.zeros((repetitions, 1))

    with torch.no_grad():
        for i, (inputs, _) in enumerate(dataloaders['test']):
            inputs = inputs.to(device)
            for rep in range(repetitions):
                # 모델이 추론 시작하기 전 시간
                starter.record()
                outputs = model(inputs)
                _, preds = torch.max(outputs, 1)
                ender.record()
                # WAIT FOR GPU SYNC
                torch.cuda.synchronize()
                curr_time = starter.elapsed_time(ender)
                timings[rep] = curr_time
            time_check_list.append(np.mean(timings[rep]))

    return time_check_list


def main():
    what_model, data_root, weight_root = opt.model, opt.data_path, opt.weights
    img_size, csv_name = opt.img_size, opt.csv_name

    batch_size = 1
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    if what_model == 1:
        model = EfficientNet.from_pretrained('efficientnet-b0', num_classes=3)
        print("Clear EfficientNet Loading!")

        test_data_path = data_root

        dataloaders = {}
        dataloaders['test'] = ready_data(test_data_path, img_size, batch_size)

        model.load_state_dict(torch.load(weight_root))

        model = model.to(device)

        time_list = time_check(device, model, dataloaders)
        pd.DataFrame(time_list).to_csv(csv_name, index=False, encoding='utf-8')
        print("Csv Store Clear")

    elif what_model == 0:
        model = models.resnet50(pretrained=True)
        num_ftrs = model.fc.in_features
        model.fc = nn.Linear(num_ftrs, 2)

        print("Clear Resnet Loading!")
        test_data_path = data_root

        dataloaders = {}
        dataloaders['test'] = ready_data(test_data_path, img_size, batch_size)

        model.load_state_dict(torch.load(weight_root))

        model = model.to(device)

        time_list = time_check(device, model, dataloaders)
        pd.DataFrame(time_list).to_csv(csv_name, index=False, encoding='utf-8')
        print("Csv Store Clear")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', type=str, help='input model root')
    parser.add_argument('--model', type=int, help='resnet is 0 efficient is 1')
    parser.add_argument('--data-path', type=str, help='input datasets root')
    parser.add_argument('--img-size', type=int, help='model_img_size')
    parser.add_argument('--csv-name', type=str, help='input store csv name')

    opt = parser.parse_args()
    main()
