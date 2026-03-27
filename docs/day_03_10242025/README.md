# Hackathon – Day 3 Report

This repository presents a collection of modeling approaches developed during the **CAMM Hackathon** for predicting the **Coefficient of Thermal Expansion (CTE)** of materials.  
The work integrates **regression models**, **neural networks**, and **explainability techniques** to explore predictive performance and interpretability.

---

## ⚙️ Regression Models
Traditional regression algorithms were implemented to establish baseline performance.  
The models included:
- **Random Forest Regressor**  
- **Gradient Boosting Regressor**  
- **Ensemble comparisons** using R², MSE, and MAE metrics  

These methods served as reference models for evaluating the effects of more complex architectures.

---

## 🧠 Neural Network Models
Deep learning models were developed to capture nonlinear relationships in the dataset.  
Key elements:
- **Feedforward neural networks (MLP)** with multiple hidden layers  
- **Batch Normalization** and **Dropout** for improved stability and regularization  
- **AdamW optimizer** with learning rate scheduling  
- Grid search over **activation functions**, **learning rates**, and **hidden layer sizes**

---

## 🔍 Feature Importance
Feature importance analysis was conducted to identify the most relevant material descriptors for CTE prediction.  
Both statistical metrics and model-based rankings were used to interpret feature influence.

---

## 📊 SHAP Analysis
**SHAP (SHapley Additive exPlanations)** was applied to interpret model outputs.  
This helped visualize:
- Which structural and compositional features most impact CTE  
- How feature interactions contribute to model predictions  

---

## 🔗 Causal Analysis
Causal inference methods were explored to reveal underlying cause–effect relationships among material features and target properties.  
This approach aimed to identify true **drivers** rather than simple correlations.

---

## 🧩 Causal LLM
An experimental **Causal LLM** component was integrated to connect **language-model-based reasoning** with causal discovery.  
This hybrid framework allows combining **data-driven insights** with **contextual scientific understanding**, enhancing interpretability and hypothesis generation.

---

## 📘 Summary
This project demonstrates a multi-faceted approach to materials property prediction, combining:
- Traditional **machine learning** baselines  
- Advanced **deep learning** architectures  
- **Explainable AI** and **causal reasoning** frameworks  

Together, these methods provide both **high predictive accuracy** and **meaningful scientific insights** into material behavior.

---

