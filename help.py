import streamlit as st

st.title("❓ HELP & SUPPORT")

st.subheader("How to use Spend Wise?")

st.write("Follow these simple steps to manage your expenses.")

with st.expander("💰 How to set a budget?"):
    st.write(
        "Go to the Home page, enter your budget amount "
        "and click Set Budget."
    )

with st.expander("➕ How to add an expense?"):
    st.write(
        "Select an expense category, enter the expense "
        "name and amount, then click Add an Expense."
    )

with st.expander("📊 How to view Dashboard?"):
    st.write(
        "Click Dashboard in the sidebar to view your "
        "total expenses and bar chart."
    )

with st.expander("📋 How to view expense history?"):
    st.write(
        "Go to Home to view your previously added expenses."
    )

st.divider()

st.subheader("💡 Need Help?")

st.write(
    "If you face any issues while using Spend Wise, "
    "please check that you have entered the correct details."
)

st.info("Thank you for using Spend Wise! 💚")