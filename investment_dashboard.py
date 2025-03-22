import streamlit as st
import matplotlib.pyplot as plt

# App Title
st.title("💰 Investment Growth Dashboard")

# Sidebar Inputs
initial = st.number_input("Initial Investment (EGP)", value=10000, step=1000)
rate = st.slider("Annual Interest Rate (%)", min_value=1.0, max_value=20.0, value=7.0) / 100
monthly_contrib = st.number_input("Monthly Contribution (EGP)", value=1500, step=500)
years = st.slider("Investment Duration (Years)", min_value=1, max_value=50, value=10)

# Calculations
monthly_rate = rate / 12
balance = initial
total_contributed = initial

years_list = []
balance_list = []
interest_list = []

for year in range(1, years + 1):
    for month in range(12):
        balance += monthly_contrib
        total_contributed += monthly_contrib
        balance *= (1 + monthly_rate)
    years_list.append(year)
    balance_list.append(round(balance, 2))
    interest_list.append(round(balance - total_contributed, 2))

# Results
st.subheader("📊 Final Results")
st.write(f"**Final Balance:** {round(balance, 2)} EGP")
st.write(f"**Total Contributed:** {round(total_contributed, 2)} EGP")
st.write(f"**Total Interest Earned:** {round(balance - total_contributed, 2)} EGP")

# Chart
fig, ax = plt.subplots()
ax.plot(years_list, balance_list, label='Total Balance', marker='o')
ax.plot(years_list, interest_list, label='Interest Earned', marker='o')
ax.set_xlabel("Year")
ax.set_ylabel("EGP")
ax.set_title("Investment Growth Over Time")
ax.grid(True)
ax.legend()

st.pyplot(fig)