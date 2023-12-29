from pyexpat import model
from django.db.models import Model
from django.db import models
import string
import uuid
from django.contrib.auth.models import User
from django.db.models import Max

A4 = "A4"
Small = "288mm"
Medium = "500mm"


PAPER_SIZE_CHOICES = (
    (A4, "A4"),
    (Small, "288mm"),
    (Medium, "500mm"),
)

CLIENT_ACCOUNT_TYPE = (
    ("DEBIT", "Debit"),
    ("CREDIT", "Credit"),
   
)
CLIENT_IDENTITY_DOCUMENT_TYPE = (
    ("Citizenship Card", "Citizenship"),
    ("Driving License", "Driving License"),
    ("PAN Card", "Pan Card"),
    ("Passport", "Passport"),
    ("Voter ID", "Voter ID"),
   
)

class Company(Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=200, blank=True,null=True)
    phone = models.CharField(max_length=10)
    city=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    province=models.CharField(max_length=50)
    pincode=models.IntegerField(max_length=6)
    country=models.CharField(max_length=50,default="Nepal")
    pan_no=models.CharField(max_length=50)
    reg_no=models.CharField(max_length=50,null=True,blank=True)
    reg_date=models.DateField(null=True,blank=True)
    website=models.URLField(max_length=255,blank=True,null=True)
    address = models.CharField(max_length=255,null=True, blank=True)
    logo=models.FileField(upload_to='company_logo' ,  default='default.png')
    paper_size=models.CharField(max_length=10, choices=PAPER_SIZE_CHOICES,default="A4")
    user=models.ManyToManyField(User,blank=True,related_name="getCompany")              # Change to many field

    def __str__(self):
        return self.name


class Client(Model):
    fullname=models.CharField(max_length=100)
    billing_address=models.CharField(max_length=300)
    city=models.CharField(max_length=50,null=True,blank=True)
    district=models.CharField(max_length=50)
    province=models.CharField(max_length=50)
    pincode=models.CharField(max_length=6,null=True,blank=True)
    country=models.CharField(max_length=50,default="Nepal")
    email=models.EmailField(max_length=200, blank=True,null=True)
    phone = models.CharField(max_length=10,blank=True,null=True)
    mobile = models.CharField(max_length=10)
    pan_no=models.CharField(max_length=10,blank=True,null=True)
    vat=models.CharField(max_length=10,blank=True,null=True)
    account_type=models.CharField(max_length=10, choices=CLIENT_ACCOUNT_TYPE,  default="Debit")
    opening_balance=models.IntegerField(null=True,blank=True)
    profile_pic=models.FileField(upload_to='client_profile_pic' ,  default='default.png')
    identity_doc=models.CharField(max_length=50, choices=CLIENT_IDENTITY_DOCUMENT_TYPE,  blank=True,null=True)
    document_no=models.CharField(max_length=50, blank=True,null=True)
    credit_allowed=models.BooleanField()
    credit_limit=models.IntegerField(null=True,blank=True)
    remark=models.CharField(max_length=255, blank=True,null=True)
    is_active=models.BooleanField(default=True)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    def __str__(self):
        return self.fullname


class Supplier(Model):
    company_name=models.CharField(max_length=100)
    billing_address=models.CharField(max_length=300,null=True,blank=True)
    city=models.CharField(max_length=50,null=True,blank=True)
    district=models.CharField(max_length=50)
    province=models.CharField(max_length=50)
    pincode=models.CharField(max_length=6,null=True,blank=True)
    country=models.CharField(max_length=50,default="Nepal")
    email=models.EmailField(max_length=200, blank=True,null=True)
    phone = models.CharField(max_length=10,blank=True,null=True)
    contact_person = models.CharField(max_length=50,blank=True,null=True)
    contact_no = models.CharField(max_length=10)
    pan_no=models.CharField(max_length=10,blank=True,null=True)
    vat=models.CharField(max_length=10,blank=True,null=True)
    account_type=models.CharField(max_length=10, choices=CLIENT_ACCOUNT_TYPE,  default="Debit")
    opening_balance=models.IntegerField(null=True,blank=True)
    bank_name=models.CharField(max_length=50, blank=True,null=True)
    account_no=models.CharField(max_length=100, blank=True,null=True)
    ifsc_code=models.CharField(max_length=100, blank=True,null=True)
    remark=models.CharField(max_length=255, blank=True,null=True)
    is_active=models.BooleanField(default=True)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.company_name


class ExpenseType(Model):
    name=models.CharField(max_length=100)
    is_enabled=models.BooleanField(default=True)
    def __str__(self):
        return self.name 

