import streamlit as st
import pandas as pd
from datetime import date 

st.title("📊 SPEND WISE DASHBOARD")

# Calculate total
total = sum(
    expense["amount"]
    for expense in st.session_state.expenses
)

# Summary cards
col1, col2 = st.columns(2)

col1.metric(
    "Total Budget",
    f"₹{st.session_state.budget}"
)

col2.metric(
    "Total Expenses",
    f"₹{total}"
)

st.divider()

# Bar chart
st.subheader("📊 EXPENSE ANALYSIS")

if st.session_state.expenses:

    df = pd.DataFrame(st.session_state.expenses)

    st.bar_chart(
        df.set_index("Name")["amount"]
    )

else:
    st.info("No expenses added yet. Add expenses from Home.")

# Expense history
st.subheader("EXPENSE HISTORY")

if st.session_state.expenses:
    st.dataframe(
        pd.DataFrame(st.session_state.expenses),
        use_container_width=True
    )

date=st.date_input("select date")