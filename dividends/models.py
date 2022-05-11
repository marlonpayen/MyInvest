from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    


class Stock(models.Model):
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    amount  = models.DecimalField(max_digits=9, decimal_places=2)
    
    # Create your models here.
class Dividend(models.Model):
    name = models.CharField(max_length=50)
    
class Portfolio_File(models.Model):
    data = models.FileField()

    def save(self, *args, **kwargs):
        super(Portfolio_File, self).save(*args, **kwargs)
        filename = self.data.url
        # Do anything you'd like with the data in filename bla
    
