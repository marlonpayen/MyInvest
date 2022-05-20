'''
Created on 13 May 2022

@author: mpayen
'''

class PortfolioTransactions(object):
    '''
    classdocs
    '''


    def __init__(self, type_transaction, stock_name, company_name, number_shares, price_share, currency, currency_exchange, total_amount_shares, currency_fee):
        '''
        Constructor
        '''
        self.type_transaction = type_transaction
        self.stock_name = stock_name
        self.company_name = company_name
        self.number_shares = number_shares
        self.price_share = price_share
        self.currency = currency
        self.currency_exchange = currency_exchange
        self.total_amount_shares = total_amount_shares
        self.currency_fee = currency_fee
        