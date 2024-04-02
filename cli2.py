import os
import numpy as np
from PIL import Image
import pillow_heif
import threading
from pillow_heif import register_heif_opener

source_dir = "C:\\Users\\ravir\\OneDrive\\Documents\\Zapya\\Photo\\2024_04_02_121914\\"
dest_dir="C:\\Users\\ravir\\OneDrive\\Documents\\Zapya\\Photo\\converted1\\"
folder_dir2="C:\\Users\\ravir\\OneDrive\\Pictures\\Zapya\\2022_12_10_172257\\"

re= register_heif_opener()

def start():
   
    heic_files = [
        file for file in os.listdir(source_dir) if file.lower().endswith(".heic")
    ]

    print(type(heic_files))
    print(len(heic_files))
    splits = np.array_split(heic_files,16)
    for f in splits:
        print(len(f))
        t=threading.Thread(target=img_conversion,args=(f,))
        t.start()



def img_conversion(heic_files):

   for heic_file in heic_files:
    
        if (heic_file.lower().endswith(".heic")):
            # print(images)
            origin = source_dir+heic_file
            c = heic_file.split(".")[0]
            c_png = c+".png"
            dest_png = dest_dir+c_png
            c_jpg = c+".jpg"
            dest_jpg = dest_dir+c_jpg
            if(not os.path.exists(dest_jpg)):
                image=Image.open(origin)
                image.save(dest_png)
                im=Image.open(dest_png)
                im.resize((900,900))
                im.save(dest_jpg)
                os.remove(dest_png)
        print(f"*****Image sucessfully convert into jpg***** {heic_file}")


start()