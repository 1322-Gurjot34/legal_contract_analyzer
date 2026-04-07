from utils.extract_text import extract_text_from_pdf
from utils.summarize_contract import summarize_contract
from utils.extract_key_info import extract_key_info
from utils.risk_detector import detect_risks

pdf_path = "contracts/ABC_Contract/sample.pdf"

# Step 1: Extract text
text = extract_text_from_pdf(pdf_path)

# Step 2: Generate summary
summary = summarize_contract(text)

# Step 3: Extract key details
info = extract_key_info(text)

# Step 4: Detect risks
risks = detect_risks(text)

# Output
print("\n========== CONTRACT ANALYSIS ==========\n")

print("SUMMARY:\n")
print(summary)

print("\n========== KEY INFORMATION ==========\n")

for key, value in info.items():
    print(f"{key}:")
    
    if isinstance(value, list):
        for item in value[:3]:
            print("-", item)

    print()

print("\n========== RISKS DETECTED ==========\n")

for risk in risks:
    print(f"Risk Type: {risk['Risk Type']}")

    for sentence in risk["Sentences"][:2]:
        print("-", sentence[:150])

    print()