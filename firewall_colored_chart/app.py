import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
from firewall_engine import analyze_email

st.set_page_config(page_title="AI Email Firewall Dashboard", layout="wide")
st.title("📧 AI Email Firewall Dashboard")

email = st.text_area("Paste Email Content")

if st.button("Scan Email"):
    if email.strip() == "":
        st.warning("Please enter email content")
    else:
        result = analyze_email(email)
        st.subheader("Scan Result")
        st.json(result)
        st.success("Email scanned and logged successfully")
        st.rerun()

st.markdown("---")
st.subheader("📊 Threat Analytics Dashboard")

if os.path.exists("logs.csv"):
    df = pd.read_csv("logs.csv")

    if len(df) >= 1:
        # Threat Distribution
        st.write("Threat Distribution")
        fig1, ax1 = plt.subplots()
        df["Threat Level"].value_counts().plot(kind="bar", ax=ax1, color=["green","orange","red"])
        st.pyplot(fig1)

        # Actual vs Predicted Line Chart
        st.write("Actual vs Predicted Threat Score")
        df["Actual"] = df["Final Score"]
        df["Predicted"] = df["Final Score"] * 0.9  # simulated prediction

        fig2, ax2 = plt.subplots()
        ax2.plot(df.index, df["Actual"], label="Actual Score", color="green", marker="o")
        ax2.plot(df.index, df["Predicted"], label="Predicted Score", color="red", linestyle="--", marker="x")
        ax2.set_xlabel("Email Index")
        ax2.set_ylabel("Threat Score")
        ax2.legend()
        st.pyplot(fig2)

        # Confusion Matrix
        st.write("Confusion Matrix (Demo)")
        cm = [[8, 2], [1, 9]]
        fig3, ax3 = plt.subplots()
        ax3.imshow(cm, cmap="Blues")
        for i in range(2):
            for j in range(2):
                ax3.text(j, i, cm[i][j], ha="center", va="center")
        ax3.set_xlabel("Predicted")
        ax3.set_ylabel("Actual")
        st.pyplot(fig3)
    else:
        st.info("Logs file exists but no data yet.")
else:
    st.info("Scan emails to generate analytics.")