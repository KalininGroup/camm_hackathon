# Hackathon – Day 6 Report

## Overview  
Define a workflow to align SEM and AFM images by shared locations and use one modality as a proxy for the other where appropriate.

---

## Data Preparation  
Paired SEM and AFM images referenced to the same physical locations, with consistent scaling, orientation, and metadata.

---

## Modeling Approach  
Assume SEM as ground-truth topology. Use stochastic local matching between SEM and AFM patches to estimate and calibrate AFM tip shape.

---

## Evaluation  
Similarity metrics between predicted and measured AFM, consistency of calibrated tip shape across locations, and qualitative visual checks.

---

## Key Takeaways  
AFM and SEM can act as proxies for each other; stochastic matching enables practical AFM tip calibration using SEM.
