import itertools
from tkinter import Tk, Canvas

def generate_simple_barcode(data, filename='barcode.eps', bar_width=2, bar_height=100):
    # Create a tkinter window
    root = Tk()
    root.withdraw()  # Hide the root window

    # Calculate canvas size
    width = len(data) * bar_width
    height = bar_height
    
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    
    for i, char in enumerate(data):
        color = 'black' if char == '1' else 'white'
        x1 = i * bar_width
        y1 = 0
        x2 = x1 + bar_width
        y2 = bar_height
        canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
    
    # Save the canvas content as an EPS file
    canvas.update()
    canvas.postscript(file=filename)
    root.destroy()