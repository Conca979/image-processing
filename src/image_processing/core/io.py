import sys
from PIL import Image

def load_image(input_path: str, mode: str = "RGBA") -> Image.Image:
    """Load an image and convert it to the specified mode."""
    try:
        return Image.open(input_path).convert(mode)
    except Exception as e:
        print(f"Error loading image '{input_path}': {e}")
        sys.exit(1)

def save_image(img: Image.Image, output_path: str):
    """Save an image, handling format-specific constraints automatically."""
    output_ext = output_path.split('.')[-1].lower()

    if output_ext in ['jpg', 'jpeg']:
        # JPEG doesn't support alpha channel.
        # If the image has an alpha channel, paste it onto a white background.
        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
            background = Image.new("RGB", img.size, (255, 255, 255))
            # Some modes might not split properly, so ensure it's RGBA before splitting
            img_rgba = img.convert("RGBA")
            background.paste(img_rgba, mask=img_rgba.split()[3]) # alpha channel is the mask
            img = background
        else:
            img = img.convert("RGB")

    # If it's an ICO we specify sizes, otherwise let Pillow handle it based on format
    if output_ext == 'ico':
        img.save(output_path, format="ICO", sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)])
    else:
        img.save(output_path)
