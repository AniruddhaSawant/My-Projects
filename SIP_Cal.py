#!/usr/bin/env python
# coding: utf-8

# In[1]:


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




