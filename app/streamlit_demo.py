import streamlit as st

st.set_page_config(page_title="Scam Shield – Hinglish Scam Detector", page_icon="🛡️")
st.title("Scam Shield – Hinglish Scam Detector")
st.write("Friendly, supportive assistant to help you spot risky WhatsApp messages in Hinglish.")

msg = st.text_area("Paste a WhatsApp-style message:", height=150)

def simple_rules(text: str) -> float:
    text = text.lower()
    hits = 0
    keywords = ["otp", "kyc", "link", "click", "lottery", "refund", "verify", "fees", "bank", "upi", "pan", "fastag", "custom", "suspend"]
    for k in keywords:
        if k in text:
            hits += 1
    return min(hits / 5.0, 1.0)

if st.button("Check Risk"):
    if msg.strip():
        risk = simple_rules(msg)
        if risk >= 0.5:
            st.error(f"High scam risk. Confidence: {risk:.0%}")
            st.info("Care tip: OTP kisi ko mat batana. Unknown links mat kholna. Bank ki official app/website par verify karein.")
        else:
            st.success(f"Looks low risk. Confidence: {1-risk:.0%}")
            st.caption("General advice: Personal info share na karein. Agar doubt ho to verify karein.")
    else:
        st.warning("Please paste a message to analyze.")
