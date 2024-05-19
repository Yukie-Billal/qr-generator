import itertools

def matrix_to_image(matrix, pixel_size=10):
    import itertools
    from PIL import Image

    matrix_size = len(matrix)
    image_size = matrix_size * pixel_size
    image = Image.new('1', (image_size, image_size), 1)  # Create a white image

    for y, x in itertools.product(range(matrix_size), repeat=2):
        color = 0 if matrix[y][x] == 1 else 1  # Black for 1, white for 0
        for dy, dx in itertools.product(range(pixel_size), repeat=2):
            image.putpixel((x * pixel_size + dx, y * pixel_size + dy), color)

    return image