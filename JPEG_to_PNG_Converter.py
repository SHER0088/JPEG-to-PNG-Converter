import sys
import os
from PIL import Image

Image_Folder = sys.argv[1]
Output_Folder = sys.argv[2]

if not os.path.exists(Output_Folder):
    os.makedirs(Output_Folder)

for filename in os.listdir(Image_Folder):
    img = Image.open(f"{Image_Folder}{filename}")
    clean_name = os.path.splitext(filename)[0]
    img.save(f"{Output_Folder}{clean_name}.png", "png")

print("All Done!!")