# Super Simple Stock Market
Code to calculate metrics for given stocks

## Description
The code will :

- For a given stock, 
    - Given any price as input, calculate the dividend yield
    - Given any price as input, calculate the P/E Ratio
    - Record a trade, with timestamp, quantity of shares, buy or sell indicator and price
    - Calculate Volume Weighted Stock Price based on trades recorded in past 15 minutes
- Calculate the GBCE All Share Index using the geometric mean of prices for all stocks

## Requirements

- Python 3.x (tested on 3.10)

## Run
- python stock_market.py

#### Code summary:
- Stock class is created which will calculate dividend yield, pe ratio, record trade and calculate volume weighted stock price
- Method cal_pe_ratio will calculate pr ratio using the formula provided
- Method cal_dividend_yield will calculate dividend yielded using the formula
- Method record_trade will record the quantity of stocks bought or sold for a given time
- Method cal_vol_weight_sp will calculate volume weighted stock on trades in past 15 mins
- GBCE class is created which will calculate all share index using the method cal_all_share_index and using geomentric mean method : cal_geomentric_mean

## Author
Prerna Pratik