class Expense(Model):
    date=models.DateField()
    paid_to=models.CharField(max_length=100)
    paid_by=models.CharField(max_length=100)
    expense_type=models.ForeignKey(ExpenseType,on_delete=models.CASCADE)
    amount=models.CharField(max_length=50)
    pay_mode=models.CharField(max_length=50)
    pay_ref_no=models.CharField(max_length=100,blank=True,null=True)
    remark=models.CharField(max_length=50)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # def __str__(self):
    #     return self.expense_type.name + "-> Paid By :" + self.paid_by

class Brand(Model):
    name=models.CharField(max_length=100)
    is_enabled=models.BooleanField(default=True)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    def __str__(self):
        return self.name 

class Designation(Model):
    name=models.CharField(max_length=100)
    is_enabled=models.BooleanField(default=True)
    def __str__(self):
        return self.name 

class Department(Model):
    name=models.CharField(max_length=100)
    is_enabled=models.BooleanField(default=True)
    def __str__(self):
        return self.name 

class Unit(Model):
    name=models.CharField(max_length=100)
    is_enabled=models.BooleanField(default=True)
    def __str__(self):
        return self.name 

class Group(Model):
    name=models.CharField(max_length=200)
    vat=models.IntegerField(null=True,blank=True)
    hsn_or_sac_code=models.CharField(max_length=200,null=True,blank=True)
    is_enabled=models.BooleanField(default=True)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    def __str__(self):
        return self.name 

class Bank(Model):
    account_name=models.CharField(max_length=100)
    account_no=models.BigIntegerField()
    bank_name=models.CharField(max_length=200)
    account_type=models.CharField(max_length=50)
    opening_balance=models.BigIntegerField()
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.bank_name

class CategoryType(Model):
    name=models.CharField(max_length=50)
    is_enabled=models.BooleanField(default=True)
    def __str__(self):
        return self.name


class Category(Model):
    name=models.CharField(max_length=50)
    type=models.ForeignKey(CategoryType,on_delete=models.CASCADE)
    color=models.CharField(max_length=50)
    is_enabled=models.BooleanField(default=True)
    def __str__(self):
        return self.name


class TaxType(Model):
    name=models.CharField(max_length=50)
    is_enabled=models.BooleanField(default=True)
    def __str__(self):
        return self.name

