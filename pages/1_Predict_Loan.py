import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Predict Loan", page_icon="🔍", layout="wide")

model = joblib.load("trained_model.pkl")

st.title("🔍 Predict Loan Repayment")

col1, col2 = st.columns(2)

credit_policy = col1.selectbox("Credit Policy (0 = No, 1 = Yes)", [0, 1])
purpose_options = {"Credit Card":0, "Debt Consolidation":1, "Home Improvement":2, "Small Business":3, "Other":4}
purpose = col2.selectbox("Purpose of Loan", list(purpose_options.keys()))
int_rate = col1.slider("Interest Rate (%)", 0.0, 50.0, 10.0, 0.01)
installment = col2.slider("Installment Amount", 0.0, 5000.0, 500.0, 1.0)
log_annual_inc = col1.number_input("Log Annual Income", min_value=0.0, step=0.01, value=10.0)
dti = col2.slider("Debt-to-Income Ratio", 0.0, 50.0, 20.0, 0.01)
fico = col1.slider("FICO Score", 300, 850, 700, 1)
days_with_cr_line = col2.slider("Days with Credit Line", 0, 20000, 5000, 1)
revol_bal = col1.number_input("Revolving Balance", min_value=0.0, step=1.0, value=1000.0)
revol_util = col2.slider("Revolving Utilization (%)", 0.0, 200.0, 50.0, 0.01)
inq_last_6mths = col1.slider("Inquiries Last 6 Months", 0, 20, 1, 1)
delinq_2yrs = col2.slider("Delinquencies in 2 Years", 0, 10, 0, 1)
pub_rec = col1.slider("Public Records", 0, 10, 0, 1)

inputs = [credit_policy, purpose_options[purpose], int_rate, installment,
          log_annual_inc, dti, fico, days_with_cr_line, revol_bal,
          revol_util, inq_last_6mths, delinq_2yrs, pub_rec]

if st.button("Predict Loan Repayment"):
    prediction = model.predict(np.array([inputs]))
    if prediction[0] == 1:
        st.error("❌ Borrower likely NOT to fully repay the loan.")
    else:
        st.success("✅ Borrower likely to fully repay the loan.")
