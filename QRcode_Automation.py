import streamlit as st
import qrcode
import time
import uuid


# ----------- PAGE TITLE ------------------
st.title("QR Code Automation")

# ----------- USER INPUT ------------------
data = st.text_input("Enter text or URL")
expiry_time = 15 # SECOND

# ---------- SESSION STATE ----------------
if "active" not in st.session_state:
    st.session_state.active = False

if "token" not in st.session_state:
    st.session_state.token=None

# ---------- GENERATE/ REGENERATE ------------
if st.button("Generate / Regenerate QR"):
    st.session_state.active = True
    st.session_state.token=str(uuid.uuid4())[:8]

# ---------- QR + TOKEN LOGIC -----------
if st.session_state.active and data.strip():

    qr_data=f"{data} | Token:{st.session_state.token}"
    img = qrcode.make(qr_data)
    img.save("qrcode.png")
    st.success("QR Code Generated")
    img_box=st.image("qrcode.png")
    st.info(f"Token:{st.session_state.token}")

    # ------------ EXPIRY/COUNTDOWN LOGIC -------------
    timer_box=st.empty()

    for sec in range(expiry_time, 0, -1):
        timer_box.warning(f"QR expires in {sec} seconds")
        time.sleep(1)

    # ------------ AFTER EXPIRY -------------
    img_box.empty()
    timer_box.error("❌ QR Code Expired (Token Invalid")

    st.session_state.active = False
    st.session_state.token=None








































