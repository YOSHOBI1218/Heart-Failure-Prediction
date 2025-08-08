import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

# ----------------- PAGE CONFIG -----------------
st.set_page_config(page_title="Heart Failure Prediction", layout="wide")

# ----------------- SIDEBAR TOGGLE -----------------
if "sidebar_visible" not in st.session_state:
    st.session_state.sidebar_visible = True

if "menu" not in st.session_state:
    st.session_state.menu = "Data Exploration"

def toggle_sidebar():
    st.session_state.sidebar_visible = not st.session_state.sidebar_visible

# Toggle button in main page
st.button("☰ Toggle Menu", on_click=toggle_sidebar)

# ----------------- LOAD DATA & MODEL -----------------
@st.cache_data
def load_data():
    df = pd.read_csv("dataset/heart_failure_clinical_records (1).csv")
    return df.convert_dtypes()

@st.cache_resource
def load_model():
    return joblib.load("model/random_forest_model.joblib")

data = load_data()
model = load_model()

# ----------------- SIDEBAR -----------------
if st.session_state.sidebar_visible:
    st.sidebar.title("🔧 Menu")
    # Update menu selection in session_state
    st.session_state.menu = st.sidebar.radio("Go to:", ["Data Exploration", "Visualisations", "Model Prediction", "Model Performance"], index=["Data Exploration", "Visualisations", "Model Prediction", "Model Performance"].index(st.session_state.menu))
else:
    st.sidebar.empty()  # Hide sidebar contents

# ----------------- APP TITLE & DESCRIPTION -----------------
st.title("💓 Heart Failure Prediction App")
st.markdown("""
This interactive Streamlit app predicts the risk of heart failure based on patient medical records.  
You can explore the dataset, view visual insights, try predictions, and check model performance.
""")

menu = st.session_state.menu

# ----------------- DATA EXPLORATION -----------------
if menu == "Data Exploration":
    st.header("🔍 Dataset Overview")

    st.write("**Shape of Dataset:**", data.shape)
    st.write("**Column Names and Data Types:**")
    st.dataframe(data.dtypes.astype(str), use_container_width=True)

    st.subheader("📋 Sample Data")
    st.dataframe(data.sample(5), use_container_width=True)

    st.subheader("🔎 Filter Data")
    age_range = st.slider("Filter by Age", int(data.age.min()), int(data.age.max()), (40, 60))
    sex_option = st.selectbox("Filter by Sex", ["All", "0 (Female)", "1 (Male)"])

    filtered_data = data[(data.age >= age_range[0]) & (data.age <= age_range[1])]
    if sex_option != "All":
        filtered_data = filtered_data[filtered_data.sex == int(sex_option[0])]

    st.write("**Filtered Data:**")
    st.dataframe(filtered_data, use_container_width=True)

# ----------------- VISUALISATIONS -----------------
elif menu == "Visualisations":
    st.header("📊 Data Visualisations")

    st.subheader("🧓 Heart Failure by Age")
    fig1, ax1 = plt.subplots()
    sns.histplot(data, x="age", hue="DEATH_EVENT", kde=True, ax=ax1)
    st.pyplot(fig1)

    st.subheader("🧑 Sex Distribution")
    fig2, ax2 = plt.subplots()
    data['sex_label'] = data['sex'].map({0: 'Female', 1: 'Male'})
    data['sex_label'].value_counts().plot.pie(
        autopct='%1.1f%%', startangle=90, colors=['#FF9999', '#66B2FF'], ax=ax2
    )
    ax2.set_ylabel('')
    st.pyplot(fig2)

    st.subheader("📈 Correlation Heatmap")
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sns.heatmap(data.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax3)
    st.pyplot(fig3)

# ----------------- MODEL PREDICTION -----------------
elif menu == "Model Prediction":
    st.header("🧪 Predict Heart Failure Risk")
    st.markdown("### Enter Patient Details:")

    age = st.number_input("Age", min_value=0, max_value=130, value=60)
    anaemia = st.selectbox("Anaemia", [0, 1])
    creatinine_phosphokinase = st.number_input("Creatinine Phosphokinase", value=582)
    diabetes = st.selectbox("Diabetes", [0, 1])
    ejection_fraction = st.number_input("Ejection Fraction", value=38)
    high_blood_pressure = st.selectbox("High Blood Pressure", [0, 1])
    platelets = st.number_input("Platelets", value=265000.0)
    serum_creatinine = st.number_input("Serum Creatinine", value=1.1)
    serum_sodium = st.number_input("Serum Sodium", value=137)
    sex = st.selectbox("Sex", [0, 1])
    smoking = st.selectbox("Smoking", [0, 1])
    time = st.number_input("Follow-up Period (days)", value=130)

    input_data = np.array([[age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction,
                            high_blood_pressure, platelets, serum_creatinine, serum_sodium,
                            sex, smoking, time]])

    if st.button("Predict"):
        with st.spinner("Predicting..."):
            prediction = model.predict(input_data)[0]
            proba = model.predict_proba(input_data)[0][1]

        st.success("✅ Prediction complete!")
        st.write(f"### 🎯 Prediction: **{'DEATH' if prediction == 1 else 'SURVIVAL'}**")
        st.write(f"📈 Probability of Death: `{proba * 100:.2f}%`")

# ----------------- MODEL PERFORMANCE -----------------
elif menu == "Model Performance":
    st.header("📉 Model Performance Metrics")

    X_test = data.drop("DEATH_EVENT", axis=1)
    y_test = data["DEATH_EVENT"]
    y_pred = model.predict(X_test)

    st.subheader("📋 Classification Report")
    report_df = pd.DataFrame(classification_report(y_test, y_pred, output_dict=True)).transpose()
    st.dataframe(report_df, use_container_width=True)

    st.subheader("🔲 Confusion Matrix")
    fig4, ax4 = plt.subplots()
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(ax=ax4)
    st.pyplot(fig4)

    st.markdown("""
    **Model Used:** Random Forest Classifier  
    **Evaluation Metrics:** Accuracy, Precision, Recall, F1-Score  
    
    """)

