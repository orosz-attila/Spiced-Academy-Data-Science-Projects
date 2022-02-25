<div align="justify">The goal of this project is to build a regression model, in order to predict the total number of rented bycicles in each hour based on time and weather features, optimizing the accuracy of the model for RMSLE, using Kaggle's "Bike Sharing Demand" dataset that provides hourly rental data spanning two years.</div><br> 

<div align="justify">After extracting datetime features, highly correlated variables were dropped via feature selection (correlation analysis, Variance Inflation Factor) to avoid multicollienarity. I compared more linear regression models with one another (PossionRegressor, PolinomialFeatures, Lasso, Ridge, RandomForestRegressor) based on R2 and RMSLE scores. After evaluating the different models, I kept the RandomForestRegressor, and applied GridSearchCV and cross validation to ensure the best fit, finally submitted the predictions with 0.47210 RMSLE.</div><br>

The notebook of this project is available [here](https://github.com/orosz-attila/Spiced-Academy-Data-Science-Projects/blob/master/03_regression_bycicle_rental_prediction/03_project_bycicle_rental_forecast.ipynb).


Data source: [Kaggle: Bike Sharing Demand](https://www.kaggle.com/c/bike-sharing-demand/data).<br>