"""
Delete Roboflow garbage file name
"""
import numpy as np
import cv2
import os
from tqdm import tqdm
from file_to_list import file_to_list_func

if __name__ == "__main__":
    path = "/Volumes/NONAME/VIG_Test_data/"
    folder = "labels/"

    txt = []
    jpg = []

    os.chdir(path+folder)  # 해당 폴더로 이동
    files = os.listdir(path+folder)  # 해당 폴더에 있는 파일 이름을 리스트 형태로 받음
    files.sort()
    for file in tqdm(files):
        if file.find("txt") != -1:
            idx = file.find("jpg")
            new_file = file[:idx+4] + "txt"
            os.rename(file,new_file)
        else:
            idx = file.find("jpg")
            new_file = file[:idx+4] + "jpg"
            os.rename(file,new_file)
