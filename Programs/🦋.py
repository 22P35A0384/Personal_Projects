from PIL import Image, ImageDraw

# create new image
img = Image.new('RGB', (400, 400), 'white')
draw = ImageDraw.Draw(img)

# draw left wing
draw.polygon([(50, 150), (150, 50), (250, 150)], fill='pink')

# draw right wing
draw.polygon([(250, 150), (350, 50), (450, 150)], fill='purple')

# draw body
draw.line([(200, 150), (200, 300)], width=10, fill='black')

# save image
img.save('butterfly.png')

# show image
img.show()
