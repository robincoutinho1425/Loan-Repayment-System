import streamlit as st

st.set_page_config(page_title="Contact", page_icon="📞", layout="centered")

st.title("📞 Contact Information")

st.markdown("""
For project-related queries, collaborations, or just to say hi, feel free to connect!

**Name:** Ryan  
**Email:** ryan@example.com  
**Phone:** +91-XXXXXXXXXX  
**GitHub:** [github.com/ryan](https://github.com/ryan)  
**LinkedIn:** [linkedin.com/in/ryan](https://www.linkedin.com/in/ryan)  
**Portfolio:** [ryan.com](#)  

---

### 📌 Preferred Communication
- **Email:** For detailed queries, collaborations, or project proposals.  
- **LinkedIn:** For professional networking and updates.  
- **GitHub:** To explore my projects and code contributions.

---
""")

# Quick message form
st.subheader("💬 Quick Message")
name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Your Message")
if st.button("Send Message"):
    st.success("Thank you! Your message has been sent.")
