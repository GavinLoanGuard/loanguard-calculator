import streamlit as st

# Function to calculate revenue
def calculate_revenue(deals_per_month, avg_mortgage, lender_commission, loanguard_commission, retention_rate, refinance_rate):
    lender_revenue = deals_per_month * avg_mortgage * (lender_commission / 100)
    loanguard_revenue = deals_per_month * avg_mortgage * (loanguard_commission / 100)
    
    lost_clients = deals_per_month * (refinance_rate / 100)
    lost_revenue = lost_clients * avg_mortgage * (lender_commission / 100)
    
    additional_revenue = loanguard_revenue - lender_revenue
    retained_clients = deals_per_month * (retention_rate / 100)
    retained_revenue = retained_clients * avg_mortgage * (loanguard_commission / 100)
    
    return lender_revenue, loanguard_revenue, lost_revenue, additional_revenue, retained_revenue

# Streamlit UI
st.title("🏡 Mortgage Broker Profit Maximizer Calculator")
st.write("🚀 See how much more you could be earning with Loanguard vs. lender insurance.")

# User Inputs
deals_per_month = st.number_input("📊 How many mortgage deals do you close per month?", min_value=1, value=10)
avg_mortgage = st.number_input("💵 What is your average mortgage loan size?", min_value=50000, value=400000)
lender_commission = st.slider("🏦 Current lender insurance commission (%)", min_value=0.5, max_value=5.0, value=1.0, step=0.1)
loanguard_commission = st.slider("🔑 Loanguard commission (%)", min_value=1.5, max_value=7.0, value=3.0, step=0.1)
retention_rate = st.slider("📈 Client retention with Loanguard (%)", min_value=50, max_value=100, value=85, step=5)
refinance_rate = st.slider("🔄 Clients lost due to refinancing (%)", min_value=10, max_value=50, value=30, step=5)

# Button to calculate revenue potential
if st.button("💰 Calculate My Revenue Potential"):
    lender_revenue, loanguard_revenue, lost_revenue, additional_revenue, retained_revenue = calculate_revenue(
        deals_per_month, avg_mortgage, lender_commission, loanguard_commission, retention_rate, refinance_rate)

    # Display Results
    st.subheader("📊 Your Results")
    st.write(f"💰 **Your current revenue with lender insurance:** **${lender_revenue:,.2f}/month**")
    st.write(f"💰 **Your potential revenue with Loanguard:** **${loanguard_revenue:,.2f}/month**")
    st.write(f"🚨 **Lost revenue due to lender insurance gaps:** **${lost_revenue:,.2f}/month**")
    st.write(f"📈 **Extra revenue if you switch to Loanguard:** **${additional_revenue:,.2f}/month**")
    st.write(f"🔒 **Revenue retained from existing clients with Loanguard:** **${retained_revenue:,.2f}/month**")

    st.success("✅ Want to see how Loanguard works? **[Book a quick call!](#)**")

