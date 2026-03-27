# Dataset Description: MFM Image Analysis

## 📁 Overview
This dataset contains **Magnetic Force Microscopy (MFM)** images collected for AuCoNi combinatorial library.  
The primary purpose of this dataset is to **analyze surface topography and magnetic domain structures** in order to extract meaningful quantitative features.

---

## 📂 Data Contents
Each sample in the dataset includes the following **image channels**:

- **AFM Height Channel (`AFM_height`)**  
  Represents the sample’s surface **topography** in nanometers.
  
- **AFM Amplitude / Phase / Z-Sensor Channels**  
  Capture the mechanical response and phase-shift signals from the AFM tip–sample interaction.  
  These channels are mainly used for complementary surface information.

- **MFM Channel (`MFM`)**  
  Provides contrast for **magnetic domains** and field distribution at the nanoscale.

---

## 🧾 Metadata
Alongside the images, the dataset also includes:
- **Positions**: The spatial coordinates of each scan region.

---

## 🎯 Objective of Analysis
The focus of this dataset is to correlate:
- **Surface topography (AFM height)**  
- **Magnetic domain structures (MFM)**  

## 🎯 Objective of Analysis

The objective is to **analyze the spatial grid of scans** to understand **how the sample’s properties are distributed across the grid** with respect to key features in the structure.

---

## 🧪 Planned Feature Extraction
We will create a **Bag-of-Features (BoF)** representation for this dataset.  
The extracted features will include, but are not limited to:

- **Surface Roughness** – derived from height images  
- **Magnetic Domain Size & Shape** – from the MFM pahse channel  
- **Domain Intensity / Contrast** – pixel-level magnetic signal strength  
- **Particle Size Distribution** – from segmentation of topographic 
- **Texture and Orientation Metrics** – using filters (e.g., Gabor filters)  
- **Statistical Descriptors** – mean, variance, skewness, kurtosis of pixel values  
- **Edge Density & Boundary Roughness** – characteristics of domain boundaries  
- **Frequency-Domain Features** – FFT-based periodicity and roughness  
- **Other Derived Metrics** 

## 📜 Citation
Please Do not include this dataset or any derived results in publications without prior written permission from the data owners.

