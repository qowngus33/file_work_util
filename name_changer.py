"""
Read Images and change name in order
"""
import os
import shutil

path = "/Volumes/NONAME/construction_dataset/"
folder = "0803(L)/"
combs = os.listdir(path+folder+"images/")
combs.sort()
out_dir = path + folder + "comb_images/"
loc_code = "005"
print(combs)

count = 1644

for comb in combs:
    print(comb, end="\r")
    # if not os.path.exists(os.path.join(out_dir, comb)):
    #     os.mkdir(os.path.join(out_dir, comb))
    for filename in os.listdir((os.path.join(path + folder + "images/", comb))):
        file_path = os.path.join(path + folder + "images/", comb, filename)
        newname = f"{loc_code}_{comb}_c{str(count).zfill(6)}.jpg"
        shutil.copy(file_path, os.path.join(out_dir, newname))
        print(newname)
        count += 1
