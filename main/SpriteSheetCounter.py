'''
Created on 22.03.2018

@author: raLa
'''
from PIL import Image, ImageFont, ImageDraw
#Read image
im = Image.open( 'items.png' )
width, height = im.size

txt = Image.new('RGBA', im.size, (255,255,255,0))
fnt = ImageFont.truetype("arial.ttf", 16)
# get a drawing context
d = ImageDraw.Draw(txt)
# draw text, half opacity
row = 0;
column = 0;
counter = 1;
for x in range(1, int(width/32)+1):
    for y in range(0, int(height/32)):
        d.text((row,column), str(counter), font=fnt, fill=(255,0,0,255))
        row += 32
        counter += 1
        if(row == width):
            row = 0
            column += 32
# draw text, full opacity
out = Image.alpha_composite(im, txt)
out.show()



