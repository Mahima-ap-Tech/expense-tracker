import streamlit as st

st.image("coin.png", width=250)


st.markdown("""
<style>
.stApp {
    background-color:#59483F;
}
</style>
""", unsafe_allow_html=True)

st.title("💰 MY EXPENSE TRACKER")
st.subheader("Manage your Daily Expenses easily!")
st.markdown("""
- 💸 About Expense Tracker
- 💰 Keep track of where your money goes!
- 📊 Manage your daily expenses and stay within your budget.
- 🪙 Track your spending, understand your habits, and save more.
- 🎯 Make smarter financial decisions, one expense at a time.
- ✨ Small savings today, a better tomorrow! """)




import streamlit as st

st.title("💰 Welcome to Spend Wise!")
st.write("Manage your money and track your expenses easily.")

st.divider()

st.markdown("""
### 🌱 A Little Reminder

"Do not save what is left after spending,
but spend what is left after saving."
""")


st.subheader("✨ What You Can Do With Spend Wise")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown("""
        <div style="border-left: 5px solid #6D4938;
                    padding-left: 12px;">
            <h3>💸 Expense Tracking</h3>
            <p>Record and manage your daily expenses
            in one place.</p>
        </div>
        """, unsafe_allow_html=True)

with col2:
    with st.container(border=True):
        st.markdown("""
        <div style="border-left: 5px solid #806044;
                    padding-left: 12px;">
            <h3>🎯 Budget Planning</h3>
            <p>Set your budget and keep your spending
            under control.</p>
        </div>
        """, unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    with st.container(border=True):
        st.markdown("""
        <div style="border-left: 5px solid #77534B;
                    padding-left: 12px;">
            <h3>📊 Spending Analysis</h3>
            <p>Understand where your money goes
            with expense insights.</p>
        </div>
        """, unsafe_allow_html=True)

with col4:
    with st.container(border=True):
        st.markdown("""
        <div style="border-left: 5px solid #81704C;
                    padding-left: 12px;">
            <h3>💰 Savings Goals</h3>
            <p>Develop smart saving habits
            for a better future.</p>
        </div>
        """, unsafe_allow_html=True)



st.divider()

st.subheader("💳 Smart Spending Categories")
st.write("Explore and manage your expenses by category.")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.markdown("<h2 style='text-align:center;'>🍔</h2>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align:center;'>Food</h4>", unsafe_allow_html=True)
        st.caption("Restaurants, groceries and snacks")

with col2:
    with st.container(border=True):
        st.markdown("<h2 style='text-align:center;'>🚗</h2>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align:center;'>Travel</h4>", unsafe_allow_html=True)
        st.caption("Fuel, transport and trips")

with col3:
    with st.container(border=True):
        st.markdown("<h2 style='text-align:center;'>🛍️</h2>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align:center;'>Shopping</h4>", unsafe_allow_html=True)
        st.caption("Clothes and personal purchases")

col4, col5, col6 = st.columns(3)

with col4:
    with st.container(border=True):
        st.markdown("<h2 style='text-align:center;'>🏥</h2>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align:center;'>Healthcare</h4>", unsafe_allow_html=True)
        st.caption("Medicines and medical expenses")

with col5:
    with st.container(border=True):
        st.markdown("<h2 style='text-align:center;'>📚</h2>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align:center;'>Education</h4>", unsafe_allow_html=True)
        st.caption("Books, courses and fees")

with col6:
    with st.container(border=True):
        st.markdown("<h2 style='text-align:center;'>📦</h2>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align:center;'>Others</h4>", unsafe_allow_html=True)
        st.caption("Other daily expenses")




# Budget
budget = st.number_input("Enter Amount", min_value=0)

if st.button("Set Budget"):
    st.session_state.budget = budget
    st.success("Budget set successfully")


# Add expense
st.title("ADD AN EXPENSE")

category = st.multiselect(
    "Select Category",
    [
        "Grocery 🛒",
        "Personal Care 🧴",
        "Entertainment 🎥",
        "Shopping 🛍️",
        "Travel 🚵",
        "Restaurant 🥗",
        "Transport 🚚"
    ]
)

exp_name = st.text_input("Enter Expense Name")

exp_amt = st.number_input(
    "Enter Expense Amount",
    min_value=0
)

if st.button("Add an Expense"):
    if exp_name and exp_amt > 0:
        st.session_state.expenses.append({
            "Name": exp_name,
            "Category": category,
            "amount": exp_amt
        })

        st.success("Expense added successfully")

    else:
        st.warning("Enter expense name and amount")

# Calculate expenses
total = sum(
    expense["amount"]
    for expense in st.session_state.expenses
)

remaining = st.session_state.budget - total

# Summary
st.title("MY SUMMARY")

st.write("Total Budget: ₹", st.session_state.budget)
st.write("Total Spent: ₹", total)
st.write("Remaining Balance: ₹", remaining)


# Expense history
st.title("EXPENSE HISTORY")

for expense in st.session_state.expenses:
    st.write(
        expense["Name"],
        expense["Category"],
        expense["amount"]
    )

st.subheader("📊 Your Financial Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Monthly Budget", budget)
col2.metric("Total Expenses", exp_amt)
col3.metric("Remaining", remaining)


st.divider()

st.subheader("🌱 Your Daily Money Motivation")

st.success("""
💡 Don't save what is left after spending;
spend what is left after saving.

Every small saving makes a difference!
""")


st.divider()

st.markdown("""
<div style="text-align:center; padding:20px;">
    <h3>💚 Spend Wise</h3>
    <p>Track Smart. Spend Better. Save More.</p>
    <p>Made with ❤️ using Python & Streamlit</p>
    <small>© 2026 Spend Wise | All Rights Reserved</small>
</div>
""", unsafe_allow_html=True)