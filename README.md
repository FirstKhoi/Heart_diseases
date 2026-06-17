# Heart Disease Risk Predictor 🫀

A machine learning-powered web application that predicts the 10-year risk of coronary heart disease (CHD) based on clinical patient data.

## Overview

This project leverages a trained machine learning model to assess cardiovascular disease risk using key clinical parameters. The application provides an interactive interface built with Streamlit, making it accessible for healthcare professionals to quickly evaluate patient risk profiles.

## 🚀 Demo App

Try the live demo application here:
### [Heart Disease Risk Predictor - Live Demo]([https://heartdiseasespredictionbykhoi.streamlit.app/](https://heartdiseasespredictionbykhoi.streamlit.app/))

Hosted on Streamlit Cloud for easy access without local installation.

## Features

- 🎯 **10-Year CHD Risk Prediction** - Estimates the probability of coronary heart disease within 10 years
- 📊 **Interactive Patient Input** - User-friendly sidebar interface for entering patient clinical data
- 🔬 **Machine Learning Model** - XGBoost-based model trained on cardiovascular health data
- ⚠️ **Risk Classification** - Automatic categorization of risk as HIGH or LOW based on optimal threshold
- 📈 **Feature Engineering** - Advanced features including Pulse Pressure and Age-Cigarettes interaction
- 💾 **Cached Model** - Fast loading and inference using model caching

## Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd Heart_diseases
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit application:
```bash
streamlit run app.py
```

The application will launch in your default web browser at `http://localhost:8501`.

### How to Use

1. **Enter Patient Information** in the sidebar:
   - **Age**: Patient's age (30-100 years)
   - **Gender**: Select Male or Female
   - **Cigarettes per Day**: Daily cigarette consumption (0-60)
   - **Systolic BP (sysBP)**: Systolic blood pressure in mmHg (80-250)
   - **Diastolic BP (diaBP)**: Diastolic blood pressure in mmHg (50-150)
   - **Total Cholesterol**: Total cholesterol level (100-500 mg/dL)
   - **Glucose Level**: Blood glucose level (40-400 mg/dL)

2. **Click "🔍 Predict Risk"** button to generate the assessment

3. **Review Results**:
   - **HIGH RISK**: Probability ≥ 45% - Immediate medical consultation recommended
   - **LOW RISK**: Probability < 45% - Maintain healthy lifestyle and routine check-ups

## Model Details

### Features Used
- Demographics: Age, Gender
- Lifestyle: Cigarette consumption, Education level
- Medical History: Current smoking status, History of stroke, Hypertension, Diabetes
- Clinical Measurements: Blood pressure (systolic & diastolic), Total cholesterol, Glucose level, BMI, Heart rate
- Derived Features: Pulse Pressure, Age-Cigarettes interaction

### Optimal Threshold
- The model uses an **optimal threshold of 0.45** (45%) determined via Youden's J statistic for better classification performance

### Model Type
- **XGBoost** gradient boosting classifier trained on cardiovascular health data

## Technical Stack

- **Python 3** - Programming language
- **Streamlit** - Web application framework
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing
- **Scikit-learn** - Machine learning utilities
- **XGBoost** - Gradient boosting model
- **Joblib** - Model serialization and caching

## File Structure

```
Heart_diseases/
├── README.md                    # Project documentation
├── app.py                       # Main Streamlit application
├── requirements.txt             # Python dependencies
└── heart_disease_model.pkl      # Pre-trained ML model
```

## Model Performance

The model was trained on clinical cardiovascular data and optimized using Youden's J statistic to find the best threshold for distinguishing between high and low-risk patients.

## Important Disclaimer ⚠️

**This application is for educational and research purposes only.**

- Predictions should **not** replace professional medical advice
- Always consult with qualified healthcare professionals for accurate diagnosis
- Results are probabilistic estimates based on training data
- Individual risk factors may vary based on additional clinical information

## Requirements

See `requirements.txt` for all dependencies:
- streamlit
- pandas
- numpy
- scikit-learn
- xgboost
- joblib

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests to improve the application.

## License

This project is open source and available under the MIT License.

## Author

Created by FirstKhoi

## Support

For questions or issues, please open an issue in the repository.

---

**Note**: This tool predicts 10-year coronary heart disease risk based on the Framingham Heart Study model and clinical parameters provided.
