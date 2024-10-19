from PIL import Image, ImageEnhance
import os
import sys

def apply_warm_filter(img):
    # Enhance the color to give a warm effect
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(1.5)
    return img

def resize_and_compress_image(image_path):
    # Open the image
    with Image.open(image_path) as img:
        # Calculate the new height to maintain the aspect ratio
        width, height = img.size
        new_width = 1200
        new_height = int((new_width / width) * height)
        
        # Resize the image
        resized_img = img.resize((new_width, new_height))
        
        # Apply warm filter
        warm_img = apply_warm_filter(resized_img)
        
        base, ext = os.path.splitext(image_path)
        new_file_path = f"{base}_resized{ext}"
        
        # Save the resized and compressed image
        warm_img.save(new_file_path, optimize=True, quality=85)
        print(f"Image saved to {new_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python website_image_resizer.py <path_to_image>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    resize_and_compress_image(image_path)