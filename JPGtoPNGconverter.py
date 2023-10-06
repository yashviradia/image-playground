import sys
import os
from PIL import Image 

# grab first and second argument; eg: python JPGtoPNGconverter.py Pokedex/ new/
commandline_arguments = sys.argv
pokedex_directory = commandline_arguments[1]
new_directory = commandline_arguments[2]

# check new/ exists, if not create
parent_dir = "./"
path = os.path.join(parent_dir, new_directory)

os.mkdir(path)

print(f'Directory {new_directory} created.')

# loop through pokedex, convert images to png, save it to 'new' folder
for filename in os.listdir(f'./{pokedex_directory}'):
    if filename.endswith(".jpg"):
        im = Image.open(os.path.join(f"./{pokedex_directory}", filename))
        prefix = filename.split(".jpg")[0]
        name = f'{prefix}' + '.png'
        # rgb_im = im.convert("RGB")
        # rgb_im.save(name)
        im.save(f'./{new_directory}{name}', 'png')
        print(os.path.join(f'./{new_directory}', name))
    else: 
        continue