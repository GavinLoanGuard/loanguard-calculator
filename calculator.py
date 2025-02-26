import streamlit as st

def calculate_revenue(deals_per_month, avg_mortgage, lender_commission_multiplier, loanguard_commission_multiplier, retention_rate, refinance_rate):
    avg_premium = avg_mortgage * 0.003  # Estimated mortgage insurance premium (0.3% of loan value)
    
    lender_revenue = deals_per_month * avg_premium * lender_commission_multiplier
    loanguard_revenue = deals_per_month * avg_premium * loanguard_commission_multiplier
    
    lost_clients = deals_per_month * (refinance_rate / 100)
    lost_revenue = lost_clients * avg_premium * lender_commission_multiplier
    
    additional_revenue = loanguard_revenue - lender_revenue
    retained_clients = deals_per_month * (retention_rate / 100)
    retained_revenue = retained_clients * avg_premium * loanguard_commission_multiplier
    
    return lender_revenue, loanguard_revenue, lost_revenue, additional_revenue, retained_revenue

st.title("🚀 STOP LOSING THOUSANDS: The Mortgage Broker Revenue Maximizer")
st.subheader("You’re Leaving BIG Money on the Table—Find Out How Much in Seconds!")

st.write("**Fact:** Most brokers settle for lender-provided mortgage insurance and **miss out on massive commissions.** Let’s calculate how much you’re losing—and how much more you could be making with Loanguard!")

# User inputs
deals_per_month = st.number_input("📊 How many mortgage deals do you close per month?", min_value=1, value=15)
avg_mortgage = st.number_input("💵 Average mortgage loan size?", min_value=50000, value=1000000)
lender_commission_multiplier = st.slider("🏦 Lender Insurance Commission (Multiplier of Monthly Premium)", min_value=5, max_value=12, value=9, step=1)
loanguard_commission_multiplier = st.slider("🔑 Loanguard Commission (Multiplier of Monthly Premium)", min_value=10, max_value=20, value=15, step=1)
retention_rate = st.slider("📈 Client retention with Loanguard (%)", min_value=50, max_value=100, value=85, step=5)
refinance_rate = st.slider("🔄 Clients lost due to refinancing (%)", min_value=10, max_value=50, value=30, step=5)

if st.button("💰 Show Me My Hidden Profits"):
    lender_revenue, loanguard_revenue, lost_revenue, additional_revenue, retained_revenue = calculate_revenue(
        deals_per_month, avg_mortgage, lender_commission_multiplier, loanguard_commission_multiplier, retention_rate, refinance_rate)
    
    st.subheader("📊 Your Results")
    st.write(f"💰 **Your current revenue with lender insurance:** **${lender_revenue:,.2f}/month**")
    st.write(f"💰 **Your potential revenue with Loanguard:** **${loanguard_revenue:,.2f}/month**")
    st.write(f"🚨 **Lost revenue due to lender insurance gaps:** **${lost_revenue:,.2f}/month**")
    st.write(f"📈 **Extra revenue if you switch to Loanguard:** **${additional_revenue:,.2f}/month**")
    st.write(f"🔒 **Revenue retained from existing clients with Loanguard:** **${retained_revenue:,.2f}/month**")
    
    st.success("✅ Stop losing money—**[Book a quick 10-minute strategy call now!](#)**")


