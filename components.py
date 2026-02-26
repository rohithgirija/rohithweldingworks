import streamlit as st

st.set_page_config(page_title="Welding Website", layout="wide")

# ---------------- SESSION STATE ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "buttons"

# ---------------- LOGIN PAGE ----------------
def login_page():
    st.markdown("""
        <style>
        .login-box {
            background:#111;
            padding:40px;
            border-radius:15px;
            text-align:center;
            color:white;
            box-shadow:0 0 20px red,0 0 40px orange,0 0 60px yellow;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align:center;'>🔥 Welding Website Login 🔥</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        with st.container():
            st.markdown("<div class='login-box'>", unsafe_allow_html=True)
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")

            if st.button("Login"):
                if username == "admin" and password == "1234":
                    st.session_state.logged_in = True
                    st.success("Login Successful ✅")
                    st.rerun()
                else:
                    st.error("Invalid Username or Password ❌")
            st.markdown("</div>", unsafe_allow_html=True)


# ---------------- BUTTON PAGE ----------------
def button_page():
    st.title("🔥 Welcome to Welding Website")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Continue"):
            st.session_state.page = "animated"

    with col2:
        if st.button("Open Calculator"):
            st.session_state.page = "calculator"

    with col3:
        if st.button("Open Websites"):
            st.session_state.page = "style"

    st.markdown("---")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()


# ---------------- CALCULATOR ----------------
def calculator_page():
    st.title("🧮 Calculator")

    num1 = st.number_input("Enter First Number")
    num2 = st.number_input("Enter Second Number")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("+"):
            st.success(num1 + num2)
    with col2:
        if st.button("-"):
            st.success(num1 - num2)
    with col3:
        if st.button("×"):
            st.success(num1 * num2)
    with col4:
        if st.button("÷"):
            if num2 != 0:
                st.success(num1 / num2)
            else:
                st.error("Cannot divide by zero")

    st.markdown("---")
    st.subheader("GST Calculator")

    amount = st.number_input("Amount")
    percent = st.number_input("GST %")

    if st.button("Calculate GST"):
        gst = (amount * percent) / 100
        total = amount + gst
        st.success(f"GST: ₹ {gst}")
        st.success(f"Total: ₹ {total}")

    if st.button("⬅ Back"):
        st.session_state.page = "buttons"


# ---------------- ANIMATED PAGE ----------------
def animated_page():
    st.title("Welding Services")

    st.subheader("Related Category")
    st.write("• MIG Welding")
    st.write("• TIG Welding")
    st.write("• Aluminium Welding")

    st.markdown("---")

    st.subheader("Services")

    st.success("Welding Fabrication Service - ₹135 / Kg - Coimbatore")
    st.success("TIG Welding Service - ₹530 / Day")

    if st.button("⬅ Back"):
        st.session_state.page = "buttons"


# ---------------- STYLE PAGE ----------------
def style_page():
    st.title("Open Websites")

    st.markdown("[Google](https://www.google.com)")
    st.markdown("[Flipkart](https://www.flipkart.com)")
    st.markdown("[Amazon](https://www.amazon.in)")
    st.markdown("[YouTube](https://www.youtube.com)")
    st.markdown("[Chrome](https://www.google.com/chrome/)")

    if st.button("⬅ Back"):
        st.session_state.page = "buttons"


# ---------------- MAIN CONTROL ----------------
if not st.session_state.logged_in:
    login_page()
else:
    if st.session_state.page == "buttons":
        button_page()
    elif st.session_state.page == "calculator":
        calculator_page()
    elif st.session_state.page == "animated":
        animated_page()
    elif st.session_state.page == "style":
        style_page()
