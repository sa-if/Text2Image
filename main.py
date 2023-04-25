from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_image(text, font_path, font_size, width, height, bg_color=(255, 255, 255), text_color=(0, 0, 0), line_width=0, line_color=(0, 0, 0), blur_radius=0, image_filter=None):
    # Create a blank image with the given width and height
    image = Image.new('RGB', (width, height), color=bg_color)
    
    # Create a drawing object
    draw = ImageDraw.Draw(image)
    
    # Load the font
    font = ImageFont.truetype(font_path, font_size)
    
    # Calculate the size of the text
    text_width, text_height = draw.textsize(text, font=font)
    
    # Calculate the position of the text
    x = (width - text_width) / 2
    y = (height - text_height) / 2
    
    # Draw the text
    if line_width > 0:
        draw.text((x, y), text, font=font, fill=bg_color)
        for i in range(1, line_width+1):
            draw.text((x-i, y), text, font=font, fill=line_color)
            draw.text((x+i, y), text, font=font, fill=line_color)
            draw.text((x, y-i), text, font=font, fill=line_color)
            draw.text((x, y+i), text, font=font, fill=line_color)
    else:
        draw.text((x, y), text, font=font, fill=text_color)
    
    # Apply image filter
    if image_filter is not None:
        image = image.filter(image_filter)
    
    # Apply image blur
    if blur_radius > 0:
        image = image.filter(ImageFilter.GaussianBlur(radius=blur_radius))
    
    return image

# Example usage
text = "Hello, World!"
font_path = "/path/to/font.ttf"
font_size = 40
width = 400
height = 200
bg_color = (255, 255, 255)
text_color = (0, 0, 0)
line_width = 2
line_color = (255, 0, 0)
blur_radius = 5
image_filter = None

image = create_image(text, font_path, font_size, width, height, bg_color, text_color, line_width, line_color, blur_radius, image_filter)
image.save("output.png")
