import streamlit as st
import joblib
import numpy as np

# -------------------------------
# Load Model and Scaler
# -------------------------------
@st.cache_resource
def load_model():
    model = joblib.load("concrete_strength_model.pkl")
    scaler = joblib.load("concrete_strength_scaler.pkl")
    return model, scaler

model, scaler = load_model()

# -------------------------------
# Prediction Function
# -------------------------------
def predict_concrete_strength(
    cement,
    blast_slag,
    fly_ash,
    water,
    superplasticizer,
    coarse_agg,
    fine_agg,
    age
):
    input_data = np.array([[
        cement,
        blast_slag,
        fly_ash,
        water,
        superplasticizer,
        coarse_agg,
        fine_agg,
        age
    ]])

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)

    return prediction[0]

# -------------------------------
# Streamlit UI
# -------------------------------
def main():

    st.set_page_config(
        page_title="Concrete Strength Predictor",
        page_icon="🏗️"
    )

    st.title("🏗️ Concrete Strength Predictor")
    st.write("Enter the concrete mix proportions below.")

    cement = st.number_input(
        "Cement (kg/m³)",
        min_value=0.0,
        value=540.0,
        step=0.1
    )

    blast_slag = st.number_input(
        "Blast Furnace Slag (kg/m³)",
        min_value=0.0,
        value=0.0,
        step=0.1
    )

    fly_ash = st.number_input(
        "Fly Ash (kg/m³)",
        min_value=0.0,
        value=0.0,
        step=0.1
    )

    water = st.number_input(
        "Water (kg/m³)",
        min_value=0.0,
        value=162.0,
        step=0.1
    )

    superplasticizer = st.number_input(
        "Superplasticizer (kg/m³)",
        min_value=0.0,
        value=2.5,
        step=0.1
    )

    coarse_agg = st.number_input(
        "Coarse Aggregate (kg/m³)",
        min_value=0.0,
        value=1040.0,
        step=0.1
    )

    fine_agg = st.number_input(
        "Fine Aggregate (kg/m³)",
        min_value=0.0,
        value=676.0,
        step=0.1
    )

    age = st.number_input(
        "Age (days)",
        min_value=1,
        value=28,
        step=1
    )

    if st.button("Predict Concrete Strength"):

        prediction = predict_concrete_strength(
            cement,
            blast_slag,
            fly_ash,
            water,
            superplasticizer,
            coarse_agg,
            fine_agg,
            age
        )

        st.success(
            f"Predicted Concrete Compressive Strength: {prediction:.2f} MPa"
        )

if __name__ == "__main__":
    main()