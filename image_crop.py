"""
Read Files from given path and crop images
"""
import cv2
import os
from tqdm import tqdm

if __name__ == "__main__":
    path = "/Volumes/SANDISK123/"
    save_path = "/Volumes/SANDISK123/"
    folder = "new_get_4_28/"

    os.chdir(path+folder)  # 해당 폴더로 이동
    files = os.listdir(path+folder)  # 해당 폴더에 있는 파일 이름을 리스트 형태로 받음

    images = []
    txts = []
    for file in tqdm(files):
        if file.find("jpg") != -1:
            # img = cv2.imread(file)
            images.append(file)
        else:
            txts.append(file)
    print(len(images),len(txts))

    images.sort()
    txts.sort()

    for i, image in enumerate(images):
        img = cv2.imread(image)
        h, w, c = img.shape
        file = open(txts[i], "r")
        while True:
            line = file.readline()
            if not line:
                break
            numbers = int(line.split(" "))
            print(numbers)

        file.close()

