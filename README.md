# Image Transparent (Universal Image Converter)

A simple Python tool to convert images between different formats (e.g., PNG to JPG, JPG to PNG). By default, it automatically makes near-white and light-grey backgrounds transparent.

If the output format does not support transparency (like JPEG), the script automatically flattens the image onto a white background to prevent errors.

## Supported Formats
See the `format_support_checklist.md` file for a full list of supported formats. Currently implemented:
- **PNG**
- **JPEG / JPG**
- **ICO**

## Requirements

- Python >= 3.10
- Pillow
- NumPy

## Usage

```bash
python main.py <path_to_input_image> -o <path_to_output_image> [--no-transparent]
```

### Examples

Convert a PNG to a JPG (automatically flattens transparent background to white):
```bash
python main.py input.png -o output.jpg
```

Convert a JPG to a PNG (with automatic background transparency):
```bash
python main.py input.jpg -o output.png
```

Convert an image without modifying transparency (keep original background):
```bash
python main.py input.png -o output.ico --no-transparent
```
