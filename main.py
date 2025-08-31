#REMOVE BACKGROUND USING PYTHON 
# By- [Rafe Khan]
###
from rembg import remove
from PIL import Image

input_path = 'input.jpg'
output_path = 'output.png'

src = Image.open(input_path)
dst = remove(src)  # background removed with transparency
dst.save(output_path)