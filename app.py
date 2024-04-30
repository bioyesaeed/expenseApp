import streamlit as st
import pandas as pd

st.set_page_config(page_title="Expense App",
                   page_icon=":dollar_banknote:")


# --- Title----

st.subheader("Castush Expense App")


expenses = {
    "Purchases": [],
    "Amounts": []
}


# ------- Form ----------
with st.form(key="form", clear_on_submit=True):
    purchase = st.text_input('Enter your purchase')
    amount = st.number_input('Enter the amount')
    add_btn = st.form_submit_button("Add", type="primary")


# Event handler
def addPurchase(purchase, amount):
    if purchase and amount:
        expenses.get('Purchases').append(purchase)
        expenses.get("Amounts").append(amount)


if add_btn:
    addPurchase(purchase=purchase, amount=amount)

# Create a DataFrame Object
df = pd.DataFrame(expenses)

# Display df as a table

if len(expenses.get('Purchases')) > 0 and len(expenses.get('Amounts')) > 0:
    st.table(df)

amounts_list = expenses.get("Amounts")

total = 0
if len(amounts_list) > 0:

    for item in amounts_list:
        total += item

    st.subheader(f'Your total expenses is: {total}')


# -------- Test Code
# def tDisplay(purchase, amount):
#     st.write(f"Purchase: {purchase}  Amount: {amount}")


# if add_btn:
#     tDisplay(purchase, amount)
