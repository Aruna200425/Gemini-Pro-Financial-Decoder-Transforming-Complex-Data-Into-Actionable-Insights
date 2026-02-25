import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import google.generativeai as genai


genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-pro")

st.title("💎 Gemini Pro Financial Decoder")
st.subheader("Transforming Complex Data into Actionable Insights")


uploaded_file = st.file_uploader("sample_financial_data.csv", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("### 📊 Raw Data")
    st.dataframe(df)

    st.write("### 📈 Financial Summary")

    revenue = df["Revenue"].sum()
    expenses = df["Expenses"].sum()
    profit = revenue - expenses
    avg_growth = df["Revenue"].pct_change().mean() * 100

    summary_text = f"""
    Total Revenue: {revenue}
    Total Expenses: {expenses}
    Net Profit: {profit}
    Average Revenue Growth: {avg_growth:.2f}%
    """

    st.text(summary_text)


    st.write("### 📉 Revenue vs Expenses Chart")
    plt.figure()
    plt.plot(df["Month"], df["Revenue"])
    plt.plot(df["Month"], df["Expenses"])
    plt.legend(["Revenue", "Expenses"])
    st.pyplot(plt)

    if st.button("Generate AI Financial Insights"):
        prompt = f"""
        Analyze the following financial summary and provide:
        - Business performance insights
        - Risk factors
        - Improvement strategies
        - Investment suggestions

        Financial Summary:
        {summary_text}
        """

        response = model.generate_content(prompt)
        st.write("### 🤖 Gemini Pro Insights")
        st.write(response.text)