class PayMode(Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Tax(Model):
    name=models.CharField(max_length=50)
    type=models.ForeignKey(TaxType,on_delete=models.CASCADE)
    rate=models.CharField(max_length=5)
    is_enabled=models.BooleanField(default=True)
    def __str__(self):
        return self.name


class ItemCategory(Model):
    name=models.CharField(max_length=50)
    is_enabled=models.BooleanField(default=True)
    def __str__(self):
        return self.name




class Product(Model):
    item_code=models.CharField(max_length=70,null=True,blank=True)
    name=models.CharField(max_length=255)
    print_name=models.CharField(max_length=255,null=True,blank=True)
    sale_price=models.IntegerField()
    purchase_price=models.IntegerField()
    min_sale_price=models.IntegerField(blank=True,null=True)
    mrp=models.IntegerField(blank=True,null=True)
    opening_stock=models.IntegerField(blank=True,null=True)
    opening_stock_price=models.IntegerField(blank=True,null=True)
    hsn_or_sac_code=models.CharField(max_length=200,null=True,blank=True)
    vat=models.FloatField()
    discount=models.IntegerField(blank=True,null=True)
    serial_no=models.CharField(max_length=100,null=True,blank=True)
    description=models.TextField(max_length=250,blank=True,null=True)
    picture=models.FileField(upload_to='items' , default='shopping-bag.png')
    is_print_description=models.BooleanField(default=False)
    is_one_click_sale=models.BooleanField(default=False)
    is_enabled_for_tracking=models.BooleanField(default=False)
    is_print_serial_no=models.BooleanField(default=False)
    is_not_for_sale=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    unit=models.ForeignKey(Unit,on_delete=models.CASCADE)
    category=models.ForeignKey(ItemCategory,on_delete=models.CASCADE)
    group=models.ForeignKey(Group,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Service(Model):
    group=models.ForeignKey(Group,on_delete=models.CASCADE)
    item_code=models.CharField(max_length=70,null=True,blank=True)
    name=models.CharField(max_length=255)
    print_name=models.CharField(max_length=255,null=True,blank=True)
    decription=models.CharField(max_length=255)
    service_charge=models.IntegerField()
    min_service_charge=models.IntegerField(null=True,blank=True)
    discount=models.FloatField(null=True,blank=True)
    hsn_or_sac_code=models.CharField(max_length=200,null=True,blank=True)
    vat=models.FloatField()
    unit=models.ForeignKey(Unit,on_delete=models.CASCADE,null=True,blank=True)
    is_print_description=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    def __str__(self):
        return self.name


# Summary models here 

class StockSummary(Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    opening_qty=models.IntegerField()
    inward_qty=models.IntegerField()
    outward_qty=models.IntegerField()
    closing_qty=models.IntegerField()
    net_change=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    def __str__(self):
        return self.product.name +" - Stock Summary"


class BankAccountLedger(Model):
    bank=models.ForeignKey(Bank,on_delete=models.CASCADE)
    date=models.DateField(null=True,blank=True)
    description=models.CharField(max_length=255)
    debit=models.FloatField(null=True,blank=True)
    credit=models.FloatField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    def __str__(self):
        return self.bank.bank_name +" -> "+ self.description+" - Account Ledger"


class BankAccountAdjustment(Model):
    bank=models.ForeignKey(Bank,on_delete=models.CASCADE)
    date=models.DateField(null=True,blank=True)
    type=models.CharField(max_length=255)
    amount=models.FloatField()
    remark=models.CharField(max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    def __str__(self):
        return self.bank.bank_name +" - Account Ledger"



class CashBook(Model):
    date=models.DateField(null=True,blank=True)
    particulars=models.CharField(max_length=255)
    type=models.CharField(max_length=255)
    debit=models.FloatField(null=True,blank=True)
    credit=models.FloatField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    def __str__(self):
        return self.particulars +" -> "+ self.type+" - CashBook Ledger"


class CashBookAdjustment(Model):
    date=models.DateField(null=True,blank=True)
    type=models.CharField(max_length=255)
    amount=models.FloatField()
    remark=models.CharField(max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    def __str__(self):
        return self.type +" - " +str(self.date)





class Purchase(Model):
    type=models.CharField(max_length=255)
    bill_date=models.DateField(null=True,blank=True)
    supplier=models.ForeignKey(Supplier,on_delete=models.CASCADE)
    payment_terms=models.CharField(max_length=255,null=True,blank=True)
    due_date=models.DateField(null=True,blank=True)
    place_of_supply=models.CharField(max_length=255)
    bill_no=models.CharField(max_length=255,null=True,blank=True)
    order_no=models.CharField(max_length=255,null=True,blank=True)
    order_date=models.DateField(null=True,blank=True)
    e_way_bill_no=models.CharField(max_length=255,null=True,blank=True)
    pay_mode=models.ForeignKey(PayMode,on_delete=models.CASCADE)
    transaction_id=models.CharField(max_length=255,null=True,blank=True)
    amount_paid=models.IntegerField()
    balance=models.IntegerField()
    sub_total_amount=models.IntegerField()
    vat_amount=models.FloatField()
    round_off_amount=models.FloatField(null=True,blank=True)
    total_amount=models.PositiveBigIntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    purchase_id = models.CharField(max_length=10, blank=True, null=True,unique=True)

    def save(self, *args, **kwargs):
        if self.__class__.objects.all().count() == 0:
            # First object need to be set like this
            letter =  'P-'
            number = 1
            # %05d used to write the number with 2 zeros before
            self.purchase_id = letter+'{0:05d}'.format(number)  # 'A001' this time
        else:
            # Get the last object ID
            last_id = self.__class__.objects.all().order_by("-id")[0].id + 1

            # We need to know wich letter is it, we use division over ID
            # wich_letter = (last_id+1) / 1000  
            letter =  'P-'
            number = (last_id+1) % 100000
            self.purchase_id = letter+'{0:05d}'.format(number)

        super(self.__class__, self).save(*args, **kwargs)

    def __str__(self):
        return self.purchase_id


class Particular(Model):
    item_code=models.CharField(max_length=255,null=True,blank=True)
    item=models.ForeignKey(Product,on_delete=models.CASCADE)
    unit=models.ForeignKey(Unit,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    purchase_price=models.IntegerField()
    vat=models.FloatField()
    discount=models.IntegerField(blank=True,null=True)
    total=models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    purchasebill=models.ForeignKey(Purchase,on_delete=models.CASCADE)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    def __str__(self):
        return self.item.name
    
    
    
    
    






class History(Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    task = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    

class UserPermission(Model):
    user = models.ManyToManyField(User,related_name="getPermissions",blank=True)
    task = models.CharField(max_length=100)
    
    def __str__(self):
        return self.task