from PIL import Image, ImageDraw, ImageFont
import textwrap

# Load text from input.txt file
with open("input.txt", "r") as f:
    text = f.read()

# Set up font and image size
font_path = r"path_of_font"
font_size = 24
img_width = 1200
img_height = 630

# Create image and draw object
img = Image.new("RGB", (img_width, img_height), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

# Set up font
font = ImageFont.truetype(font_path, font_size)

# Wrap text and calculate text size
wrapper = textwrap.TextWrapper(width=50)
text_lines = wrapper.wrap(text=text)
text_size = draw.textsize("\n".join(text_lines), font=font)

# Calculate starting position for text drawing
text_x = (img_width - text_size[0]) // 2
text_y = (img_height - text_size[1]) // 2

# Draw text on image
for line in text_lines:
    draw.text((text_x, text_y), line, font=font, fill=(0, 0, 0))
    text_y += font_size

# Save image to file
img.save("output.jpg")
