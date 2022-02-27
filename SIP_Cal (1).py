#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# SIP Cal


pmt = int(input('SIP Amt Per Month- '))
rate_tens = str(input('Expected Rate of Int- '))
years = int(input('Number of Years- '))

rate_float = float(rate_tens)
rate = (rate_float/12)/100
months = years*12

SIP_Amt = (pmt*(((1 + rate)**months-1)/rate*(1+rate)))
Invested_Amt = pmt*months
earning = SIP_Amt - Invested_Amt

print ('Total Value after', years, 'years will be RS.', SIP_Amt)
print ('Total Invested Capital = RS.', Invested_Amt)
print ('Tota earnings = RS.', earning)


# In[ ]:


# Mutual Fund Cal


pv = int(input('One time invested Value - '))
rate_ten = str(input('Expected Rate of Int - '))
Nu_years = int(input('Number of Years - '))

INT_I = float(rate_ten)
INT = INT_I/100

MF_earning = (pv*(1+INT)**Nu_years)
earnings = MF_earning - pv

print ('Total Invested Value is =', pv)
print ('Total Investment is =', MF_earning)
print ('Total Earnings =', earnings)


# In[ ]:


# Equity Returns


buy = int(input('Buying Price - '))
sell = int(input('Selling Price - '))
div = int(input('Dividend - '))
stock = int(input('Number of Stocks - '))

buy_val = buy * stock
sell_val = sell * stock


returns = (((sell - buy) + div )/buy)*100
profit = sell_val - buy_val + div

print ('Your total Returns on Equity is', returns, '%')
print ('Toal Profit of RS.', profit)
print ('Total Investment = ', buy_val)


# In[ ]:




