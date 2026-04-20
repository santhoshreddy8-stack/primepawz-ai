import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier


# --- THE MAGIC PAINTBRUSH (CSS INJECTION) ---
page_bg_gradient = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(to bottom right, #4A00E0, #8E2DE2);
    color: white; 
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0); /* Makes the top header invisible */
}
</style>
"""
st.markdown(page_bg_gradient, unsafe_allow_html=True)
# --------------------------------------------

# ... (The rest of your normal code starting with st.title goes below here!) ...

# 1. Design the Website Header
st.title("ChurnIQ Analytics")
st.write("Welcome to the Manager Dashboard. Enter customer data below to predict if they will return!")

# 2. Train the AI Brain (Quietly in the background)
data = {
    'Times_Visited': [1, 5, 2, 8, 1, 10],
    'Total_Spent_INR': [100, 5000, 200, 8000, 50, 10000],
    'Bought_Again': [0, 1, 0, 1, 0, 1] 
}
df = pd.DataFrame(data)
X_clues = df[['Times_Visited', 'Total_Spent_INR']] 
y_answers = df['Bought_Again'] 
brain = DecisionTreeClassifier()
brain.fit(X_clues, y_answers)

# 3. Create Web Inputs for the User
st.subheader("Enter New Customer Details:")
visits = st.number_input("How many times did they visit?", min_value=1, value=5)
spent = st.number_input("How much did they spend (INR)?", min_value=0, value=2000)

# 4. Create the Magic Button!
if st.button("🔮 Predict Customer Future"):
    
    # Ask the brain!
    prediction = brain.predict([[visits, spent]])
    
    # Show the results on the website
    st.divider()
    if prediction[0] == 1:
        st.success("A.I. Result: YES! They will be a VIP. Send them a Thank You email! 🏆")
    else:
        st.error("A.I. Result: NO. High risk of leaving forever. Send a 20% Discount! 🚨")