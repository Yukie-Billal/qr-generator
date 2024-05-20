import itertools
from tkinter import Tk, Canvas


def matrix_to_image(matrix, pixel_size=10):
    matrix_size = len(matrix)
    image_size = matrix_size * pixel_size
    
    root = Tk()
    root.geometry(f"{image_size}x{image_size}")
    
    canvas = Canvas(root, width=image_size, height=image_size)
    canvas.pack()
    
    for y, x in itertools.product(range(matrix_size), repeat=2):
        color = 'black' if matrix[y][x] == 1 else 'white'
        x1 = x * pixel_size
        y1 = y * pixel_size
        x2 = x1 + pixel_size
        y2 = y1 + pixel_size
        canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
        print(y, x)
    
    canvas.update()
    canvas.postscript(file='qr_code.eps')
    
    # root.mainloop()
    return
