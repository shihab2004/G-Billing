from rest_framework import serializers
from ebilling.models import *
class CompanySRZ(serializers.ModelSerializer):
       logo =  serializers.CharField()
       class Meta:
            model = Company
            fields="__all__"
          
            
            
class BankSRZ(serializers.ModelSerializer):
       class Meta:
            model = Bank
            fields="__all__"


class BrandSRZ(serializers.ModelSerializer):
       class Meta:
            model = Brand
            fields="__all__"
            
            
class ClientSRZ(serializers.ModelSerializer):
       profile_pic = serializers.CharField()
     #   identity_doc = serializers.CharField()
     #   account_type = serializers.CharField()
       class Meta:
            model = Client
            fields="__all__"
            
            
class SupplierSRZ(serializers.ModelSerializer):
       class Meta:
            model = Supplier
            fields="__all__"

class GroupSRZ(serializers.ModelSerializer):
       class Meta:
            model = Group
            fields="__all__"


class ParticularSRZ(serializers.ModelSerializer):
       class Meta:
            model = Particular
            fields="__all__"
            


class ProductSRZ(serializers.ModelSerializer):
       picture = serializers.CharField()
       class Meta:
            model = Product
            fields="__all__"


class PurchaseSRZ(serializers.ModelSerializer):
       class Meta:
            model = Purchase
            fields="__all__"

class Stock_summarySRZ(serializers.ModelSerializer):
       class Meta:
            model = StockSummary
            fields="__all__"

class Bank_account_adjustmentSRZ(serializers.ModelSerializer):
       class Meta:
            model = BankAccountAdjustment
            fields="__all__"


class Bank_account_ledgerSRZ(serializers.ModelSerializer):
       class Meta:
            model = BankAccountLedger
            fields="__all__"


class CashBookAdjustmentSRZ(serializers.ModelSerializer):
       class Meta:
            model = CashBookAdjustment
            fields="__all__"
            
            
            
class ServiceSRZ(serializers.ModelSerializer):
       class Meta:
            model = Service
            fields="__all__"
            
            
class CashBookSRZ(serializers.ModelSerializer):
       class Meta:
            model = CashBook
            fields="__all__"


class ExpenseSRZ(serializers.ModelSerializer):
       class Meta:
            model = Expense
            fields="__all__"