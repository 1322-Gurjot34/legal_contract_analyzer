from fpdf import FPDF

def clean_text(text):
    return str(text).replace("’", "'") \
                    .replace("‘", "'") \
                    .replace("“", '"') \
                    .replace("”", '"') \
                    .replace("–", "-") \
                    .replace("—", "-") \
                    .replace("•", "-") \
                    .encode("latin-1", "ignore") \
                    .decode("latin-1")

def export_pdf_report(contract_type, summary, info, risks, score, level):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, clean_text("Legal Contract Analysis Report"), ln=True, align="C")

    pdf.ln(10)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, clean_text(f"Contract Type: {contract_type}"), ln=True)

    pdf.ln(5)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, clean_text("Summary"), ln=True)

    pdf.set_font("Arial", size=11)

    if isinstance(summary, list):
        for point in summary:
            pdf.multi_cell(0, 8, clean_text(f"- {point}"))
    else:
        pdf.multi_cell(0, 8, clean_text(summary))

    pdf.ln(5)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, clean_text("Key Information"), ln=True)

    pdf.set_font("Arial", size=11)

    for key, value in info.items():
        pdf.multi_cell(0, 8, clean_text(f"{key}: {value}"))

    pdf.ln(5)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, clean_text("Risk Analysis"), ln=True)

    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 8, clean_text(f"Risk Score: {score}/100"))
    pdf.multi_cell(0, 8, clean_text(f"Risk Level: {level}"))

    pdf.ln(5)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, clean_text("Detected Risks"), ln=True)

    pdf.set_font("Arial", size=11)

    if risks:
        for risk in risks:
            pdf.multi_cell(0, 8, clean_text(f"Risk Type: {risk['Risk Type']}"))

            for sentence in risk["Sentences"][:2]:
                pdf.multi_cell(0, 8, clean_text(f"- {sentence}"))
    else:
        pdf.multi_cell(0, 8, clean_text("No major risks found."))

    output_path = "contract_report.pdf"
    pdf.output(output_path)

    return output_path

