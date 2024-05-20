from tkinter import Tk, Canvas
from datetime import datetime

def generate_simple_barcode(data, filename=None, bar_width=2, bar_height=100):
    if not filename:
        filename = f"barcode-{datetime.now().strftime('%d%m%Y')}.eps"

    # Create binary code
    data = "".join(format(ord(i), '08b') for i in data)

    # Calculate canvas size
    width = len(data) * bar_width
    height = bar_height

    # Create a tkinter window
    root = Tk()
    root.geometry(f"{width}x{height}")  # Hide the root window
    
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    
    for i, char in enumerate(data):
        color = 'black' if char == '1' else 'white'
        x1 = i * bar_width
        y1 = 0
        x2 = x1 + bar_width
        y2 = bar_height
        # print(x1, x2, y1, y2)
        canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
    
    # Save the canvas content as an EPS file
    canvas.update()
    canvas.postscript(file=filename)
    # root.destroy()

# Example usage
# For simplicity, assuming '1' is a black bar and '0' is a white bar
barcode_data = 'https://www.yukie.site'  # Example binary string
generate_simple_barcode(barcode_data)