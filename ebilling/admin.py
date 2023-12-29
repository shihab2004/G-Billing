from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Company)
admin.site.register(Client)
admin.site.register(Supplier)

# Master Model Register Here
admin.site.register(Group)
admin.site.register(Brand)
admin.site.register(Bank)
admin.site.register(ExpenseType)
admin.site.register(Unit)
admin.site.register(Designation)
admin.site.register(Department)
admin.site.register(PayMode)

admin.site.register(Expense)
admin.site.register(Category)
admin.site.register(CategoryType)
admin.site.register(Tax)
admin.site.register(TaxType)
admin.site.register(ItemCategory)
admin.site.register(Product)
admin.site.register(Service)
admin.site.register(Purchase)
admin.site.register(Particular)


admin.site.register(StockSummary)
admin.site.register(BankAccountLedger)
admin.site.register(BankAccountAdjustment)

admin.site.register(CashBook)
admin.site.register(CashBookAdjustment)

class HistoryModelView(admin.ModelAdmin):
    list_filter = ['user__username','user__getCompany__name']
admin.site.register(History,HistoryModelView)
admin.site.register(UserPermission)