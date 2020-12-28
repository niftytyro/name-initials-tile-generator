from PIL import Image, ImageDraw, ImageFont

def generate_tile(initials, bgColor=(15,15,15), fgColor='white'):
    canvas_w, canvas_h = 400, 400
    poppinsFont = ImageFont.truetype("/home/udasitharani/Downloads/ttf/Poppins-Medium.ttf", 200)
    
    canvas = Image.new('RGBA', (canvas_w, canvas_h), color=bgColor)
    draw = ImageDraw.Draw(canvas)
    
    text_w, text_h = draw.textsize(initials, font=poppinsFont)
    draw.text(((canvas_w-text_w)/2, (canvas_h-text_h)/3), initials, fill=fgColor, font=poppinsFont)

    return canvas

def generate_initials_from_string(text):
    return "".join([initial.capitalize()[0] for initial in text.split(" ") ])

initials = generate_initials_from_string(input("Enter you name:\n"))
print(initials)

canvas = generate_tile(initials, bgColor=(250,250,250), fgColor='black')
canvas.show()
