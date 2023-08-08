import numpy as np
import cv2
import os
from tqdm import tqdm
from file_to_list import file_to_list_func

if __name__ == "__main__":
    path = "/Volumes/NONAME/construction_dataset/0803(O)/"
    folder = "Galaxy/"
    save_folder = "images/"

    f = open("label.txt", "r")

    folder_names_list = []
    while True:
        line = f.readline().strip().split(" ")
        if line[0] != "":
            folder_names_list.append(line[0])
        else:
            break

    print(folder_names_list)
    print(len(folder_names_list))

    jpg = []

    os.chdir(path+folder)  # 해당 폴더로 이동
    files = os.listdir(path+folder)  # 해당 폴더에 있는 파일 이름을 리스트 형태로 받음
    files.sort()
    for i, file in enumerate(tqdm(files)):
        img = cv2.imread(file)
        if i % 3 == 0 and not os.path.exists(path+save_folder+folder_names_list[i//3].zfill(4)):
            os.mkdir(path+save_folder+folder_names_list[i//3].zfill(4))
        try:
            img = cv2.imwrite(path+save_folder+folder_names_list[i//3].zfill(4)+"/"+file, img)
        except:
            print(path+save_folder+folder_names_list[i//3].zfill(4)+"/"+file)

