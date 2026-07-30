import streamlit as st

st.set_page_config(
    page_title="ATM Management System",
    page_icon="🏧",
    layout="centered"
)

# ---------------- Session State ---------------- #

if "balance" not in st.session_state:
    st.session_state.balance = 5000

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- Title ---------------- #

st.title("🏧 ATM Management System")

# ---------------- Login ---------------- #

if not st.session_state.logged_in:

    st.subheader("Login")

    pin = st.text_input("Enter PIN", type="password")

    if st.button("Login", use_container_width=True):

        if pin == "1234":
            st.session_state.logged_in = True
            st.success("Login Successful")
            st.rerun()

        elif pin == "":
            st.warning("Please enter your PIN.")

        else:
            st.error("Invalid PIN")

# ---------------- ATM Menu ---------------- #

else:

    st.success("Welcome!")

    option = st.selectbox(
        "Choose an Option",
        [
            "Check Balance",
            "Deposit Amount",
            "Withdraw Amount"
        ]
    )

    # -------- Check Balance -------- #

    if option == "Check Balance":

        if st.button("Check Balance", use_container_width=True):
            st.info(f"Current Balance : ₹{st.session_state.balance}")

    # -------- Deposit -------- #

    elif option == "Deposit Amount":

        deposit = st.number_input(
            "Enter Deposit Amount",
            min_value=1,
            value=1,
            step=1
        )

        if st.button("Deposit", use_container_width=True):
            st.session_state.balance += deposit
            st.success(f"₹{deposit} Deposited Successfully")
            st.info(f"Available Balance : ₹{st.session_state.balance}")

    # -------- Withdraw -------- #

    elif option == "Withdraw Amount":

        withdraw = st.number_input(
            "Enter Withdrawal Amount",
            min_value=1,
            value=1,
            step=1
        )

        if st.button("Withdraw", use_container_width=True):

            if withdraw > st.session_state.balance:
                st.error("Insufficient Balance")

            else:
                st.session_state.balance -= withdraw
                st.success(f"₹{withdraw} Withdrawn Successfully")
                st.info(f"Available Balance : ₹{st.session_state.balance}")

    st.divider()

    if st.button("Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.rerun()
