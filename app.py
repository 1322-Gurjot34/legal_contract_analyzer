import os
import streamlit as st

from utils.extract_text import extract_text_from_pdf
from utils.summarize_contract import summarize_contract
from utils.extract_key_info import extract_key_info
from utils.risk_detector import detect_risks
from utils.contract_score import calculate_contract_score
from utils.export_pdf_report import export_pdf_report
from utils.contract_type import detect_contract_type
from utils.clause_extractor import extract_clauses
from utils.search_keyword import search_keyword_in_contract
from utils.upload_history import save_upload_history, get_upload_history

st.set_page_config(page_title="Legal Contract Analyzer", layout="wide")

st.title("Legal Contract Analyzer")
st.caption("AI-powered contract summary, key information extraction, risk detection, and report generation.")

st.sidebar.title("Navigation")
st.sidebar.write("1. Upload PDF")
st.sidebar.write("2. Contract Type")
st.sidebar.write("3. Summary")
st.sidebar.write("4. Key Information")
st.sidebar.write("5. Clauses")
st.sidebar.write("6. Risk Score")
st.sidebar.write("7. Risks")
st.sidebar.write("8. Download Report")

history = get_upload_history()

st.sidebar.header("Upload History")

if history:
    for item in history[-10:]:
        st.sidebar.write("-", item)
else:
    st.sidebar.write("No uploads yet.")

uploaded_file = st.file_uploader("Upload Contract PDF", type=["pdf"])

if uploaded_file is not None:
    save_path = "temp.pdf"

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    save_upload_history(uploaded_file.name)

    text = extract_text_from_pdf(save_path)

    contract_type = detect_contract_type(text)
    summary = summarize_contract(text)
    info = extract_key_info(text)
    clauses = extract_clauses(text)
    risks = detect_risks(text)
    score, level = calculate_contract_score(risks)

    keyword = st.text_input("Search Keyword in Contract")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Summary",
        "Key Information",
        "Clauses",
        "Risk Score",
        "Risks",
        "Full Text"
    ])

    with tab1:
        st.header("Contract Type")
        st.info(contract_type)

        st.header("Contract Summary")

        if isinstance(summary, list):
            for point in summary:
                st.write("-", point)
        else:
            st.write(summary)

        if keyword:
            results = search_keyword_in_contract(text, keyword)

            st.header("Keyword Search Results")

            if results:
                for result in results[:5]:
                    st.write("-", result[:200])
            else:
                st.warning("No matching sentences found.")

    with tab2:
        st.header("Important Contract Information")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Dates Found")
            for date in info.get("Dates Found", [])[:5]:
                st.write("-", date)

            st.subheader("Amounts Found")
            for amount in info.get("Amounts Found", [])[:5]:
                st.write("-", amount)

        with col2:
            st.subheader("Penalty Clauses")
            for penalty in info.get("Penalty Clauses", [])[:3]:
                st.write("-", penalty[:150])

            st.subheader("Renewal Clauses")
            for renewal in info.get("Renewal Clauses", [])[:3]:
                st.write("-", renewal[:150])

    with tab3:
        st.header("Important Clauses")

        for clause_type, clause_list in clauses.items():
            st.subheader(clause_type)

            if clause_list:
                for clause in clause_list[:2]:
                    st.write("-", clause[:200])
            else:
                st.write("No clause found.")

    with tab4:
        st.header("Overall Contract Score")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Risk Score", f"{score}/100")

        with col2:
            st.metric("Risk Level", level)

        with col3:
            st.metric("Total Risks Found", len(risks))

        if level == "Low Risk":
            st.success(f"Score: {score}/100 - {level}")
        elif level == "Medium Risk":
            st.warning(f"Score: {score}/100 - {level}")
        else:
            st.error(f"Score: {score}/100 - {level}")

    with tab5:
        st.header("Detected Risks")

        if risks:
            for risk in risks:
                st.write(f"### {risk['Risk Type']}")

                for sentence in risk["Sentences"][:2]:
                    st.write("-", sentence[:150])
        else:
            st.success("No major risks found.")

    with tab6:
      st.header("Full Extracted Contract Text")
      st.write(text[:5000])

    report_file = export_pdf_report(
     contract_type,
     summary,
     info,
     risks,
     score,
     level
)

    with open(report_file, "rb") as file:
     st.download_button(
        label="Download PDF Report",
        data=file,
        file_name="contract_report.pdf",
        mime="application/pdf"
    )