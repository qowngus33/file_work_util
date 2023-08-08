import numpy as np
import cv2
import os
from tqdm import tqdm
import shutil

if __name__ == "__main__":
    number = "3/"
    path = "/Volumes/NONAME/lab_dataset/test/test_crawl/"
    folder = "001/images/" + number
    save_folder = "001/labels/" + number

    jpg = []

    os.chdir(path+folder)  # 해당 폴더로 이동
    files = os.listdir(path+folder)  # 해당 폴더에 있는 파일 이름을 리스트 형태로 받음

    files.sort()
    for i, file in enumerate(tqdm(files)):
        if "jpg" in file:
            txt = file[:-3] + "txt"
            try:
                shutil.copy(path + "labels/" + txt, path + save_folder)
            except:
                try:
                    print(txt)
                    txt = txt.replace("019", "001")
                    shutil.copy(path + "labels/" + txt, path + save_folder)
                except:
                    print(file)


