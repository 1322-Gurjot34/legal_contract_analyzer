from utils.extract_text import extract_text_from_pdf
from utils.summarize_contract import summarize_contract

pdf_path = "contracts/ABC_Contract/sample.pdf"


text = extract_text_from_pdf(pdf_path)


summary = summarize_contract(text)

print("\n--- CONTRACT SUMMARY ---\n")
print(summary)