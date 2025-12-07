from PIL import Image
from collections import Counter

def get_dominant_colors(image_path, num_colors=5):
    try:
        img = Image.open(image_path)
        img = img.resize((150, 150))  # Resize for speed
        img = img.convert('RGB')
        
        # Get pixels
        pixels = list(img.getdata())
        
        # Count frequency
        counts = Counter(pixels)
        
        # Get most common
        common = counts.most_common(num_colors)
        
        print(f"Dominant colors for {image_path}:")
        for color, count in common:
            print(f"RGB: {color}, Hex: #{color[0]:02x}{color[1]:02x}{color[2]:02x}")
            
    except Exception as e:
        print(f"Error: {e}")

image_path = "/Users/sparshgupta/.gemini/antigravity/brain/de9bc5b3-d23c-4609-8c26-964414e06a90/uploaded_image_1765120806919.png"
get_dominant_colors(image_path, num_colors=10)
