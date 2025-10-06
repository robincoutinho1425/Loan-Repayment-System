import streamlit as st

st.set_page_config(page_title="Loan Repayment Predictor", page_icon="💰", layout="wide")

st.markdown("""
<style>
    /* Reset */
    * {margin: 0; padding: 0; box-sizing: border-box;}

    /* Page Body */
    .main {
        text-align: center;
        font-family: 'Segoe UI', sans-serif;
        padding: 60px 20px;
    }
    .main h1 {
        color: #0d47a1;
        font-size: 48px;
        font-weight: 700;
        margin-bottom: 20px;
    }
    .main p {
        color: #444;
        font-size: 20px;
        margin-bottom: 30px;
    }
    .main img {
        max-width: 80%;
        border-radius: 15px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
    }

    /* Footer */
    footer {
        background-color: #0d47a1;
        color: white;
        text-align: center;
        padding: 10px;
        margin-top: 60px;
        width: 100%;
        font-weight: 500;
        border-radius: 0;
    }
</style>

<div class="main">
    <h1>Welcome to the Loan Repayment Prediction System</h1>
    <p>Use this AI-powered system to assess a borrower’s likelihood of repaying their loan efficiently and accurately.</p>
    <img src="https://imgs.search.brave.com/4UvvsjSVnl9dYGom1YKnBdhSjMYYflQrWFLXIS8gbfQ/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTM5/NTE1NDg2OC92ZWN0/b3IvbG9hbi1yZXBh/eW1lbnQtbGVuZGlu/Zy1sb2FuLWNhbmNl/bGxhdGlvbi1kZW5p/YWwtb2YtZnVuZGlu/Zy1sZW5kaW5nLW1l/dGFwaG9yLWJhbmst/c2VydmljZS5qcGc_/cz02MTJ4NjEyJnc9/MCZrPTIwJmM9b3dD/clpoRnhkX18xVkx1/UUN3WlQ2SVhnUzNQ/aVJycVNhOXlJWVlt/T0NFUT0" alt="Loan Prediction Image">
</div>

<footer>
    <p>© 2025 Loan Repayment Predictor | Designed by Robin Coutinho</p>
</footer>
""", unsafe_allow_html=True)
