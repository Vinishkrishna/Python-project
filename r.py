#import the python libraries
from pandas_datareader import data as web
import pandas as pd 
import numpy as np 
import datatime
import matplotlib.pyplot as plt 
import PyPortfolioOpt
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns
from pypfopt.discrete_allocation import DisceteAllocation,get_latest_prices
plt.style.use('fivethirtyeight')
#get the stock symbols or tickets in the portfolio
#FAANG
assets=['FB','AMZN','AAPL','NFLX','GOOG']
#Assign weights to a stocks.
weights=np.array([0.2,0.2,0.2,0.2,0.2])
#Get the stock/portfolio starting date
stockStart='2013-01-01'
#Get the stocks ending date(today)
today=datatime.today().strftime('%Y-%m-%d')
#Create a dataframe to store the adjusted close proce of the stocks
df=pd.DataFrame()
#Store the adjused close price of the stock into the df
for stock in assets:
    df[stock]=web.DataReader(stock,data_source='yahoo',start=stockStartDate,end=today)['Adj Close']
#show the df
#df
#Create and plot the graph
for c in my_stocks.columns.values:
    plt.plot(my_stocks[c],label=c)
    
plt.title(title)
plt.xlabel('Date',fontsize=18)
plt.ylabel('Adj. Price USD($)',fontsize=18)
plt.legend(my_stocks.columns.values,loc='upper left')
plt.show()
#Show the daily simple return
returns=df.pct_change()
#returns
#create and show the annualized covariance matrix
cov_matrix_annual=returns.cov()*252
#cov_matrix_annual
port_variance=np.dot(weights.T,np.dot(cov_matrix_annual,weights))
#port_variance
#Calculate the portfolio volatility aka standard deviation
port_volatility=np.sum(returns.mean()*weights)*252
#port_volatility
#Calculate the annual portfolio return
portfolioSimpleAnnualReturn=np.sum(returns.mean()*weights)*252
#portfolioSimpleAnnualReturn
#Show the expected annual reurn,volatility(risk),and variance
percent_var=str(round(port_variance,2)*100)+'%'
percent_vols=str(round(port_volatility,2)*100)+'%'
percent_ret=str(round(portfolioSimpleAnnualReturn,2)*100)+'%'

print('Expected annual return:'+percent_ret)
print('Annual volatility/risk:'+percent_vols)
print('Annual variance:'+percent_var)
#portfolio optimization!
#calculate the expected returns and the annualised matrix of asset returns
mu=expected_returns.mean_historical_return(df)
S=risk_models.sample_cov(df)
#optimize for max sharpe ratio
ef=EfficientFrontier(mu,S)
weights=ef.max_sharpe()
cleaned_weights=ef.clean_weights()
print(cleaned_weights)
#ef.portfolio_performance(verbose=True)
#Get the discrete allocation of each share per stock
latest_prices=get_latest_prices(df)
weights=cleaned_weights
da=DisceteAllocation(weights,latest_prices,total_portfolio_value=15000)
allocation,leftover=da.lp_portfolio()
print('Discrete allocation:',allocation)
print('Funds remaining: ${:.2f}'.format(leftover))