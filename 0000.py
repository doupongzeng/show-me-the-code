from PIL import Image, ImageFont, ImageDraw
with Image.open('0000.jpg') as im:
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("arial", 20)
    draw.text((150, 110), "4", font=font,fill=(255,0,0))
    im.save('0000.jpg')
im.show()