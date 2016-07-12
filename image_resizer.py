from PIL import Image, ImageDraw, ImageFont, ImageEnhance


WIDTH = 500
HEIGHT = 500
IMAGE = 'mj.jpg'
TEXT = 'SoftGroupPython'
OPACITY = 0.7


def resize_image(image=IMAGE, width=WIDTH, height=HEIGHT):
    img = Image.open(image)
    img = img.resize((width, height))       
    img.save('resized_' + image)


def add_watermark(image, text=TEXT, opacity=OPACITY):
    img = Image.open(image)
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    watermark = Image.new('RGBA', img.size, (0, 0, 0, 0))
    waterdraw = ImageDraw.Draw(watermark, 'RGBA')
    waterdraw.text((15, 15), text)
    alpha = watermark.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    watermark.putalpha(alpha)
    Image.composite(watermark, img, watermark).save('watermarked_' + image,
                                                    'JPEG')

if __name__ == '__main__':
    resize_image()
    image = 'resized_' + IMAGE
    add_watermark(image)