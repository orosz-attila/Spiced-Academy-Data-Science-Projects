## 07. Time Series Analysis: Temperature Forecast

<div align="justify">In this project, I applied the ARIMA model for a short-term temperature forecast. After visualizing the trend, the seasonality and the remainder of the time series data (daily mean temperature in Berlin-Treptow from 1979-2020), I run tests such as ADF and KPSS for checking stationarity (time dependence).</div><br> 

<div align="justify">For determining the parameters of the ARIMA model (p, d, q), I present two approaches:</div><br> 

  1. Inspecting the lags of the Autocorrelation (ACF) and Partial Auto Correlation Functions (PACF) plots. 
  2. Using alkaline-ml Auto-Arima process which automatically finds the most optimal order setting that has the lowest AIK. 

<div align="justify">The prediction with the tuned ARIMA model achieved a MAE score as low as 1.72.</div><br>

The notebook with plotly interactivy is also available on [Jupyter Colab](https://colab.research.google.com/drive/1nRPrfqCVFn-EHhl5GenxREuNRYeWV_h8#scrollTo=PynGYIu55aHb).<br>


Data source: [European Climate Assessment Dataset](https://www.ecad.eu).<br>
<br>