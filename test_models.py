#!/usr/bin/env python3
"""
Test script to verify model loading and prediction functionality
"""

import joblib
import os
import pandas as pd
import numpy as np

def test_model_loading():
    """Test if models can be loaded successfully"""
    MODEL_PATH = 'saved_models'

    print("🔍 Testing model loading...")

    try:
        print("Loading model A...")
        model_A = joblib.load(os.path.join(MODEL_PATH, 'stroke_model_A_original.pkl'))
        print("✅ Model A loaded successfully")

        print("Loading model B...")
        model_B = joblib.load(os.path.join(MODEL_PATH, 'stroke_model_B_synthetic.pkl'))
        print("✅ Model B loaded successfully")

        print("Loading feature info...")
        feature_info = joblib.load(os.path.join(MODEL_PATH, 'feature_info.pkl'))
        print("✅ Feature info loaded successfully")

        return model_A, model_B, feature_info

    except Exception as e:
        print(f"❌ Error loading models: {e}")
        return None, None, None

def prepare_test_features():
    """Prepare test features for prediction"""
    # Test data
    test_data = {
        'age': 65,
        'gender': 'Male',
        'hypertension': 1,
        'heart_disease': 0,
        'ever_married': 'Yes',
        'work_type': 'Private',
        'residence_type': 'Urban',
        'avg_glucose_level': 150.0,
        'bmi': 28.5,
        'smoking_status': 'formerly smoked'
    }

    # Encode categorical variables (same as in app.py)
    gender_map = {'Female': 0, 'Male': 1, 'Other': 2}
    married_map = {'No': 0, 'Yes': 1}
    work_map = {'Govt_job': 0, 'Never_worked': 1, 'Private': 2, 'Self-employed': 3, 'children': 4}
    residence_map = {'Rural': 0, 'Urban': 1}
    smoking_map = {'Unknown': 0, 'formerly smoked': 1, 'never smoked': 2, 'smokes': 3}

    # Extract values
    age = float(test_data['age'])
    gender = gender_map.get(test_data['gender'], 0)
    hypertension = int(test_data['hypertension'])
    heart_disease = int(test_data['heart_disease'])
    ever_married = married_map.get(test_data['ever_married'], 0)
    work_type = work_map.get(test_data['work_type'], 2)
    residence_type = residence_map.get(test_data['residence_type'], 1)
    avg_glucose_level = float(test_data['avg_glucose_level'])
    bmi = float(test_data['bmi'])
    smoking_status = smoking_map.get(test_data['smoking_status'], 0)

    # Feature engineering
    age_glucose_interaction = age * avg_glucose_level
    age_bmi_interaction = age * bmi
    glucose_bmi_interaction = avg_glucose_level * bmi

    # Age group
    if age <= 18: age_group = 0
    elif age <= 35: age_group = 1
    elif age <= 50: age_group = 2
    elif age <= 65: age_group = 3
    else: age_group = 4

    # BMI category
    if bmi < 18.5: bmi_category = 0
    elif bmi < 25: bmi_category = 1
    elif bmi < 30: bmi_category = 2
    else: bmi_category = 3

    # Glucose category
    if avg_glucose_level < 100: glucose_category = 0
    elif avg_glucose_level < 126: glucose_category = 1
    elif avg_glucose_level < 200: glucose_category = 2
    else: glucose_category = 3

    # Risk score
    risk_score = (int(age > 50) + hypertension + heart_disease +
                  int(avg_glucose_level > 126) + int(bmi > 30) +
                  int(smoking_status == 3))

    # Create feature DataFrame
    features = pd.DataFrame({
        'gender': [gender],
        'hypertension': [hypertension],
        'heart_disease': [heart_disease],
        'ever_married': [ever_married],
        'work_type': [work_type],
        'residence_type': [residence_type],
        'avg_glucose_level': [avg_glucose_level],
        'bmi': [bmi],
        'smoking_status': [smoking_status],
        'bmi_missing': [0],
        'age': [age],
        'age_glucose_interaction': [age_glucose_interaction],
        'age_bmi_interaction': [age_bmi_interaction],
        'glucose_bmi_interaction': [glucose_bmi_interaction],
        'age_group': [age_group],
        'bmi_category': [bmi_category],
        'glucose_category': [glucose_category],
        'risk_score': [risk_score]
    })

    return features, test_data

def test_prediction(model_A, model_B, feature_info, features):
    """Test prediction with loaded models"""
    print("\n🔍 Testing prediction...")

    try:
        # Reorder columns to match training data if feature_info is available
        if feature_info and 'feature_names' in feature_info:
            features = features[feature_info['feature_names']]
            print(f"✅ Features reordered to match training data: {len(feature_info['feature_names'])} features")

        print(f"Feature shape: {features.shape}")
        print(f"Feature columns: {list(features.columns)}")

        # Make predictions
        print("Making prediction with Model A...")
        prob_A = float(model_A.predict_proba(features)[0][1])
        print(f"✅ Model A prediction: {prob_A:.4f}")

        print("Making prediction with Model B...")
        prob_B = float(model_B.predict_proba(features)[0][1])
        print(f"✅ Model B prediction: {prob_B:.4f}")

        # Ensemble prediction
        ensemble_prob = (prob_A + prob_B) / 2
        print(f"✅ Ensemble prediction: {ensemble_prob:.4f}")

        return True

    except Exception as e:
        print(f"❌ Error during prediction: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    print("🧠 Stroke Prediction Model Test")
    print("=" * 40)

    # Test model loading
    model_A, model_B, feature_info = test_model_loading()

    if model_A is None or model_B is None:
        print("❌ Models failed to load. Cannot continue testing.")
        return

    # Test feature preparation
    print("\n🔍 Testing feature preparation...")
    features, test_data = prepare_test_features()
    print("✅ Test features prepared")
    print(f"Test data: {test_data}")

    # Test prediction
    success = test_prediction(model_A, model_B, feature_info, features)

    if success:
        print("\n🎉 All tests passed! Models are working correctly.")
    else:
        print("\n❌ Prediction test failed.")

if __name__ == "__main__":
    main()