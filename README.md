In this work, we build and estimate a portfolio multifactor risk  model from two perspectives: Time Series Risk Models and PCA (Principal Components Analysis) Risk Models.

- For the Time Series Risk Models, we use the Fama and French 5-factor model. The latter is considered as a benchmark portfolio that includes return time series of five potential drivers of volatility: RM (Market Return), SMB (Small Minus Big), HML (High Minus Low), RMW (Robust Minus Weak) and CMA (Conservative Minus Aggressive). 

- For the PCA Risk model approach, the goal is to reduce the dimensionality of our dataset (asset returns time series) by identifying the directions that explain the maximum amount of variance. This involves creating a new vector basis that captures the highest volatility in the data. The greater the variance of the dataset along a given direction, the larger the dispersion of the data along that direction, indicating a higher risk exposure of the portfolio in that direction. Using PCA and matrix transformations, we compute latent variables that represent potential drivers of risk (risk factors) in those directions. The factor exposures are the new vector basis, and the specific returns are deduced from matrix transformations on the original returns time series, factor exposures, and risk factors.


This task is very important in the sense that it is usually a necessary preliminary task before moving towards portfolio optimization.
