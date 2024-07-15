# Crab Age Prediction

## Introduction
This project focuses on predicting the age of crabs from physical measurements and other derived features. Using machine learning techniques, the goal is to accurately estimate crab age, which is crucial for ecological research and fisheries management.


Data Dictionary
Variable	Description
# Crab Measurements

<img src = '../images/Measurement-of-width-and-length-of-crab-Source-FAO.png' alt = 'https://www.researchgate.net/figure/Measurement-of-width-and-length-of-crab-Source-FAO_fig2_316495313'>


## Data Dictionary

| Column Name      | Data Type   | Description                                                |
|------------------|-------------|------------------------------------------------------------|
| id               | integer     | The identification number of the crab species              |
| Sex              | Categorical | M for Male; F for Female; I for Intersex                     |
| Length           | float       | Measured from the front (eye) carapace to the tail  (feet)        |
| Diameter         | float       | Measured from one side of the carapace to the other  (feet)|
| Height           | float       | Measured from the base of the body to the top     (feet)          |
| Weight           | float       | The overall weight of the crab (ounces)                            |
| Shucked Weight   | float       | The weight of 'meat' (ounces)                                      |
| Viscera Weight   | float       | The weight of the internal organs (ounces)                          |
| Shell Weight     | float       | The weight of the shell (ounces)                                   |
| shell_weight_ratio | float    | Ratio of shell weight to total weight                |
| shucked_weight_ratio | float    | Ratio of meat weight to total weight after shucking                |
| vis_shucked_weight_ratio | float    | Ratio of viscera weight to shucked weight                |
| surface_area | float    | Calculated based on the approximated surface area using the crab's length and diameter                |
| Age              | integer     | The target variable and the age of the crab                |


## Model Choice
The choice of model was determined after evaluating several baseline models including `Random Forest`, `K-Nearest Neighbors`, `Support Vector Regression (SVR)`, `CatBoost`, `LightGBM`, and `XGBoost`. Feature engineering was applied to improve model performance, introducing new features based on the physical characteristics of the crabs: `shell_weight_ratio`, `shucked_weight_ratio`, `vis_shucked_weight_ratio`, `surface_area`.

## Results
XGBoost was selected due to its superior performance and efficiency in handling both linear and non-linear relationships in data. It has better scores `MSE` and `R2` relative to the other models, even though, the `MAE` scores were on comparable with other models such as `Random Forest`.
