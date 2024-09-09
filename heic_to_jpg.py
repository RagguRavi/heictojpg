import os
import numpy as np
from PIL import Image
import pillow_heif
import threading
from pillow_heif import register_heif_opener
import piexif

source_dir = "D:\\test\\Photos_1\\"
dest_dir = "D:\\test\\Photos\\"

register_heif_opener()


def start():
    heic_files = [
        file for file in os.listdir(source_dir) if file.lower().endswith(".heic")
    ]

    print(type(heic_files))
    print(len(heic_files))
    splits = np.array_split(heic_files, 16)
    for f in splits:
        t = threading.Thread(target=img_conversion, args=(f,))
        t.start()
    print("File conversion completed.")


def img_conversion(heic_files):
    for heic_file in heic_files:
        if heic_file.lower().endswith(".heic"):
            # print(images)
            origin = source_dir + heic_file
            c = heic_file.split(".")[0]
            c_png = c + ".png"
            dest_png = dest_dir + c_png
            c_jpg = c + ".jpg"
            dest_jpg = dest_dir + c_jpg
            if not os.path.exists(dest_jpg):
                image = Image.open(origin)
                image.save(dest_png)
                exif_data_image = image.getexif()
                exif_data_image[37520] = "Ravi Prajapati"
                exif_data_image[37521] = "Ravi Prajapati"
                exif_data_image[37522] = "Ravi Prajapati"
                im = Image.open(dest_png)
                im.resize((im.width, im.height))
                im.save(dest_jpg, exif = exif_data_image)
                os.remove(dest_png)
                add_author_to_image(dest_jpg, "Ravi Prajapati")


def add_author_to_image(image_path, author_name):
    """Adds the specified author to the Exif metadata of the given image.

Args:
    image_path (str): The path to the image file.
    author_name (str): The author's name to be added.
"""

try:
    # Load the image's Exif data
    exif_dict = piexif.load(image_path)

    # Set the author tag (tag number 37520)
    exif_dict['0th'][piexif.Tag.Artist] = author_name.encode('utf-8')

    # Save the modified Exif data back to the image
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, image_path)
except Exception as e:
    print(f"Error adding author information: {e}")
        
start()
