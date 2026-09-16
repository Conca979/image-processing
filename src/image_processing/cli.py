import argparse
from image_processing.fields.image_processing.tools import transparency

def main():
    parser = argparse.ArgumentParser(description="Vision Toolkit - General Image Processing and Computer Vision Tool")
    subparsers = parser.add_subparsers(dest="field", help="The field of processing (e.g., image_processing, computer_vision)")
    subparsers.required = True

    # --- Field: image_processing ---
    ip_parser = subparsers.add_parser("image_processing", help="General image processing tools")
    ip_subparsers = ip_parser.add_subparsers(dest="tool_name", help="Specific tool to use")
    ip_subparsers.required = True

    # Tool: transparency
    transparency_parser = ip_subparsers.add_parser("transparency", help="Convert images and handle background transparency")
    transparency_parser.add_argument("input", help="Path to the input image")
    transparency_parser.add_argument("-o", "--output", help="Path to the output image", required=True)
    transparency_parser.add_argument("--no-transparent", action="store_true", help="Do not make white background transparent")
    
    # Example placeholder for future field: computer_vision
    cv_parser = subparsers.add_parser("computer_vision", help="Computer vision tools (Placeholder)")
    cv_subparsers = cv_parser.add_subparsers(dest="tool_name", help="Specific tool to use")
    
    args = parser.parse_args()
    
    if args.field == "image_processing":
        if args.tool_name == "transparency":
            transparency.run(args.input, args.output, args.no_transparent)
    elif args.field == "computer_vision":
        print("Computer vision tools are not yet implemented.")

if __name__ == "__main__":
    main()
