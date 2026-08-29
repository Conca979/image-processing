# Image Transparent (PNG to ICO Converter)

A simple Python tool to convert PNG images to ICO format. By default, it automatically makes near-white and light-grey backgrounds transparent.

## Requirements

- Python >= 3.10
- Pillow
- NumPy

## Usage

```bash
python main.py <path_to_input_png> [-o <path_to_output_ico>] [--no-transparent]
```

### Examples

Convert a PNG to an ICO (with automatic background transparency):
```bash
python main.py input.png -o output.ico
```

Convert a PNG to an ICO without modifying transparency (keep original background):
```bash
python main.py input.png -o output.ico --no-transparent
```
