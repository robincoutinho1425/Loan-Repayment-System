import streamlit as st

st.set_page_config(page_title="About", page_icon="ℹ️", layout="centered")

st.title("ℹ️ About the Project")

st.markdown("""
This project predicts whether a borrower is likely to **fully repay a loan** using advanced **machine learning and ensemble learning techniques**.  
It aims to help financial institutions **assess credit risk** more accurately and make smarter, data-driven lending decisions.

---

### 🔧 **Key Details:**
- **Algorithm:** Ensemble Learning (Bagging, Boosting, Random Forest)
- **Features Used:** 13 borrower-related financial and demographic attributes
- **Framework:** Streamlit
- **Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Pickle
- **Developer:** Robin Coutinho

---

### 🎯 **Objective**
To build a robust predictive system that determines the likelihood of loan repayment by analyzing customer financial behavior and risk indicators.  
This helps reduce defaults, improve approval accuracy, and optimize loan portfolio management.

---

### ⚙️ **How It Works**
1. The dataset is cleaned and preprocessed (handling nulls, encoding categorical values, feature scaling).  
2. Machine learning models such as **Bagging**, **Boosting**, and **Random Forest** are trained and compared.  
3. The best-performing model is serialized using **Pickle** and integrated into the Streamlit interface.  
4. Users can input borrower details or upload data to get instant loan repayment predictions.

---

### 🚀 **Impact**
This project demonstrates the power of AI in finance — allowing real-time, data-driven decision support to reduce loan default risks and enhance customer trust.

---

### 💡 **Future Scope**
- Integrate with real-time financial APIs for live predictions.  
- Add model explainability using SHAP or LIME for transparency.  
- Deploy on the cloud for production-level use.  
- Extend to classify loan types and interest rate optimization.

---
""")
