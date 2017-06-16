import numpy as np
import pandas as pd
# import pandas.io.data as web
from numpy import *
from math import *

"""
Chapter 01 - "Why Python?"
"""
#===============================================================================
#  Quick Example of a European Call Option
S0 = 100.
K = 105.
T = 1.0
r = 0.05
sigma = 0.2

I = 100000

random.seed(1000)
z = random.standard_normal(I)
ST = S0 * exp(r * T + sigma * sqrt(T) * z)
hT = maximum(ST - K, 0)
CO = exp(-r * T) * sum(hT) / I

print "Value of European Call Option %5.3f" % CO
#===============================================================================
# goog = web.DataReader('GOOG', data_source='google',
#                               start='3/14/2009',
#                               end='4/14/2014')
#
# goog.index_name = u'Date'
# goog.tail()
#
# goog['Log_Ret'] = np.log(goog['Close'] / goog['Close'].shift(1))
# goog['Volatility'] = pd.rolling_std(goog['Log_Ret'], window=252) * np.sqrt(252)
#
# goog[['Close', 'Volatility']].plot(subplots=True,
#                                    color='blue',
#                                    figsize=(8,6),
#                                    grid=True)



#===============================================================================
#
# def f(x):
#     return 3 * log(x) + cos(x) ** 2
#
# r = [f(x) for x in a]
#
#
# a = np.arange(1, loops)
#
# import numexpr as ne
# ne.set_num_threads(1)
# f = '3 * log(a) + cos(a) ** 2'
# r = ne.evaluate(f)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#



#===============================================================================
#===============================================================================
#===============================================================================
#===============================================================================
#===============================================================================
#===============================================================================
#===============================================================================
#===============================================================================
