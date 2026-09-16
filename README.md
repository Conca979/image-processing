# Vision Toolkit (Image Processing)

A modular Python tool to perform image processing and computer vision tasks. The project uses a multi-level CLI to easily expand into different fields of computer vision and image processing.

## Available Fields and Tools

### 1. `image_processing`
General image processing utilities.

- **`transparency`**: Converts images between different formats (e.g., PNG to JPG, JPG to PNG). By default, it automatically makes near-white and light-grey backgrounds transparent. If the output format does not support transparency (like JPEG), the script automatically flattens the image onto a white background to prevent errors.

### 2. `computer_vision`
*(Placeholder for future computer vision features like classification, detection, etc.)*

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

You can use the new command structure via `uv run` or directly running `main.py`.

```bash
uv run image-processing <field> <tool_name> [args]
```

Or using python:

```bash
python main.py <field> <tool_name> [args]
```

### Examples

Convert a PNG to a JPG (automatically flattens transparent background to white):
```bash
python main.py image_processing transparency input.png -o output.jpg
```

Convert a JPG to a PNG (with automatic background transparency):
```bash
python main.py image_processing transparency input.jpg -o output.png
```

Convert an image without modifying transparency (keep original background):
```bash
python main.py image_processing transparency input.png -o output.ico --no-transparent
```
