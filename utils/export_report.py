def export_report(summary, info, risks, score, level):
    report = "CONTRACT ANALYSIS REPORT\n"
    report += "=" * 40 + "\n\n"

    report += "SUMMARY:\n"
    report += summary + "\n\n"

    report += "KEY INFORMATION:\n"
    for key, value in info.items():
        report += f"{key}: {value}\n"

    report += "\nRISKS:\n"
    if risks:
        for risk in risks:
            report += f"- {risk['Risk Type']}\n"
    else:
        report += "No major risks detected.\n"

    report += f"\nFINAL SCORE: {score}/100\n"
    report += f"RISK LEVEL: {level}\n"

    with open("contract_report.txt", "w", encoding="utf-8") as file:
        file.write(report)

    return "contract_report.txt"