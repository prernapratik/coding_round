from datetime import datetime, timedelta


class Stock:
    def __init__(self, last_dividend, fixed_dividend, par_value):
        self.last_dividend = last_dividend
        self.fixed_dividend = fixed_dividend
        self.par_value = par_value
        self.trades_list = []

    def cal_pe_ratio(self,price):
        return price / self.last_dividend

    def cal_dividend_yield(self,price):
        if self.fixed_dividend is None:
            return round(self.last_dividend / price, 2)
        else:
            return round((self.fixed_dividend * self.par_value) / price, 2)

    def record_trade(self, buy_sell_ind, quantity, price):
        timestamp = datetime.now()
        self.trades_list.append((timestamp, buy_sell_ind, quantity, price))

    def cal_vol_weight_sp(self):
        cur_time = datetime.now()
        total_price_qty = 0
        total_qty = 0
        for trade in self.trades_list:
            timestamp, _, quantity, price = trade
            if cur_time - timestamp <= timedelta(minutes=15):
                total_price_qty += price * quantity
                total_qty += quantity
            if total_qty == 0:
                return 0
            return total_price_qty / total_qty


def cal_geometric_mean(prices):
    prod = 1
    for price in prices:
        prod *= price
    return prod ** (1/len(prices))


class GBCE:
    def __init__(self):
        self.stocks_lst = []

    def add_stocks(self, stock):
        self.stocks_lst.append(stock)

    def cal_all_share_index(self):
        price_lst = [stock.cal_vol_weight_sp() for stock in self.stocks_lst
                     if stock.cal_vol_weight_sp() != 0]
        return cal_geometric_mean(price_lst)

"""stock instance creation"""
stock_tea = Stock(8, None, 150)
stock_pop = Stock(8, 0.02, 100)

"""GBCE instance creation"""
gbce = GBCE()

"""adding stocks"""
gbce.add_stocks(stock_tea)
gbce.add_stocks(stock_pop)

"""record trades for respective stocks"""
stock_tea.record_trade(True, 10, 45)
stock_tea.record_trade(False, 5, 60)
stock_pop.record_trade(True, 8, 70)
stock_pop.record_trade(False, 15, 80)

"""Printing the desired values"""
print(f"Dividend Yeild (TEA) : {stock_tea.cal_dividend_yield(20)}")
print(f"Dividend Yeild (POP) : {stock_pop.cal_dividend_yield(30)}")
print(f"P/E Ratio (TEA) : {stock_tea.cal_dividend_yield(10)}")
print(f"P/E Ratio (POP) : {stock_pop.cal_dividend_yield(50)}")
print(f"Volume weighted stock price (TEA) : {stock_tea.cal_vol_weight_sp()}")
print(f"Volume weighted stock price (POP) : {stock_pop.cal_vol_weight_sp()}")
print(f"GBCE All Share Index : {gbce.cal_all_share_index()}")
