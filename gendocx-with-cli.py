import argparse
import os
import sys
from docxtpl import DocxTemplate

def parse_kv(arg_string):
    """Helper function to split key=value arguments."""
    if '=' not in arg_string:
        raise argparse.ArgumentTypeError(f"Invalid key=value format: '{arg_string}'. Must be key=value.")
    key, val = arg_string.split('=', 1)
    return key.strip(), val.strip()

def main():
    parser = argparse.ArgumentParser(
        description="Automate MS Word .docx template generation via command-line."
    )
    
    # Core file flags - now with built-in DEFAULTS
    parser.add_argument(
        "-t", "--template", 
        default="template.docx",  # <--- Default fallback
        help="Path to input template. Defaults to 'template.docx'"
    )
    parser.add_argument(
        "-o", "--output", 
        default="output.docx",    # <--- Default fallback
        help="Path to save output. Defaults to 'output.docx'"
    )
    
    # Custom tags flag
    parser.add_argument(
        "tags", 
        nargs="*", 
        type=parse_kv, 
        help="Space-separated variables to replace: key=value"
    )

    args = parser.parse_args()

    # Verify the template exists (whether it's the default or a custom file)
    if not os.path.exists(args.template):
        print(f"Error: The template file '{args.template}' does not exist.", file=sys.stderr)
        sys.exit(1)

    context = dict(args.tags)

    try:
        print(f"Loading template: {args.template}")
        doc = DocxTemplate(args.template)
        
        print(f"Injecting values: {context}")
        doc.render(context)
        
        doc.save(args.output)
        print(f"Success! Document saved successfully to: {args.output}")
        
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
