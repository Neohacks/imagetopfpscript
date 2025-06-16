from PIL import Image
import io
import os

def compress_image_to_1mb(input_filename, output_filename):
    print(f"Running script in directory: {os.getcwd()}")
    print(f"Files available: {os.listdir()}")
    input_path = os.path.join(os.getcwd(), input_filename)
    output_path = os.path.join(os.getcwd(), output_filename)
    try:
        img = Image.open(input_path)
    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found in {os.getcwd()}")
        return
    quality = 95
    while True:
        buffer = io.BytesIO()
        img.save(buffer, format='JPEG', quality=quality)
        size = buffer.tell()
        if size <= 1_000_000 or quality <= 10:
            break
        quality -= 5
    with open(output_path, 'wb') as f:
        f.write(buffer.getvalue())
    print(f'Compressed image saved as {output_filename} with quality {quality} and size {size} bytes')

if __name__ == '__main__':
    compress_image_to_1mb('input-image.png', 'output-image.jpg')
