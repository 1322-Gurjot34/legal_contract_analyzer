import streamlit as st
import os
import json

from utils.extract_text import extract_text_from_pdf
from utils.summarize_contract import summarize_contract
from utils.extract_key_info import extract_key_info
from utils.risk_detector import detect_risks
from utils.contract_score import calculate_contract_score
from utils.export_pdf_report import export_pdf_report
from utils.contract_type import detect_contract_type

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Legal Contract Analyzer", layout="wide")

USER_FILE = "users.json"
HISTORY_FILE = "history.json"

# ---------------- STORAGE ----------------
def load_users():
    if os.path.exists(USER_FILE):
        return json.load(open(USER_FILE))
    return {}

def save_users(data):
    json.dump(data, open(USER_FILE, "w"))

def load_history():
    if os.path.exists(HISTORY_FILE):
        return json.load(open(HISTORY_FILE))
    return {}

def save_history(data):
    json.dump(data, open(HISTORY_FILE, "w"))

# ---------------- SESSION ----------------
if "user" not in st.session_state:
    st.session_state.user = None

# ---------------- LOGIN ----------------
def login_page():
    st.title("🔐 Login / Signup")

    users = load_users()

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login / Signup"):
        if username in users:
            if users[username] == password:
                st.session_state.user = username
                st.success("Logged in successfully")
                st.rerun()
            else:
                st.error("Wrong password")
        else:
            users[username] = password
            save_users(users)
            st.session_state.user = username
            st.success("Account created")
            st.rerun()

# ---------------- SIDEBAR ----------------
def sidebar():
    st.sidebar.title("Navigation")
    st.sidebar.write(f"👤 {st.session_state.user}")

    page = st.sidebar.radio(
        "Go to",
        ["Analyzer", "Compare Contracts", "Feedback"]
    )

    if st.sidebar.button("Logout"):
        st.session_state.user = None
        st.rerun()

    return page

# ---------------- ANALYZER ----------------
def analyzer_page():
    st.title("📄 Contract Analyzer")

    history = load_history()
    user_history = history.get(st.session_state.user, [])

    st.sidebar.subheader("📂 Upload History")
    if user_history:
        for item in user_history[-5:]:
            st.sidebar.write("-", item)
    else:
        st.sidebar.write("No uploads yet")

    uploaded_file = st.file_uploader("Upload Contract PDF", type=["pdf"])

    if uploaded_file:
        path = "temp.pdf"
        with open(path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Save history
        user_history.append(uploaded_file.name)
        history[st.session_state.user] = user_history
        save_history(history)

        text = extract_text_from_pdf(path)

        summary = summarize_contract(text)
        info = extract_key_info(text)
        risks = detect_risks(text)
        score, level = calculate_contract_score(risks)
        contract_type = detect_contract_type(text)

        # -------- SUMMARY --------
        st.subheader("📌 Smart Summary")
        for point in summary:
            st.markdown(f"✔️ {point}")

        # -------- INFO --------
        st.subheader("📊 Key Information")
        st.write(info)

        # -------- SCORE --------
        st.subheader("⚠️ Risk Score")
        st.metric("Score", score)
        st.metric("Level", level)

        # -------- DOWNLOAD (FIXED) --------
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
                label="📥 Download Report",
                data=file,
                file_name="contract_report.pdf",
                mime="application/pdf"
            )

# ---------------- COMPARE ----------------
def compare_page():
    st.title("⚖️ Compare Contracts")

    file1 = st.file_uploader("Upload Contract 1", type=["pdf"], key="c1")
    file2 = st.file_uploader("Upload Contract 2", type=["pdf"], key="c2")

    if file1 and file2:
        with open("c1.pdf", "wb") as f:
            f.write(file1.getbuffer())

        with open("c2.pdf", "wb") as f:
            f.write(file2.getbuffer())

        text1 = extract_text_from_pdf("c1.pdf")
        text2 = extract_text_from_pdf("c2.pdf")

        s1 = summarize_contract(text1)
        s2 = summarize_contract(text2)

        r1 = detect_risks(text1)
        r2 = detect_risks(text2)

        sc1, lv1 = calculate_contract_score(r1)
        sc2, lv2 = calculate_contract_score(r2)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📄 Contract 1")
            st.metric("Score", sc1)
            st.write(lv1)
            for s in s1:
                st.write("-", s[:120])

        with col2:
            st.subheader("📄 Contract 2")
            st.metric("Score", sc2)
            st.write(lv2)
            for s in s2:
                st.write("-", s[:120])

        st.subheader("📊 Final Insight")

        if sc1 > sc2:
            st.success("✅ Contract 1 is safer")
        elif sc2 > sc1:
            st.success("✅ Contract 2 is safer")
        else:
            st.info("⚖️ Both contracts are similar")

# ---------------- FEEDBACK ----------------
def feedback_page():
    st.title("💬 Feedback / Complaint")

    rating = st.slider("Rate the app", 1, 5)
    feedback = st.text_area("Write your feedback")

    if st.button("Submit"):
        data = {
            "user": st.session_state.user,
            "rating": rating,
            "feedback": feedback
        }

        if os.path.exists("feedback.json"):
            old = json.load(open("feedback.json"))
        else:
            old = []

        old.append(data)
        json.dump(old, open("feedback.json", "w"))

        st.success("Feedback submitted!")

# ---------------- MAIN ----------------
if not st.session_state.user:
    login_page()
else:
    page = sidebar()

    if page == "Analyzer":
        analyzer_page()

    elif page == "Compare Contracts":
        compare_page()

    elif page == "Feedback":
        feedback_page()