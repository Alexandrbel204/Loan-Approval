import streamlit as st
from ml import inference

st.header('Try Streamlit package')
st.text("My first ML app")

person_age = st.slider("Enter your age:", min_value=18, max_value=150, step=1)
person_income = st.slider("Enter your income:", max_value=8000000)
person_emp_exp = st.slider("Enter your experience years:", max_value=125)
loan_amount = st.slider("Enter the loan amount you want:", min_value=50, max_value=40000)
loan_int_rate = st.slider("Enter your interest rate(%):", min_value=5, max_value=20)
loan_percent_income = st.slider("Enter your percent income(%):", min_value=0.0, max_value=0.7, step=0.01)
cb_person_cred_hist_length = st.slider("Enter your credit length:", min_value=0, max_value=35, step=1)
credit_score = st.slider("Enter your credit score:", min_value=300, max_value=900, step=1)


gender = st.radio("Gender", ["Female", "Male"])
gender_male = 1 if gender == "Male" else 0

# Education
education = st.selectbox("Education Level",
    ["Associate", "Bachelor", "Doctorate", "High School", "Master"])
edu_bachelor = 1 if education == "Bachelor" else 0
edu_doctorate = 1 if education == "Doctorate" else 0
edu_highschool = 1 if education == "High School" else 0
edu_master = 1 if education == "Master" else 0

# Home Ownership
home_own = st.selectbox("Home Ownership",
    ["MORTGAGE", "OTHER", "OWN", "RENT"])
home_other = 1 if home_own == "OTHER" else 0
home_own_val = 1 if home_own == "OWN" else 0
home_rent = 1 if home_own == "RENT" else 0

# Loan Purpose
loan_purpose = st.selectbox("Loan Purpose", [
    "DEBTCONSOLIDATION", "EDUCATION",
    "HOMEIMPROVEMENT", "MEDICAL", "PERSONAL", "VENTURE"])
intent_edu = 1 if loan_purpose == "EDUCATION" else 0
intent_homeimp = 1 if loan_purpose == "HOMEIMPROVEMENT" else 0
intent_med = 1 if loan_purpose == "MEDICAL" else 0
intent_personal = 1 if loan_purpose == "PERSONAL" else 0
intent_venture = 1 if loan_purpose == "VENTURE" else 0

# Previous Defaults
prev_defaults = st.radio("Previous Defaults", ["No", "Yes"])
prev_defaults_yes = 1 if prev_defaults == "Yes" else 0

# Prepare feature vector in EXACT order matching model training columns
features = [
    person_age,
    person_income,
    person_emp_exp,
    loan_amount,
    loan_int_rate,
    loan_percent_income,
    cb_person_cred_hist_length,
    credit_score,
    gender_male,
    edu_bachelor,
    edu_doctorate,
    edu_highschool,
    edu_master,
    home_other,
    home_own_val,
    home_rent,
    intent_edu,
    intent_homeimp,
    intent_med,
    intent_personal,
    intent_venture,
    prev_defaults_yes
]

if st.button("Check Approval"):
    prediction = inference([features])
    result = "APPROVED" if prediction[0] == 1 else "DECLINED"
    st.subheader(f"Loan Decision: {result}")
    st.write("Based on our AI assessment of your profile")

