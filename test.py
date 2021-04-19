import pandas as pd
portfolio = pd.DataFrame(columns=['Date', 'Investment', 'Return/Loss', 'Balance'])
interest_rate = 0.1
monthly_deposit = 500

dates = pd.date_range(start="3-31-2021", periods=240, freq='1m')
investment = [monthly_deposit]*len(dates)
return_losses = []
balances = []
balance_at_end = 0
current_balance = 500
for date in dates:
    current_return_loss = (0.121/12)*current_balance
    return_losses.append(round(current_return_loss,2))
    balances.append(round(current_balance + current_return_loss))
    current_balance += (current_return_loss + monthly_deposit)

portfolio['Date'] = pd.to_datetime(dates)
portfolio['Investment'] = investment
portfolio['Return/Loss'] = return_losses
portfolio['Balance'] = balances

balance_at_end = balances[-1]

print(portfolio.head(10))

        Date  Investment  Return/Loss  Balance
0 2021-03-31         500         5.04      505
1 2021-04-30         500        10.13     1015
2 2021-05-31         500        15.28     1530
3 2021-06-30         500        20.47     2051
4 2021-07-31         500        25.72     2577
5 2021-08-31         500        31.02     3108
6 2021-09-30         500        36.38     3644
7 2021-10-31         500        41.79     4186
8 2021-11-30         500        47.25     4733
9 2021-12-31         500        52.77     5286
