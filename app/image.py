from PIL import Image, ImageDraw, ImageFont

avocado = "avocadoscado"
font_name = "cm-unicode-0.7.0/cmunorm.ttf"

rnt = "/home/kronicmage/repos/api-examples/python/test.jpg"
theorem_statement = (200, 460, 1350, 600)
type_string = (850, 275, 1275, 360)
summation = (500, 775, 950, 1000)
all_of_them = [theorem_statement, type_string, summation]

def crop(image_object, new_boundaries):
    """
    new_boundaries should be a tuple (Int, Int, Int, Int) representing # of
    pixels cut off from the left, top, right, and bottom respectively.
    Saves the cropped file to cropped_file_name, and returns the cropped image object
    """
    # image_object = Image.open(image_file_name)
    cropped_image = image_object.crop(new_boundaries)
    # cropped_image.save(cropped_file_name)
    return cropped_image

def generate_avocado(size_x, size_y):
    avocado_img = Image.new("RGB", (size_x, size_y), (255, 255, 255, 0))
    drawer = ImageDraw.Draw(avocado_img)
    font_size = 1
    font = ImageFont.truetype("cm-unicode-0.7.0/cmunorm.ttf", font_size)

    while (font.getsize(avocado)[0] < size_x and font.getsize(avocado)[1] < size_y):
        font_size += 1
        font = ImageFont.truetype("cm-unicode-0.7.0/cmunorm.ttf", font_size)

    font_size -= 1
    font = ImageFont.truetype("cm-unicode-0.7.0/cmunorm.ttf", font_size)

    indent_x, indent_y = drawer.textsize(avocado, font=font)
    drawer.text(((size_x - indent_x)/2, (size_y - indent_y)/2), avocado, font=font, fill="black")

    # avocado_img.save("avocado.jpg")
    return avocado_img

def place_avocados(image_object, locations):
    # drawer = ImageDraw.Draw(image_object)
    for location in locations:
        x_0 ,y_0, x_1, y_1 = location
        current_avocado = generate_avocado(x_1 - x_0, y_1 - y_0)
        image_object.paste(current_avocado, (x_0, y_0))
    return image_object

def tester(in_file, out_file):
    image_object = Image.open(in_file)
    returned_image = place_avocados(image_object, all_of_them)
    returned_image.save(out_file)

def cropper(in_file, out_file, boundary):
    image_object = Image.open(in_file)
    returned_image = crop(image_object, boundary)
    returned_image.save(out_file)

def separator(image_object, boundaries):
    for_google_ocr = place_avocados(image_object, boundaries)
    for_mathpix = [crop(image_object, boundary) for boundary in boundaries]
    return for_google_ocr, for_mathpix

# tester(rnt, "avocado.jpg")
