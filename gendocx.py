import os
from docxtpl import DocxTemplate

def automate_word_template(template_path, output_path):
    if not os.path.exists(template_path):
        print(f"Error: Template file '{template_path}' not found.")
        return

    # Load the template file
    print("Loading Word template...")
    doc = DocxTemplate(template_path)

    # Automatically scan the document to find all tags matching {{ variable }}
    tags = doc.get_undeclared_template_variables()

    if not tags:
        print("No placeholders found in the document.")
        return

    # Prompt the user for input dynamically based on the tags found
    print("\nPlease fill out the following template fields:")
    context = {}
    for tag in sorted(tags):
        # Format the tag name into a human-readable prompt
        prompt_name = tag.replace('_', ' ').title()
        user_input = input(f"Enter {prompt_name}: ")
        context[tag] = user_input

    # Render the data into the document formatting structure
    doc.render(context)

    # Save the generated document
    doc.save(output_path)
    print(f"\nSuccess! Document saved as '{output_path}'")

if __name__ == "__main__":
    # Configure your file paths here
    TEMPLATE = "template.docx"
    OUTPUT = "filled_document.docx"

    automate_word_template(TEMPLATE, OUTPUT)

