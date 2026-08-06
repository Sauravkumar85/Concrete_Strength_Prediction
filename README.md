# 🏗️ Concrete Compressive Strength Prediction using Machine Learning

## Project Overview

This project uses **Machine Learning** to predict the **compressive strength of concrete** based on its mix composition and curing age. The application is developed using **Python**, **XGBoost**, and **Streamlit**, allowing users to enter concrete mix proportions and instantly obtain the predicted compressive strength.

The project combines concepts from **Civil Engineering (Concrete Technology)** and **Machine Learning** to provide a fast and reliable prediction tool that can assist engineers during the preliminary mix design stage.

---

## Features

* 🏗️ Predicts concrete compressive strength (MPa).
* 🤖 Machine Learning model developed using **XGBoost Regressor**.
* 📊 Data preprocessing using **StandardScaler**.
* 📈 Exploratory Data Analysis (EDA) to understand feature relationships.
* 📉 Model evaluation using regression metrics.
* 💻 Interactive web application built with **Streamlit**.
* 🚀 Ready for deployment on **Streamlit Community Cloud**.

---

## Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Joblib
* Matplotlib
* Seaborn

---

## Dataset

The project uses the **Concrete Compressive Strength Dataset** from the **UCI Machine Learning Repository**.

### Dataset Information

* Total Samples: **1030**
* Input Features: **8**
* Target Variable: **Concrete Compressive Strength (MPa)**

### Input Features

| Feature            | Unit  |
| ------------------ | ----- |
| Cement             | kg/m³ |
| Blast Furnace Slag | kg/m³ |
| Fly Ash            | kg/m³ |
| Water              | kg/m³ |
| Superplasticizer   | kg/m³ |
| Coarse Aggregate   | kg/m³ |
| Fine Aggregate     | kg/m³ |
| Age                | Days  |

**Target**

* Concrete Compressive Strength (MPa)

---

## Project Workflow

1. Dataset Collection
2. Data Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Scaling
5. Model Training
6. Model Evaluation
7. Model Serialization using Joblib
8. Streamlit Web Application
9. Deployment

---

## Project Structure

```text
ConcreteStrengthPrediction/

│── dataset/
│── notebook/
│── streamlit_app.py
│── concrete_strength_model.pkl
│── concrete_strength_scaler.pkl
│── requirements.txt
│── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ConcreteStrengthPrediction.git
```

Move into the project folder

```bash
cd ConcreteStrengthPrediction
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run streamlit_app.py
```

The application will open automatically in your browser.

---

## How to Use

1. Enter the concrete mix proportions.
2. Enter the curing age (days).
3. Click **Predict Concrete Strength**.
4. View the predicted compressive strength in **MPa**.

---

## Model

The final prediction model is developed using:

* XGBoost Regressor

The model is trained using standardized input features and saved using **Joblib** for efficient loading during prediction.

---

## Future Improvements

* Compare multiple regression models.
* Hyperparameter tuning.
* Feature importance visualization.
* SHAP explainability.
* Batch prediction using CSV upload.
* Concrete mix optimization based on target strength.

---

## Deployment

The application can be deployed easily using **Streamlit Community Cloud**.

Live Demo:

https://concretestrengthprediction-4yys5qbdewfkgpzcxdobdj.streamlit.app/

---

## Repository

GitHub Repository:

Sauravkumar803213

---

## Author

**Saurav Kumar**

B.Tech Civil Engineering

National Institute of Technology Warangal

---

## License

This project is licensed under the MIT License.
