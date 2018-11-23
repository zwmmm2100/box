from PIL import Image
import glob, os

ss = Image.open('2.jpg').convert('RGBA')
bb = Image.open('11.jpg').convert('RGBA')

dd = Image.alpha_composite(ss,bb)
dd.save('321.png')