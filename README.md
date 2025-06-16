📸 The Shrink Ray: Image Compressor
Effortlessly compress your images down to 1MB or less, both through a conceptual web demo and a powerful Python script!

The Shrink Ray is a project designed to tackle the common problem of oversized image files. Whether you're looking to optimize images for web performance, email attachments, or simply save storage space, this tool offers a smart solution. It combines a robust Python script for actual image compression with a stylish web application for demonstrating its core concept.

✨ Features
Intuitive Web Interface: A modern, responsive, and dark-themed web UI that allows you to upload images and see a conceptual demonstration of the compression process.

Smart Compression Logic: The core Python script intelligently adjusts JPEG quality to meet a target file size of approximately 1MB, or until a minimum quality threshold is met, preserving visual fidelity as much as possible.

Backend Ready Design: The web application is structured to seamlessly integrate with a backend server where the actual Python compression script can run, providing a full-stack solution.

Cross-Platform Ready: The underlying Python script is compatible with various operating systems, allowing you to compress images efficiently on your local machine.

Dynamic & Animated UI: Experience engaging background animations, gradient text effects, and interactive elements consistent with the Neohacks aesthetic.

🚀 Web Application (Conceptual Demo)
This web application serves as an interactive demo to showcase the workflow and capabilities of The Shrink Ray. Since direct heavy-duty image processing isn't feasible client-side in the browser with the Python script, the compression outcome is simulated.

How to Use the Web Demo:

Visit the App: Navigate to the deployed web application (e.g., your GitHub Pages URL for this project).

Upload an Image: Click the "Upload Your Image" input and select any image file (PNG, JPG, etc.) from your device.

Initiate Compression: Once your image appears in the preview, click the "Shrink Image!" button.

Observe & Download: The app will simulate the compression process and display a "new size." You can then click "Download 'Compressed'" to conceptually download the processed image (it will be your original image's preview, but the size displayed will be simulated).

💡 Python Script (Full Functionality)
For actual, real-world image compression, you'll use the Python script directly on your computer. This script leverages the powerful Pillow library to perform the resizing and quality adjustments.

Prerequisites:

Python: Ensure you have Python 3.6 or newer installed on your system.

Pillow Library: Install Pillow using pip:

pip install Pillow

How to Use the Python Script:

Get the Script: Download the shrink_ray.py file from this repository and save it to your local machine.

Place Your Image: Put the image you want to compress (e.g., my_large_photo.png) in the same directory as shrink_ray.py.

Modify the Script (Optional but Recommended): Open shrink_ray.py in a text editor. Locate the if __name__ == '__main__': block and change 'input-image.png' to the filename of your image, and 'output-image.jpg' to your desired output filename.

if __name__ == '__main__':
    # Change 'your_input_image.png' to your actual image file
    # Change 'your_output_image.jpg' to your desired output filename
    compress_image_to_1mb('your_input_image.png', 'your_output_image.jpg')

Run from Terminal: Open your terminal or command prompt, navigate to the directory where you saved shrink_ray.py and your image, and run the script:

python shrink_ray.py

The compressed image will be saved in the same directory!

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
        # Note: For optimal compression to a target size, JPEG is usually best.
        # If your input is PNG, it will be converted to JPEG.
        img.save(buffer, format='JPEG', quality=quality)
        size = buffer.tell()
        if size <= 1_000_000 or quality <= 10:
            break
        quality -= 5
    with open(output_path, 'wb') as f:
        f.write(buffer.getvalue())
    print(f'Compressed image saved as {output_filename} with quality {quality} and size {size} bytes')

if __name__ == '__main__':
    # IMPORTANT: Make sure 'input-image.png' exists in the same directory
    # or provide the correct path to your input image.
    compress_image_to_1mb('input-image.png', 'output-image.jpg')

🤝 Contributing
Got ideas to make the Shrink Ray even better? Found a bug? We welcome contributions! Feel free to fork this repository, make your changes, and submit a pull request.

📝 License
This project is open-source and available under the MIT License.

🚀 Credits
This project was a collaborative effort between Neohacks and Google's Gemini.
