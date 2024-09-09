# import the modules
import os
from os import listdir
from PIL import Image
import pillow_heif
import threading
from pillow_heif import register_heif_opener

register_heif_opener()
source_dir = "C:\\Users\\ravir\\OneDrive\\Documents\\Zapya\\Photo\\2024_04_02_121914\\"
dest_dir = "C:\\Users\\ravir\\OneDrive\\Documents\\Zapya\\Photo\\converted\\"
folder_dir2 = "C:\\Users\\ravir\\OneDrive\\Pictures\\Zapya\\2022_12_10_172257\\"


# img_size=1024


def img_conversion():
    for images in os.listdir(source_dir):
        if images.endswith(".HEIC"):
            # print(images)
            origin = source_dir + images
            c = images.split(".")[0]
            c_png = c + ".png"
            dest_png = dest_dir + c_png
            c_jpg = c + ".jpg"
            dest_jpg = dest_dir + c_jpg
            if (not os.path.exists(dest_jpg)):
                # heif_file = pillow_heif.read_heif(origin)
                # image = Image.frombytes(
                # heif_file.mode, heif_file.size, heif_file.data,"raw")
                image = Image.open(origin)
                # image.save(dest_png, format("png"))
                # image.resize((1024, 1024))
                image.save(dest_png)
                im = Image.open(dest_png)
                im.resize((900, 900))
                im.save(dest_jpg)
                os.remove(dest_png)
    print("*****Image sucessfully convert into jpg*****")

    for images in os.listdir(folder_dir2):
        if (images.endswith(".HEIC")):
            # print(images)
            origin = folder_dir2 + images
            c = images.split(".")[0]
            c_png = c + ".png"
            dest_png = dest_dir + c_png
            c_jpg = c + ".jpg"
            dest_jpg = dest_dir + c_jpg
            if (not os.path.exists(dest_jpg)):
                # heif_file = pillow_heif.read_heif(origin)
                # image = Image.frombytes(
                # heif_file.mode, heif_file.size, heif_file.data,"raw")
                image = Image.open(origin)
                # image.save(dest_png, format("png"))
                # image.resize((1024, 1024))
                image.save(dest_png)
                im = Image.open(dest_png)
                im.resize((900, 900))
                im.save(dest_jpg)
                os.remove(dest_png)


t = threading.Thread(target=img_conversion)
t.start()
t.join()
