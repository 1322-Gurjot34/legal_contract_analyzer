from utils.extract_text import extract_text_from_pdf
from utils.extract_key_info import extract_key_info

pdf_path = "contracts/ABC_Contract/sample.pdf"

text = extract_text_from_pdf(pdf_path)

info = extract_key_info(text)

print("\n--- EXTRACTED CONTRACT INFO ---\n")

for key, value in info.items():
    print(f"{key}:")
    
    if isinstance(value, list):
        for item in value:
            print("-", item)
    else:
        print(value)

    print()