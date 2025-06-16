# 📸 The Shrink Ray: Image Compressor

**Effortlessly compress your images down to 1MB or less!**

Are large image files slowing down your website, bogging down your emails, or taking up too much space? The Shrink Ray is a simple Python script designed to automatically reduce the file size of your images to a target of approximately 1MB, ensuring optimal quality for its new, compact size.

---

## ✨ Features

* **Target Compression:** Aims to compress images to under 1MB.
* **Automatic Quality Adjustment:** Intelligently reduces JPEG quality until the target size is met (or until a minimum quality is reached).
* **Simple to Use:** Just run the script, and let the Shrink Ray do its work!
* **Versatile Input:** Accepts various image formats (PNG, JPG, etc.) and outputs a JPEG.

---

## 🚀 How to Use

### Prerequisites

Make sure you have Python installed (Python 3.6+ recommended).
You'll also need the Pillow library. Install it using pip:

```bash
pip install Pillow
````

### Running the Script

1.  **Save the Script:** Save the provided Python code as `shrink_ray.py` (or any other `.py` filename you prefer) in your project directory.

    ```python
    # shrink_ray.py
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
    ```

2.  **Place Your Image:** Put the image you want to compress (e.g., `my-large-photo.png`) in the same directory as `shrink_ray.py`.

3.  **Modify the Script (Optional but Recommended):** Open `shrink_ray.py` and change the `input-image.png` and `output-image.jpg` values in the `if __name__ == '__main__':` block to match your desired input and output filenames.

    ```python
    if __name__ == '__main__':
        compress_image_to_1mb('my-large-photo.png', 'compressed-photo.jpg')
    ```

4.  **Run from Terminal:** Navigate to your script's directory in your terminal or command prompt and run:

    ```bash
    python shrink_ray.py
    ```

    The compressed image (`compressed-photo.jpg` in the example above) will be saved in the same directory\!

-----

## 💡 How it Works

The script uses the powerful `Pillow` library to:

1.  Open your input image.
2.  Continuously attempt to save the image as a JPEG, starting with a high quality (95).
3.  Check the file size. If it's already under 1MB, or if the quality drops too low (to prevent excessive quality loss), it stops.
4.  Otherwise, it reduces the quality by 5 and tries again, repeating the process until the target size is met.
5.  Finally, it saves the optimized image to your specified output file.

-----

## 🤝 Contributing

Got ideas to make the Shrink Ray even better? Feel free to fork this repository, make your changes, and submit a pull request\!

-----
