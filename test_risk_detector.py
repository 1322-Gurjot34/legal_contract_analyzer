from utils.extract_text import extract_text_from_pdf
from utils.risk_detector import detect_risks

pdf_path = "contracts/ABC_Contract/sample.pdf"

text = extract_text_from_pdf(pdf_path)

risks = detect_risks(text)

print("\n--- DETECTED RISKS ---\n")

for risk in risks:
    print(f"Risk Type: {risk['Risk Type']}")

    for sentence in risk["Sentences"]:
        print("-", sentence)

    print()