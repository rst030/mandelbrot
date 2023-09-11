# python3 -m pip install --upgrade Pillow if doesnt work
# Вечная Слава Андрею Владимировичу Шулаеву.
from PIL import Image
def mandel_color(c):
    divLim = 1
    z = 0+0j
    for i in range(128):
        z = z*z+c
        if (z.real > divLim) | (z.imag > divLim) :
            return 255
    if abs(z) > divLim:
        return 255
    else:
        return (255*int(abs(z)/divLim))

def point_to_screen(x,y,c,box_size):
    x_plane = c.real - box_size/2 + x*(box_size)/width
    y_plane = c.imag - box_size/2 + y*(box_size)/height
    return x_plane+y_plane*1j

c = (-2.718281828459045/3.14159265358979323+0.1349690 - 0.191051j) # adjust this point to stay at the border.

box_size = 8 # initial size of the viewport
width = 320
height = 320
out = []

zooms = range(36)
for zoom_factor in zooms:
    box_size = box_size/1.2
    tmp = Image.new("RGB", (width, height), 255)
    for x in range(width):
        for y in range(height):
            z = point_to_screen(x,y,c,box_size)
            col = mandel_color(z)
            tmp.putpixel((x,y),(col,col,col))
    tmp.show()
    out.append(tmp)

tmp.save("out.gif", save_all=True, append_images=out, duration=100, loop=0)
print('out.gif')