from django.contrib import admin
from dividends.models import Company, Stock, Transaction, Portfolio_File

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    #fields = ['first_name', 'last_name']
    ordering = ['name']
    list_display = ('name', 'stock_name', 'year_of_foundation')

    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        if Company.objects.exists():
            return False
        
        return True
    
# Register Company and CompanyAdmin
admin.site.register(Company, CompanyAdmin)

class StockAdmin(admin.ModelAdmin):
    #fields = ['first_name', 'last_name']
    ordering = ['-number_of_shares']
    list_display = ('get_company_name', 'number_of_shares', 'total_amount', 'currency')

    # This will help you to disable add functionality
    def has_add_permission(self, request):
        return False
    
    def get_company_name(self, obj):
        return obj.company.name
    
# Register Stock and StockAdmin
admin.site.register(Stock, StockAdmin)

class TransactionAdmin(admin.ModelAdmin):
    #fields = ['first_name', 'last_name']
    list_display = ('get_company_name', 'number_of_shares', 'total_amount', 'currency')

    # This will help you to disable add functionality
    def has_add_permission(self, request):
        return False
    
    def get_company_name(self, obj):
        return obj.company.name
    
# Register Contact and ContactAdmin
admin.site.register(Transaction, TransactionAdmin)

class Portfolio_FileAdmin(admin.ModelAdmin):
    # This will help you to disable add functionality
    def has_add_permission(self, request):
        if Portfolio_File.objects.exists():
            return False
        
        return True
    
admin.site.register(Portfolio_File, Portfolio_FileAdmin)