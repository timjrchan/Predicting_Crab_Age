<img src = "https://img.freepik.com/free-vector/smiling-pink-crab-cartoon-sticker_1308-76561.jpg?t=st=1721051674~exp=1721055274~hmac=f17fb49d0d6838c10a7600abde3fa51b3bf38fb2aef83ed503d159e72cea23e8&w=826" style="float: left; margin: 40px; height: 100px">

# Crab Age Prediction

## Introduction
This project is part of our participation in the Kaggle competition aimed at predicting the age of crabs using various measurements. The primary objective is to develop a machine learning model that can achieve the lowest Mean Absolute Error (MAE) score. The details and datasets for the competition are hosted on [Kaggle](https://www.kaggle.com/competitions/playground-series-s3e16/overview).

## Motivation
Our motivation for joining this competition is to apply and enhance our machine learning skills in a practical, competitive environment. By tackling this challenge, we aim to explore advanced feature engineering techniques and optimize machine learning algorithms to produce a model with high accuracy and robustness. This competition provides a platform to benchmark our approach against a community of data scientists, offering valuable insights and feedback.


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
