# Hackathon – Day 1 Report

## Overview  
On the first day of the hackathon we explored a **materials-science dataset of rare-earth samples**.  
Each record in the dataset corresponds to a point on a two-dimensional experimental grid (`x`, `y`) and contains about a dozen **measured physical and structural properties**—for example, thermal conductivity, lattice-related parameters, entropy, disorder measures, and other derived features obtained from X-ray or diffraction analyses.  
Our main objective was to **predict one key property of interest** (the “target”) from the remaining features, which makes this a **regression problem**.

---

## Data Preparation  
We began by inspecting the raw table (≈ 2,600 rows × 17 columns), checking for missing or non-numeric values.  
All relevant columns were converted to numeric types and any rows lacking a target value were removed.  
We then split the data into **training** and **validation** subsets to allow fair model assessment.  
Since many features were on different scales, we also experimented with **normalization/standardization** to improve model performance.

---

## Modeling Approach  
Our first step was to **survey a variety of regression algorithms** to understand which approaches capture the relationship between the materials’ features and the target property.  
We started with a **simple linear regression** baseline to gauge how well a straight-line relationship could explain the data.  
We then evaluated **more flexible, non-linear regressors**—such as tree-based ensemble methods—to see whether they could capture complex patterns missed by the linear model.

---

## Evaluation  
To compare models, we used **R² scores** (to measure how much of the variance in the target is explained) and **RMSE** (to measure typical prediction error in the target’s original units).  
We also employed **cross-validation** to reduce the risk of over-fitting and to assess the models’ generalization.  
Visualization was a central part of Day 1: we plotted predictions back on the experimental `(x, y)` grid to spot spatial trends and compared them with the ground-truth measurements.

---

## Key Takeaways  
Day 1’s work gave us:
- A clean, structured dataset ready for further modeling.  
- Baseline performance metrics to benchmark future improvements.  
- Insight into which features appear most influential for prediction.  
- Early evidence that more sophisticated models may outperform the linear baseline on this problem.

