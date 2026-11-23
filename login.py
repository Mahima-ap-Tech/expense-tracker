import streamlit as st



def show_login():
    st.markdown("""
<style>

/* Login page background */
.stApp {
    background-color: #A07862;
}

/* Login card */
.login-card {
    background-color: #293747;
    padding: 35px;
    border-radius: 15px;
    max-width: 450px;
    margin: auto;
}

/* Heading and text */
h1, h2, h3, p, label {
    color: white;
}

</style>
""", unsafe_allow_html=True)

    st.title("🔐 SPEND WISE LOGIN")

    st.subheader("Welcome Back!")

    st.write("Login to manage your daily expenses.")

    username = st.text_input("Enter Username")

    password = st.text_input(
        "Enter Password",
        type="password"
    )

    if st.button("Login", use_container_width=True):

        if username and password:

            st.session_state.logged_in = True

            st.success("Login Successful!")

            st.rerun()

        else:
            st.warning("Please enter username and password.")

    st.divider()



    st.write("💚 Spend Smart. Save More.")