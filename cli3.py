import os
import numpy as np
from PIL import Image
import pillow_heif
import pyheif
import threading
from pillow_heif import register_heif_opener

source_dir = "C:\\Users\\ravir\\OneDrive\\Documents\\Zapya\\Photo\\Test1\\"
dest_dir = "C:\\Users\\ravir\\OneDrive\\Documents\\Zapya\\Photo\\convertedTest\\"

register_heif_opener()


def start():
    # Get all HEIC files in the specified directory
    heic_files = [
        file for file in os.listdir(source_dir) if file.lower().endswith(".heic")
    ]
    print(len(heic_files))
    splited_files = np.array_split(heic_files, 1)
    for files in splited_files:
        print(len(files))
        t = threading.Thread(target=img_conversion, args=(files,))
        t.start()


def img_conversion(files):
    for file in files:
        # print(images)
        heic_file = source_dir + file
        jpg_file = file.split(".")[0] + ".jpg"
        dest_png = dest_dir + jpg_file
        with open(heic_file, "rb") as heic_file:
            heif_file = pyheif.read(heic_file)
            image = Image.frombytes(
                heif_file.mode,
                heif_file.size,
                heif_file.data,
                "raw",
                heif_file.mode,
                heif_file.stride,
            )

        # Save the image as JPG
        with open(jpg_file, "wb") as jpg_file:
            image.save(jpg_file, "JPEG", quality=100)
        print(f"*****Image successfully convert into jpg***** {file}")


start()
