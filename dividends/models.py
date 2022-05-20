from django.db import models
from django.core.exceptions import ValidationError
import operator

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    stock_name = models.CharField(max_length=10)
    year_of_foundation = models.CharField(max_length=4)

class Stock(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=9, decimal_places=2)
    number_of_shares = models.DecimalField(max_digits=15, decimal_places=10)
    currency = models.CharField(max_length=20)
    
class Transaction(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    stock = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    total_amount = models.DecimalField(max_digits=9, decimal_places=2)
    number_of_shares = models.DecimalField(max_digits=15, decimal_places=10)
    currency = models.CharField(max_length=20)
    
class Dividend(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=9, decimal_places=2)
    
class Portfolio_File(models.Model):
    data = models.FileField()

    def save(self, *args, **kwargs):
        super(Portfolio_File, self).save(*args, **kwargs)
        
        # List which will contain all the transactions defined as dictionaries
        list_portfolio_transactions = []
        keys = ["type_transaction","stock_name","company_name","number_shares","price_share","currency","currency_exchange","total_amount_shares","currency_fee"]
        
        # Read content of the file, instanciating object with all the date needed and creating a sorted list of all those portfolio transactions objects
        for portfolio_transaction in self.data:
            portfolio_transactions_split = portfolio_transaction.decode("utf-8").split(',') # Decode and split the bytes field self.data into a delimited string
            tmp_dict = {} # Temporary dictionary that will contain the details fetched from the file and be added to a list of dictionaries
            
            # Fetch fields needed from the CSV file that will be used to create the portfolio of owned stocks
            type_transaction = portfolio_transactions_split[0]
            stock_name = portfolio_transactions_split[3]
            company_name = portfolio_transactions_split[4]
            number_shares = portfolio_transactions_split[5]
            price_share = portfolio_transactions_split[6]
            currency = portfolio_transactions_split[7]
            currency_exchange = portfolio_transactions_split[8]
            total_amount_shares = portfolio_transactions_split[10]
            currency_fee = portfolio_transactions_split[17]
            
            # Fetch stocks bought and sold to reconcile the total amount owned by the account holder and add those to the list of dictionaries
            if type_transaction == 'Market buy' or type_transaction == 'Market sell' :
                tmp_dict[keys[0]] = type_transaction
                tmp_dict[keys[1]] = stock_name
                tmp_dict[keys[2]] = company_name
                tmp_dict[keys[3]] = number_shares
                tmp_dict[keys[4]] = price_share
                tmp_dict[keys[5]] = currency
                tmp_dict[keys[6]] = currency_exchange
                tmp_dict[keys[7]] = total_amount_shares
                tmp_dict[keys[8]] = currency_fee  
            
                list_portfolio_transactions.append(tmp_dict)
            
        list_portfolio_transactions.sort(key=operator.itemgetter('company_name')) # Sort list of dictionaries based on the company name to treat company by company
        portfolio_transaction_tmp = list_portfolio_transactions[0] # Temporary variable to store the previous portfolio transaction to be able to compare with the next one in the loop
        i = 0 # Used to fetch the previous portfolio transaction when applicable and compare it with the current one
        
        for portfolio_transaction in list_portfolio_transactions :
            print(list_portfolio_transactions[i-1])
            print(portfolio_transaction_tmp)
            if i > 1:
                portfolio_transaction_tmp = list_portfolio_transactions[i-1] #Temporary variable to store the previous portfolio transaction to be able to compare with the next one in the loop
        
            # As the list is sorted, if the previous and the current transaction are not for the same company, the current company needs to be added to the database
            print("tmp : " + portfolio_transaction_tmp.get("company_name") + "current : " + portfolio_transaction.get("company_name"))
            
            if portfolio_transaction_tmp.get("company_name") != portfolio_transaction.get("company_name") :
                # Fetch fields needed from the CSV file that will be used to create the portfolio of owned stocks
                type_transaction = portfolio_transaction.get("type_transaction")
                stock_name = portfolio_transaction.get("stock_name")
                company_name = portfolio_transaction.get("company_name")
                number_shares = portfolio_transaction.get("number_shares")
                price_share = portfolio_transaction.get("price_share")
                currency = portfolio_transaction.get("currency")
                currency_exchange = portfolio_transaction.get("currency_exchange")
                total_amount_shares = portfolio_transaction.get("total_amount_shares")
                currency_fee = portfolio_transaction.get("currency_fee")
                
                # Add the details about the company
                company = Company(name = company_name, stock_name = stock_name)
                company.save()
                
                # Add the details about the stock
                stock = Stock(company = company, total_amount = total_amount_shares, number_of_shares = number_shares, currency = currency)
                stock.save()
                
            else :
                
                # Add the amount of the stock to the current stock object
                if type_transaction == 'Market buy' :
                    print("Added amount " + total_amount_shares)
                
                # Subtract the amount of the stock to the current stock object    
                if type_transaction == 'Market sell' :
                    print("Subtracted amount " + total_amount_shares)
                    
            i += 1
            
        # Sort list according to the company name to be able to process each company share
        #list_portfolio_transactions.sort(key=)
           
            
        
        # Sort list by company to be able to calculate amount held per stocks for that specific company
        
    # We can only have one portfolio file, the person who is creating her own portfolio based on one source and the build is done once the user upload this file
    # He can always modify an existing file to reload portfolio transactions
    def clean(self):
        if Portfolio_File.objects.exists() and not self.pk:
            raise ValidationError('There can only be one portfolio file as a baseline to build your portfolio')
    
    def delete(self, using=None, keep_parents=False):
        return models.Model.delete(self, using=using, keep_parents=keep_parents)
    
