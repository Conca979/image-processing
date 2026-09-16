import numpy as np
from PIL import Image

def process_transparency(img: Image.Image, make_transparent: bool = True) -> Image.Image:
    """
    Process image transparency. 
    If make_transparent is True, near-white and light-grey background pixels 
    are made fully transparent.
    """
    if not make_transparent:
        return img
        
    data = np.array(img)
    # Replace near-white and light-grey background pixels with full transparency
    r, g, b, a = data.T
    white_areas = (r > 200) & (g > 200) & (b > 200)
    data[..., 3][white_areas.T] = 0
    return Image.fromarray(data)

def run(input_path: str, output_path: str, no_transparent: bool = False):
    """
    Execute the transparency tool.
    """
    from image_processing.core.io import load_image, save_image
    
    # Load
    img = load_image(input_path, mode="RGBA")
    
    # Process
    img = process_transparency(img, make_transparent=not no_transparent)
    
    # Save
    save_image(img, output_path)
    print(f"Successfully processed {input_path} and saved to {output_path}")
