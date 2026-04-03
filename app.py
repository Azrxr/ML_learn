import streamlit as st
import joblib
import numpy as np
import pandas as pd

# ==============================
# LOAD MODEL
# ==============================
@st.cache_resource
def load_model():
    try:
        model = joblib.load('model/pipeline.pkl')
        return model
    except FileNotFoundError:
        st.error("Model file not found.")
        return None

# ==============================
# FEATURE ORDER
# ==============================
FEATURE_NAMES = [
    'Curricular_units_2nd_sem_approved',
    'Curricular_units_1st_sem_approved',
    'Curricular_units_2nd_sem_grade',
    'Curricular_units_1st_sem_grade',
    'Curricular_units_2nd_sem_evaluations',
    'Admission_grade',
    'Tuition_fees_up_to_date',
    'Curricular_units_1st_sem_evaluations',
    'Previous_qualification_grade',
    'Course'
]

# ==============================
# PREDICTION FUNCTION
# ==============================
def predict_dropout(model, input_data):
    df_input = pd.DataFrame([input_data], columns=FEATURE_NAMES)
    
    prediction = model.predict(df_input)[0]
    probabilities = model.predict_proba(df_input)[0]
    
    return prediction, probabilities

# ==============================
# MAIN APP
# ==============================
def main():

    st.set_page_config(
        page_title="Student Dropout Prediction",
        page_icon="🎓",
        layout="wide"
    )

    model = load_model()
    if model is None:
        st.stop()

    # ==============================
    # HEADER
    # ==============================
    st.title("🎓 Student Dropout Prediction System")
    st.markdown("---")
    st.markdown("**Predict whether a student is likely to Dropout or Graduate based on academic performance.**")

    st.info("""
    💡 **Key Insight:**  
    Academic performance (approved units & grades) is the strongest predictor of student success.
    """)

    # ==============================
    # INPUT
    # ==============================
    col1, col2 = st.columns(2)

    with col1:
        st.header("Academic Background")

        course = st.number_input('Course Code', 1, 9999, 33)
        previous_qualification_grade = st.number_input('Previous Qualification Grade', 0.0, 200.0, 120.0)
        admission_grade = st.number_input('Admission Grade', 0.0, 200.0, 120.0)
        tuition_fees_up_to_date = st.selectbox(
            'Tuition Fees Up to Date',
            [1, 0],
            format_func=lambda x: 'Yes' if x == 1 else 'No'
        )

    with col2:
        st.header("Academic Performance")

        curricular_units_1st_sem_approved = st.number_input('1st Sem Approved', 0, 30, 6)
        curricular_units_1st_sem_grade = st.number_input('1st Sem Grade', 0.0, 20.0, 12.0)
        curricular_units_1st_sem_evaluations = st.number_input('1st Sem Evaluations', 0, 30, 6)

        curricular_units_2nd_sem_approved = st.number_input('2nd Sem Approved', 0, 30, 6)
        curricular_units_2nd_sem_grade = st.number_input('2nd Sem Grade', 0.0, 20.0, 12.0)
        curricular_units_2nd_sem_evaluations = st.number_input('2nd Sem Evaluations', 0, 30, 6)

    # ==============================
    # PREDICTION
    # ==============================
    st.markdown("---")

    if st.button("Predict Student Outcome", use_container_width=True):

        input_data = [
            curricular_units_2nd_sem_approved,
            curricular_units_1st_sem_approved,
            curricular_units_2nd_sem_grade,
            curricular_units_1st_sem_grade,
            curricular_units_2nd_sem_evaluations,
            admission_grade,
            tuition_fees_up_to_date,
            curricular_units_1st_sem_evaluations,
            previous_qualification_grade,
            course
        ]

        try:
            prediction, probabilities = predict_dropout(model, input_data)

            status_mapping = {
                0: ("Dropout", "🔴"),
                1: ("Graduate", "🟢")
            }

            status_name, emoji = status_mapping[prediction]

            # ==============================
            # RESULT
            # ==============================
            st.markdown("### Prediction Result")

            if prediction == 0:
                st.error(f"{emoji} **{status_name}** (High Risk)")
            else:
                st.success(f"{emoji} **{status_name}** (Low Risk)")

            # ==============================
            # PROBABILITIES
            # ==============================
            st.markdown("### Confidence")

            labels = ["Dropout", "Graduate"]

            for label, prob in zip(labels, probabilities):
                st.write(f"{label}: {prob*100:.2f}%")

        except Exception as e:
            st.error(f"Error: {str(e)}")


# ==============================
# RUN APP
# ==============================
if __name__ == "__main__":
    main()