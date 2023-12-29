

from django.views.generic.list import ListView
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404,redirect,reverse
from django.db.models import Count,Q
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.conf import settings
from django.contrib import messages
from GMCNEPAL.settings import BASE_DIR
from django.utils.translation import gettext as _
from django.contrib.auth.models import Permission
from ebilling.utils import check_permission

from ebilling.models import Category, CategoryType, Company
from .forms import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required


from django.http import JsonResponse,Http404
# Create your views here.
from django.template.loader import render_to_string

from .models import *
import datetime
from django.template import RequestContext
import xlwt

from django.http import HttpResponse,HttpResponseNotFound
from django.core.files.storage import FileSystemStorage
# Create your views here.

from .utils import Log, render_to_pdf


# Global Variables Start Here 
expensesResultSet=[]
fromDate=""
toDate=""

def setGlobalExpensesResultSet(eResultSet):
    global expensesResultSet    # Needed to modify global copy of globvar
    expensesResultSet = eResultSet

def getGlobalExpensesResultSet():
    return expensesResultSet

def setFromDateAndToDate(fromD,toD):
    global fromDate,toDate
    fromDate=fromD
    toDate=toD 
def getFromDateAndToDate():
    return (fromDate,toDate)

def loginPage(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, _("Welcome") + f' {username} !!')
            # print("loggedin")
            return redirect('ebilling:dashboard')
        else:
            messages.error(request, _('account done not exit plz sign in'))
    return render(request,"ebilling/LoginPage.html")


def registerPage(request):
    form=CreateUserForm()
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            if(len(User.objects.filter(email=email))>0):
                messages.error(request,_("Email already used!!"))
                return redirect(request.META.get('HTTP_REFERER'))
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,"Account created for "+user)
            Company(name="N/A",pan_no="N/A",reg_no="N/A",reg_date="N/A",phone="9800000000",city="N/A",district="N/A",province="N/A",pincode="00000",user=request.user,address="N/A").save()

            return redirect('ebilling:login')
    context={'form':form}
    
    return render(request,"ebilling/register.html",context)



@login_required(login_url='/e-billing/login')
@check_permission()
def Logout(request):
    logout(request)
    return redirect('ebilling:login')

@login_required(login_url='/e-billing/login')
@check_permission()
def updateCompanyDetailPage(request):
    if request.method == "POST":
        cid=request.POST['cid']
        if request.FILES:
            logo=request.FILES['logo']    
        name=request.POST.get('name')
        email=request.POST.get('email',None)
        website=request.POST.get('website',None)
        pan_no = request.POST.get('pan_no')
        reg_no = request.POST.get('reg_no',None)
        reg_date = request.POST.get('reg_date',None)
        if(reg_date is not None):
            try:
                reg_date=datetime.datetime.strptime(reg_date, "%d/%m/%Y").strftime("%Y-%m-%d")
            except:
                messages.error(request,_("Date format is incorrect, Eg: dd/mm/yyyy"))
                return redirect("ebilling:updatecompany")
        phone=request.POST.get('phone')
        city=request.POST.get('city')
        district=request.POST.get('district')
        province=request.POST.get('province')
        pincode=request.POST.get('pincode',None)
        address=request.POST.get('address')
        # paper_size=request.POST.get('paper_size')
        try:
            Company(id=cid,name=name,email=email,website=website,pan_no=pan_no,reg_no=reg_no,reg_date=reg_date,phone=phone,city=city,district=district,province=province,pincode=pincode,logo=logo,user=request.user,address=address).save()
        except:
            mylogo=Company.objects.get(id=cid).logo
            Company(id=cid,name=name,email=email,website=website,pan_no=pan_no,reg_no=reg_no,reg_date=reg_date,phone=phone,city=city,district=district,province=province,pincode=pincode,logo=mylogo,user=request.user,address=address).save()
        messages.success(request,_("Company Detail Updated Successfully"))
        return redirect("ebilling:dashboard")
   
    companyObj=Company.objects.filter(user=request.user)[0]
    formattedDate= companyObj.reg_date.strftime("%d/%m/%Y")
    return render(request,"ebilling/UpdateCompanyPage.html",{"company":companyObj,"formattedDate":formattedDate})

@login_required(login_url='/e-billing/login')
@check_permission()
def companyDetailPage(request):
    company= Company.objects.filter(user=User.objects.filter(id=request.user.id)[0])[0]
    print(company)
    if request.method == 'POST':
        tax=request.POST['tax_no']
        if request.FILES:
                logo=request.FILES['logo']    
        name=request.POST['name']
        tax=request.POST['tax_no']
        email=request.POST['email']
        address=request.POST['address']
        phone=request.POST['phone']
       
        company.name=name 
        company.tax_number=tax
        company.email=email
        company.address=address 
        company.phone=phone 
        company.save()
        messages.success(request,"Company Details Updated")
        return redirect('ebilling:dashboard')
       
    if(company):
        context={"company":company}
        return render(request,"ebilling/account-settings.html",context)
    else:
        return render(request,"ebilling/account-settings.html")



@login_required(login_url='/e-billing/login')
@check_permission()
def addClientPage(request):
    if request.method == "POST":
        if request.FILES:
            profile=request.FILES['profile_pic']    
        fullname=request.POST.get('fullname')
        email=request.POST.get('email',None)
        pan_no = request.POST.get('pan_no')
        vat_no = request.POST.get('vat_no',None)
        phone=request.POST.get('phone',None)
        mobile = request.POST.get('mobile')
        city=request.POST.get('city',None)
        district=request.POST.get('district')
        province=request.POST.get('province')
        pincode=request.POST.get('pincode',None)
        billing_address=request.POST.get('billing_address')
        identity_doc_type=request.POST.get('identity_doc',None)
        document_no=request.POST.get('document_no',None)
        account_type=request.POST.get('account_type',None)
        opening_balance=request.POST.get('opening_balance',0)
        credit_allowed=request.POST.get('credit_allowed',None)
        credit_limit=request.POST.get('credit_limit',0)
        remark=request.POST.get('remark',None)
        try:
            Client(fullname=fullname,email=email,mobile=mobile,pan_no=pan_no,
            vat=vat_no,billing_address=billing_address,phone=phone,city=city,
            district=district,province=province,pincode=pincode,
            profile_pic=profile,identity_doc=identity_doc_type,document_no=document_no,account_type=account_type,
            opening_balance=opening_balance,credit_allowed=credit_allowed,credit_limit=credit_limit,
            company=Company.objects.filter(user=request.user)[0],remark=remark).save()
        except:
            Client(fullname=fullname,email=email,mobile=mobile,pan_no=pan_no,
            vat=vat_no,billing_address=billing_address,phone=phone,city=city,
            district=district,province=province,pincode=pincode,
            identity_doc=identity_doc_type,document_no=document_no,account_type=account_type,
            opening_balance=opening_balance,credit_allowed=credit_allowed,credit_limit=credit_limit,
            company=Company.objects.filter(user=request.user)[0],remark=remark).save()
        messages.success(request,"New Client Created :"+str(Client.objects.latest('id').id))
        
        Log(request,f"A New Client has been added, Name:{fullname}; City:{city};")          # Log messages
        
        return redirect("ebilling:clients")
    return render(request,"ebilling/AddClientPage.html")



@login_required(login_url='/e-billing/login')
@check_permission()
def updateClientPage(request,pk):
    client=Client.objects.filter(id=pk,company=Company.objects.filter(user=User.objects.filter(id=request.user.id)[0])[0])[0]
    if request.method == "POST":
        if request.FILES:
            client.profile=request.FILES['profile_pic']    
        client.fullname=request.POST.get('fullname')
        client.email=request.POST.get('email',None)
        client.pan_no = request.POST.get('pan_no')
        client.vat_no = request.POST.get('vat_no',None)
        client.phone=request.POST.get('phone',None)
        client.mobile = request.POST.get('mobile')
        client.city=request.POST.get('city',None)
        client.district=request.POST.get('district')
        client.province=request.POST.get('province')
        client.pincode=request.POST.get('pincode',None)
        client.billing_address=request.POST.get('billing_address')
        client.identity_doc_type=request.POST.get('identity_doc',None)
        client.document_no=request.POST.get('document_no',None)
        client.account_type=request.POST.get('account_type',None)
        client.opening_balance=request.POST.get('opening_balance',0)
        client.credit_allowed=request.POST.get('credit_allowed',None)
        client.credit_limit=request.POST.get('credit_limit',0)
        client.remark=request.POST.get('remark',None)
        client.save()
        messages.success(request,"Client Updated")
        Log(request,f"A Client information has updated. Name:{client.fullname} ")          # Log messages
        return redirect("ebilling:clients")
    return render(request,"ebilling/updateClientPage.html",{"client":client})



@login_required(login_url='/e-billing/login')
@check_permission()
def clientsPage(request):
    try:
        userCompany=Company.objects.filter(user=User.objects.filter(id=request.user.id)[0])[0]
        clients=Client.objects.filter(company=userCompany)
        if request.method == 'POST':
            ID=request.POST.get('id',None)
            fname=request.POST.get('name',None)
            phone=request.POST.get('contact',None)

            # clients=Client.objects.filter(Q(id__icontains=ID) | Q(name__icontains=fname) | Q(mobile__icontains=phone))
            if(ID and len(Client.objects.filter(id=ID,company=userCompany))>0 ):
                clients=Client.objects.filter(id=ID,company=userCompany)
            elif(fname and len(Client.objects.filter(fullname__icontains=fname,company=userCompany))>0):
                clients=Client.objects.filter(Q(fullname__icontains=fname,company=userCompany)).values()
            elif(phone and len(Client.objects.filter(mobile=phone,company=userCompany))>0):
                clients=Client.objects.filter(mobile=int(phone),company=userCompany)
            else:
                clients=[]
    except:
        clients=[]
   
    return render(request,"ebilling/SearchAndManageClientsPage.html",{"clients":clients})



@login_required(login_url='/e-billing/login')
@check_permission()
def deleteClientPage(request,pk):
    clientResult=Client.objects.filter(id=pk,company=Company.objects.filter(user=User.objects.filter(id=request.user.id)[0])[0])
    if(len(clientResult)>0):
        Log(request,f"Client {clientResult[0].fullname} has removed from your company,")          # Log messages
        clientResult.delete()
        messages.success(request,"Client: "+str(pk)+" deleted")
    else:
        messages.error(request,"Don't have permission to delete!")
    return redirect(request.META.get('HTTP_REFERER'))

# Supplier Views here 

@login_required(login_url='/e-billing/login')
@check_permission(name="Allow Purchase")
def addSupplierPage(request):
    if request.method == "POST":
        company_name=request.POST.get('fullname')
        email=request.POST.get('email',None)
        pan_no = request.POST.get('pan_no')
        vat_no = request.POST.get('vat_no',None)
        phone=request.POST.get('phone',None)
        contact_no = request.POST.get('mobile')
        contact_person = request.POST.get('contact_person')
        city=request.POST.get('city',None)
        district=request.POST.get('district')
        province=request.POST.get('province')
        pincode=request.POST.get('pincode',None)
        billing_address=request.POST.get('billing_address')
        bank_name=request.POST.get('bank_name',None)
        account_no=request.POST.get('bank_account_no',None)
        account_type=request.POST.get('account_type',None)
        opening_balance=request.POST.get('opening_balance',0)
        ifsc_code=request.POST.get('ifsc_code',None)
        remark=request.POST.get('remark',None)

        Supplier(company_name=company_name,email=email,contact_no=contact_no,contact_person=contact_person,pan_no=pan_no,
        vat=vat_no,billing_address=billing_address,phone=phone,city=city,
        district=district,province=province,pincode=pincode,bank_name=bank_name,account_no=account_no,account_type=account_type,
        opening_balance=opening_balance,ifsc_code=ifsc_code,
        company=Company.objects.filter(user=request.user)[0],remark=remark).save()
        messages.success(request,"New Supplier Created :"+str(Supplier.objects.latest('id').id))
        
        Log(request,f"A new supplier has been added from {city}, Name: {company_name}, Vat:{vat_no}")          # Log messages
        return redirect("ebilling:suppliers")
    return render(request,"ebilling/AddSupplierPage.html")

@login_required(login_url='/e-billing/login')
@check_permission(name='Allow Expense')
def updateSupplierPage(request,pk):
    supplier=Supplier.objects.filter(id=pk,company=Company.objects.filter(user=User.objects.filter(id=request.user.id)[0])[0])[0]
    if request.method == "POST":
        supplier.company_name=request.POST.get('fullname')
        supplier.email=request.POST.get('email',None)
        supplier.pan_no = request.POST.get('pan_no')
        supplier.vat_no = request.POST.get('vat_no',None)
        supplier.phone=request.POST.get('phone',None)
        supplier.contact_person = request.POST.get('contact_person',None)
        supplier.contact_no = request.POST.get('mobile')
        supplier.city=request.POST.get('city',None)
        supplier.district=request.POST.get('district')
        supplier.province=request.POST.get('province')
        supplier.pincode=request.POST.get('pincode',None)
        supplier.billing_address=request.POST.get('billing_address')
        supplier.bank_name=request.POST.get('bank_name',None)
        supplier.account_no=request.POST.get('bank_account_no',None)
        supplier.ifsc_code=request.POST.get('ifsc_code',None)
        supplier.account_type=request.POST.get('account_type',None)
        supplier.opening_balance=request.POST.get('opening_balance',0)
        supplier.remark=request.POST.get('remark',None)
        supplier.save()
        messages.success(request,"Supplier Information Updated")
        Log(request,f"{supplier.company_name} supplier Information has Updated. ID: #{supplier.pk}")          # Log messages
        return redirect("ebilling:suppliers")
    return render(request,"ebilling/UpdateSupplierPage.html",{"Supplier":supplier})



@login_required(login_url='/e-billing/login')
@check_permission(name="Allow Purchase")
def suppliersPage(request):
    try:
        userCompany=Company.objects.filter(user=User.objects.filter(id=request.user.id)[0])[0]
        suppliers=Supplier.objects.filter(company=userCompany)
        if request.method == 'POST':
            ID=request.POST.get('id',None)
            name=request.POST.get('name',None)
            phone=request.POST.get('contact',None)

            # clients=Client.objects.filter(Q(id__icontains=ID) | Q(name__icontains=fname) | Q(mobile__icontains=phone))
            if(ID and len(Supplier.objects.filter(id=ID,company=userCompany))>0 ):
                suppliers=Supplier.objects.filter(id=ID,company=userCompany)
            elif(name and len(Supplier.objects.filter(company_name__icontains=name,company=userCompany))>0):
                suppliers=Supplier.objects.filter(Q(company_name__icontains=name,company=userCompany)).values()
            elif(phone and len(Supplier.objects.filter(contact_no=phone,company=userCompany))>0):
                suppliers=Supplier.objects.filter(contact_no=phone,company=userCompany)
            else:
                suppliers=[]
    except:
        suppliers=[]
   
    return render(request,"ebilling/SearchAndManageSupplierPage.html",{"suppliers":suppliers})



@login_required(login_url='/e-billing/login')
@check_permission(name='Allow Expense')
def deleteSupplierPage(request,pk):
    supplierResult=Supplier.objects.filter(id=pk,company=Company.objects.filter(user=User.objects.filter(id=request.user.id)[0])[0])
    if(len(supplierResult)>0):
        Log(request,f"{supplierResult[0].company_name} Supplier has removed.")          # Log messages
        supplierResult.delete()
        messages.success(request,"Supplier: "+str(pk)+" deleted")
    else:
        messages.error(request,"Don't have permission to delete!")
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/e-billing/login')
@check_permission(name='Allow Expense')
def addExpensePage(request):
    expense_type=ExpenseType.objects.all()
    if request.method == "POST":
        p_date=request.POST.get('exp_date')
        if(p_date is not None):
            d=p_date.split("-")
            p_date=datetime.date(int(d[0]),int(d[1]),int(d[2]))
        paid_to=request.POST.get('paid_to')
        paid_by=request.POST.get('paid_by')
        amount = request.POST.get('amount')
        expenseType = request.POST.get('expense_type')
      
        pay_mode=request.POST.get('pay_mode')
        ref_no = request.POST.get('payment_ref_no')
        remark=request.POST.get('remark',None)
        ex = Expense(date=p_date,paid_to=paid_to,paid_by=paid_by,amount=amount,expense_type=ExpenseType.objects.filter(id=expenseType)[0],pay_mode=pay_mode,pay_ref_no=ref_no,remark=remark,
        company=Company.objects.filter(user=request.user)[0]).save()
        messages.success(request,"New Expense Added")
        
        Log(request,f"New Expense has Added, ID:#{ex.pk}, Amount:{ex.amount}")          # Log messages
        return redirect("ebilling:expenses")
    return render(request,"ebilling/addExpensePage.html",{"expenses":expense_type})



@login_required(login_url='/e-billing/login')
@check_permission(name='Allow Expense')
def expensesPage(request):
    try:
        userCompany=Company.objects.filter(user=User.objects.filter(id=request.user.id)[0])[0]
        expenses=Expense.objects.filter(company=userCompany)
        if request.method == 'POST':
            expense_type=request.POST.get('expense_type',None)
            paid_to=request.POST.get('paid_to',None)
            paid_by=request.POST.get('paid_by',None)

            # clients=Client.objects.filter(Q(id__icontains=ID) | Q(name__icontains=fname) | Q(mobile__icontains=phone))
            if(expense_type and len(Expense.objects.filter(expense_type=ExpenseType.objects.filter(name=expense_type)[0],company=userCompany))>0 ):
                expenses=Expense.objects.filter(expense_type=ExpenseType.objects.filter(name=expense_type)[0],company=userCompany)
            elif(paid_to and len(Expense.objects.filter(paid_to__icontains=paid_to,company=userCompany))>0):
                expenses=Expense.objects.filter(paid_to__icontains=paid_to,company=userCompany).values()
            elif(paid_by and len(Expense.objects.filter(paid_by__icontains=paid_by,company=userCompany))>0):
                expenses=Expense.objects.filter(paid_by__icontains=paid_by,company=userCompany)
            else:
                expenses=[]
            return render(request,"ebilling/search_manage_expensesPage.html",{"expenses":expenses})

    except:
        expenses=[]
   
    return render(request,"ebilling/SearchAndManageExpensesPage.html",{"expenses":expenses})

@login_required(login_url='/e-billing/login')
@check_permission(name='Allow Expense')
def updateExpensePage(request,pk):
    userCompany=Company.objects.filter(user=User.objects.filter(id=request.user.id)[0])[0]
    expense=Expense.objects.filter(id=pk,company=userCompany)[0]
    expenses=ExpenseType.objects.all()
    if request.method == "POST":
        expense.date=request.POST.get('exp_date')
        expense.paid_to=request.POST.get('paid_to',None)
        expense.paid_by = request.POST.get('paid_by')
        expense.amount = request.POST.get('amount')
        expense.expense_type = ExpenseType.objects.get(id=request.POST.get('expense_type'))
        expense.pay_mode=request.POST.get('pay_mode',None)
        expense.pay_ref_no=request.POST.get('payment_ref_no',None)
        expense.remark=request.POST.get('remark',None)
        expense.save()
        messages.success(request,"Expense Detail Updated")
        
        Log(request,f"An Expense Detail has Updated, ID:#{expense.pk}")          # Log messages
        
        return redirect("ebilling:expenses")
    return render(request,"ebilling/UpdateExpensePage.html",{"expense":expense,"expenses":expenses})

@login_required(login_url='/e-billing/login')
@check_permission(name='Allow Expense')
def deleteExpensePage(request,pk):
    expense=Expense.objects.filter(id=pk,company=Company.objects.filter(user=User.objects.filter(id=request.user.id)[0])[0])
    if(len(expense)>0):
        Log(request,f"An Expense has removed, ID:#{expense[0].pk}")          # Log messages
        expense[0].delete()
        messages.success(request,"Expense: "+str(pk)+" deleted")
    else:
        messages.error(request,"Don't have permission to delete!")
    return redirect(request.META.get('HTTP_REFERER'))





#  Master Views Start Here






@login_required(login_url='/e-billing/login')
@check_permission()
def addBank(request):
    companyObj=Company.objects.filter(user=request.user)[0]
    units=Bank.objects.filter(company=companyObj)
    if request.method == "POST":
        unitId=request.POST.get('unitId')
        acc_name=request.POST.get('acc_name')
        acc_no=request.POST.get('acc_no')
        bank_name=request.POST.get('bank_name')
        acc_type=request.POST.get('acc_type')
        balance=request.POST.get('balance')
        myStatus=0
        if(acc_name != '' and acc_no != '' and bank_name != ''):
            if(unitId == ''):
                obj=Bank(account_name=acc_name,account_no=acc_no,bank_name=bank_name,account_type=acc_type,opening_balance=balance,company=companyObj)
                myStatus=201
            
                Log(request,f"A Bank account has created, Account Number:{acc_no}")          # Log messages
                
            else:
                obj=Bank(id=unitId,account_name=acc_name,account_no=acc_no,bank_name=bank_name,account_type=acc_type,opening_balance=balance,created_at=Bank.objects.get(pk=unitId).created_at,company=companyObj)
                myStatus=200
                
                Log(request,f"A Bank account has updated, Account Number:{obj.account_no}, ID:#{obj.pk}")          # Log messages
            
            obj.save()
            bank=Bank.objects.latest('id')
            print(bank)
            if(acc_type == "Debit"):
                print("inside debit")
                BankAccountLedger(bank=bank,description="Opening Balance",debit=balance,company=companyObj).save()
                BankAccountLedger(bank=bank,description="Closing Balance",debit=balance,company=companyObj).save()
            else:
                BankAccountLedger(bank=bank,description="Opening Balance",credit=balance,company=companyObj).save()
                BankAccountLedger(bank=bank,description="Closing Balance",credit=balance,company=companyObj).save()
            units=Bank.objects.filter(company=companyObj).values()
            unitsData=list(units)
            

            return JsonResponse({'status':myStatus,"units":unitsData})
        
            # messages.success(request,"New Unit Added ")
        else:
            return JsonResponse({'status':400})
    return render(request,"ebilling/BankPage.html",{"units":units})

@login_required(login_url='/e-billing/login')
@check_permission()
def deleteBank(request):
    if request.method == "POST":
        sid=request.POST.get('sid')
        u=Bank.objects.get(pk=sid)
        Log(request,f"A Bank account has removed, Account Number:{u.account_no}, ID:#{u.pk}")          # Log messages
        u.delete()
        return JsonResponse({'status':200})
    else:
        return JsonResponse({'status':400})

@login_required(login_url='/e-billing/login')
@check_permission()
def editBank(request):
    if request.method == "POST":
        sid=request.POST.get('sid')
        u=Bank.objects.get(pk=sid)
        data={"id":u.id,"acc_name":u.account_name,"acc_no":u.account_no,"bank_name":u.bank_name,"acc_type":u.account_type,"balance":u.opening_balance}
        
        Log(request,f"A Bank account has updated, Account Number:{u.account_no}, ID:#{u.pk}")          # Log messages
        return JsonResponse(data)
    else:
        return JsonResponse({'status':400})


@login_required(login_url='/e-billing/login')
@check_permission()
def viewBankAccounts(request):
    companyObj=Company.objects.filter(user=request.user)[0]
    banks=Bank.objects.filter(company=companyObj)
    data=[]
    i=1
    openingBalanceObj=BankAccountLedger.objects.filter(company=companyObj,bank=banks[0])[0]
    closingBalanceObj=BankAccountLedger.objects.filter(company=companyObj,bank=banks[0])[1]
    for d in banks:
        ac=BankAccountLedger.objects.filter(bank=d,company=companyObj)[2:]
        data.append([i,d,ac])
    if request.method == "POST":
        fromdate=request.POST.get('fromDate')
        to_date=request.POST.get('toDate')
        fromdate=  datetime.datetime.strptime(fromdate, "%d/%m/%Y").strftime("%Y-%m-%d")
        to_date=  datetime.datetime.strptime(to_date, "%d/%m/%Y").strftime("%Y-%m-%d")
        data=[]
        openingBalanceObj=BankAccountLedger.objects.filter(company=companyObj,bank=banks[0])[0]
        closingBalanceObj=BankAccountLedger.objects.filter(company=companyObj,bank=banks[0])[1]
        for d in banks:
            ac=BankAccountLedger.objects.filter(bank=d,date__range=[fromdate,to_date],company=companyObj)[2:]
            data.append([i,d,ac])
        return render(request,"ebilling/banksPage.html",{"opening":openingBalanceObj,"closing":closingBalanceObj,"banks":data})
    return render(request,"ebilling/banksPage.html",{"opening":openingBalanceObj,"closing":closingBalanceObj,"banks":data})



@login_required(login_url='/e-billing/login')
@check_permission()
def addBankAdjustment(request,pk):
    companyObj=Company.objects.filter(user=request.user)[0]
    bank=Bank.objects.filter(id=pk)[0]
    bankAccLedger=BankAccountLedger.objects.filter(bank=bank,company=companyObj)[0]
    banksAdjusts=BankAccountAdjustment.objects.filter(bank=bank,company=companyObj)
    units=BankAccountAdjustment.objects.filter(bank=bank,company=companyObj).values()
    unitsData=list(units)
    if request.method == "POST":
        date=request.POST.get('date',None)
        amount=request.POST.get('amount')
        acc_type=request.POST.get('type')
        remark=request.POST.get('remark',None)
        myStatus=0
        if(amount != ""):
            obj=BankAccountAdjustment(amount=amount,date=date,remark=remark,type=acc_type,company=companyObj,bank=bank)
            closingBalanceObj=BankAccountLedger.objects.filter(company=companyObj,bank=bank)[1]
            if(acc_type == "Debit" ):
                bankAccLedgerDescription="Debit Adjustment"
                if(remark != "None"):
                    bankAccLedgerDescription="Debit Adjustment("+remark+")"
                # openingBalanceObj=BankAccountLedger.objects.filter(company=companyObj,bank=bank)[0]
                
                if(closingBalanceObj.credit is not None):
                    closingBalanceObj.credit=bank.opening_balance-float(amount)
                    closingBalanceObj.debit=None
                    bank.opening_balance=bank.opening_balance-float(amount)
                    bank.account_type="Credit"
                else:
                    closingBalanceObj.debit=(bank.opening_balance+float(amount)) 
                    closingBalanceObj.credit=None
                    bank.opening_balance=bank.opening_balance+float(amount)
                    bank.account_type="Debit"
                closingBalanceObj.save()
                bank.save()
                BankAccountLedger(date=date,description=bankAccLedgerDescription,debit=amount,company=companyObj,bank=bank).save()
            else:
                bankAccLedgerDescription="Credit Adjustment"
                if(remark != "None"):
                    bankAccLedgerDescription="Credit Adjustment("+remark+")"
                if(closingBalanceObj.credit is not None):
                    closingBalanceObj.credit=bank.opening_balance+float(amount)
                    closingBalanceObj.debit=None
                    bank.opening_balance=bank.opening_balance+float(amount)
                    bank.account_type="Credit"
                else:
                    if(float(amount) > bank.opening_balance):
                        closingBalanceObj.credit=(-bank.opening_balance+float(amount)) 
                        closingBalanceObj.debit=None
                        bank.opening_balance=-bank.opening_balance+float(amount)
                        bank.account_type="Credit"
                    else:
                        closingBalanceObj.debit=(bank.opening_balance-float(amount)) 
                        closingBalanceObj.credit=None
                        bank.opening_balance=bank.opening_balance-float(amount)
                        bank.account_type="Debit"
                closingBalanceObj.save()
                bank.save()
                BankAccountLedger(date=date,description=bankAccLedgerDescription,credit=amount,company=companyObj,bank=bank).save()
            myStatus=201
            obj.save()
            
            Log(request ,f"A Bank account adjustment has created, Amount:{obj.amount}, Date: {obj.created_at.__str__()} ")          # Log messages
            
            units=BankAccountAdjustment.objects.filter(bank=bank,company=companyObj).values()
            unitsData=list(units)
            return JsonResponse({'status':myStatus,"units":unitsData,"bankId":bank.id})
            # messages.success(request,"New Unit Added ")
        else:
            return JsonResponse({'status':400})
    return render(request,"ebilling/addAdjustBankAccount.html",{"units":unitsData,"bankId":bank.id})




@login_required(login_url='/e-billing/login')
@check_permission(name="Allow Expense")
def addExpenseType(request):
    units=ExpenseType.objects.all()
    if request.method == "POST":
        unitId=request.POST.get('unitId')
        name=request.POST.get('name')
        isEnabled=request.POST.get('isEnabled')
        myStatus=0
        if(name != ""):
            if(isEnabled == "true"):
                isEnabled=True
            else:
                isEnabled=False
            if(unitId == ''):
                obj=ExpenseType(name=name,is_enabled=isEnabled)
                myStatus=201
                
                Log(request,f"An Expense has added. Name:{obj.name}")          # Log messages


            else:
                obj=ExpenseType(id=unitId,name=name,is_enabled=isEnabled)
                myStatus=200
                
                Log(request ,f"An Expense has updated, Type:{obj.name}.")          # Log messages


            obj.save()
            units=ExpenseType.objects.values()
            unitsData=list(units)

            return JsonResponse({'status':myStatus,"units":unitsData})
            # messages.success(request,"New Unit Added ")
        else:
            return JsonResponse({'status':400})
    return render(request,"ebilling/ExpenseTypePage.html",{"units":units})

@login_required(login_url='/e-billing/login')
@check_permission(name="Allow Expense")
def deleteExpenseType(request):
    if request.method == "POST":
        sid=request.POST.get('sid')
        u=ExpenseType.objects.get(pk=sid)
        Log(request ,f"An Expense has deleted, Type:{u.name}.")          # Log messages
        u.delete()
        return JsonResponse({'status':200})
    else:
        return JsonResponse({'status':400})

@login_required(login_url='/e-billing/login')
@check_permission(name="Allow Expense")
def editExpenseType(request):
    if request.method == "POST":
        sid=request.POST.get('sid')
        u=ExpenseType.objects.get(pk=sid)
        data={"id":u.id,"name":u.name,"is_enabled":u.is_enabled}

        return JsonResponse(data)
    else:
        return JsonResponse({'status':400})


@login_required(login_url='/e-billing/login')
@check_permission()
def addDesignation(request):
    units=Designation.objects.all()
    if request.method == "POST":
        unitId=request.POST.get('unitId')
        name=request.POST.get('name')
        isEnabled=request.POST.get('isEnabled')
        myStatus=0
        if(name != ""):
            if(isEnabled == "true"):
                isEnabled=True
            else:
                isEnabled=False
            if(unitId == ''):
                obj=Designation(name=name,is_enabled=isEnabled)
                myStatus=201
                
                Log(request ,f"A New Designation has created, Name:{obj.name}.")          # Log messages
                


            else:
                obj=Designation(id=unitId,name=name,is_enabled=isEnabled)
                myStatus=200
                
                Log(request ,f"A Designation has updated, Name:{obj.name}.")          # Log messages
                


            obj.save()
            units=Designation.objects.values()
            unitsData=list(units)
            
            return JsonResponse({'status':myStatus,"units":unitsData})
            # messages.success(request,"New Unit Added ")
        else:
            return JsonResponse({'status':400})
    return render(request,"ebilling/DesignationPage.html",{"units":units})

@login_required(login_url='/e-billing/login')
@check_permission()
def deleteDesignation(request):
    if request.method == "POST":
        sid=request.POST.get('sid')
        u=Designation.objects.get(pk=sid)
        Log(request ,f"A New Designation has delete, Name:{u.name}.")          # Log messages
        u.delete()
        return JsonResponse({'status':200})
    else:
        return JsonResponse({'status':400})

@login_required(login_url='/e-billing/login')
@check_permission()
def editDesignation(request):
    if request.method == "POST":
        sid=request.POST.get('sid')
        u=Designation.objects.get(pk=sid)
        data={"id":u.id,"name":u.name,"is_enabled":u.is_enabled}

        return JsonResponse(data)
    else:
        return JsonResponse({'status':400})


@login_required(login_url='/e-billing/login')
@check_permission()
def addDepartment(request):
    units=Department.objects.all()
    if request.method == "POST":
        unitId=request.POST.get('unitId')
        name=request.POST.get('name')
        isEnabled=request.POST.get('isEnabled')
        myStatus=0
        if(name != ""):
            if(isEnabled == "true"):
                isEnabled=True
            else:
                isEnabled=False
            if(unitId == ''):
                obj=Department(name=name,is_enabled=isEnabled)
                myStatus=201
                
                Log(request ,f"A New Department has created, Name:{obj.name}.")          # Log messages

                
            else:
                obj=Department(id=unitId,name=name,is_enabled=isEnabled)
                myStatus=200
                
                Log(request ,f"A Department has modified, Name:{obj.name}.")          # Log messages

                
            obj.save()
            units=Department.objects.values()
            unitsData=list(units)

            return JsonResponse({'status':myStatus,"units":unitsData})
            # messages.success(request,"New Unit Added ")
        else:
            return JsonResponse({'status':400})
    return render(request,"ebilling/DepartmentPage.html",{"units":units})

@login_required(login_url='/e-billing/login')
@check_permission()
def deleteDepartment(request):
    if request.method == "POST":
        sid=request.POST.get('sid')
        u=Department.objects.get(pk=sid)
        Log(request ,f"A Department has deleted, Name:{u.name}.")          # Log messages
        u.delete()
        return JsonResponse({'status':200})
    else:
        return JsonResponse({'status':400})

@login_required(login_url='/e-billing/login')
@check_permission()
def editDepartment(request):
    if request.method == "POST":
        sid=request.POST.get('sid')
        u=Department.objects.get(pk=sid)
        data={"id":u.id,"name":u.name,"is_enabled":u.is_enabled}

        return JsonResponse(data)
    else:
        return JsonResponse({'status':400})

@login_required(login_url='/e-billing/login')
@check_permission()
def addUnit(request):
    units=Unit.objects.all()
    if request.method == "POST":
        unitId=request.POST.get('unitId')
        name=request.POST.get('name')
        isEnabled=request.POST.get('isEnabled')
        myStatus=0
        if(name != ""):
            if(isEnabled == "true"):
                isEnabled=True
            else:
                isEnabled=False
            if(unitId == ''):
                obj=Unit(name=name,is_enabled=isEnabled)
                myStatus=201
                
                Log(request ,f"A new Unit has created, Name:{obj.name}.")          # Log messages
                
            else:
                obj=Unit(id=unitId,name=name,is_enabled=isEnabled)
                myStatus=200
                
                Log(request ,f"A Unit has modified, Name:{obj.name}.")          # Log messages
            
            obj.save()
            units=Unit.objects.values()
            unitsData=list(units)

            return JsonResponse({'status':myStatus,"units":unitsData})
            # messages.success(request,"New Unit Added ")
        else:
            return JsonResponse({'status':400})

        # return redirect(request.META.get('HTTP_REFERER'))
    return render(request,"ebilling/UnitPage.html",{"units":units})


@login_required(login_url='/e-billing/login')
@check_permission()
def deleteUnit(request):
    if request.method == "POST":
        sid=request.POST.get('sid')
        print(sid)
        u=Unit.objects.get(pk=sid)
        Log(request ,f"A Unit has deleted, Name:{u.name}.")          # Log messages
        u.delete()
        return JsonResponse({'status':200})
    else:
        return JsonResponse({'status':400})

@login_required(login_url='/e-billing/login')
@check_permission()
def editUnit(request):
    if request.method == "POST":
        sid=request.POST.get('sid')
        u=Unit.objects.get(pk=sid)
        data={"id":u.id,"name":u.name,"is_enabled":u.is_enabled}

        return JsonResponse(data)
    else:
        return JsonResponse({'status':400})

# @login_required(login_url='/e-billing/login')
# def addBrand1(request):
#     companyObj=Company.objects.filter(user=request.user)[0]
#     brands=Brand.objects.filter(company=companyObj)
#     if request.method == "POST":
#         brandId=request.POST.get('brandId')
#         name=request.POST.get('name')
#         isEnabled=request.POST.get('isEnabled')
#         myStatus=0
#         if(name != ""):
#             if(isEnabled == "true"):
#                 isEnabled=True
#             else:
#                 isEnabled=False
#             if(brandId == ''):
#                 obj=Brand(name=name,is_enabled=isEnabled,company=companyObj)
#                 myStatus=201
#             else:
#                 obj=Brand(id=brandId,name=name,is_enabled=isEnabled,company=companyObj)
#                 myStatus=200
#             obj.save()
#             brands=Brand.objects.filter(company=companyObj).values()
#             brandsData=list(brands)
#             return JsonResponse({'status':myStatus,"brands":brandsData})
#             # messages.success(request,"New Unit Added ")
#         else:
#             return JsonResponse({'status':400})
#     return render(request,"ebilling/BrandPage.html",{"brands":brands})


@login_required(login_url='/e-billing/login')
@check_permission()
def addBrand(request):
    companyObj=Company.objects.filter(user=request.user)[0]
    units=Brand.objects.filter(company=companyObj)
    if request.method == "POST":
        unitId=request.POST.get('unitId')
        name=request.POST.get('name')
        isEnabled=request.POST.get('isEnabled')
        myStatus=0
        if(name != ""):
            if(isEnabled == "true"):
                isEnabled=True
            else:
                isEnabled=False
            if(unitId == ''):
                obj=Brand(name=name,is_enabled=isEnabled,company=companyObj)
                myStatus=201
                
                Log(request ,f"A new Brand has created in this Company, Name:{obj.name}.")          # Log messages
            else:
                obj=Brand(id=unitId,name=name,is_enabled=isEnabled,company=companyObj)
                myStatus=200
                
                Log(request ,f"A Brand has modified, Name:{obj.name}.")          # Log messages
                
            obj.save()
            units=Brand.objects.filter(company=companyObj).values()
            unitsData=list(units)

            return JsonResponse({'status':myStatus,"units":unitsData})
            # messages.success(request,"New Unit Added ")
        else:
            return JsonResponse({'status':400})
    return render(request,"ebilling/BrandPage.html",{"units":units})


@login_required(login_url='/e-billing/login')
@check_permission()
def deleteBrand(request):
    if request.method == "POST":
        sid=request.POST.get('sid')
        u=Brand.objects.get(pk=sid)
        Log(request ,f"A Brand has deleted, Name:{u.name}.")          # Log messages
        u.delete()
        return JsonResponse({'status':200})
    else:
        return JsonResponse({'status':400})

@login_required(login_url='/e-billing/login')
@check_permission()
def editBrand(request):
    if request.method == "POST":
        sid=request.POST.get('sid')
        u=Brand.objects.get(pk=sid)
        data={"id":u.id,"name":u.name,"is_enabled":u.is_enabled}
        Log(request ,f"A Brand has modified, Name:{u.name}.")          # Log messages
        return JsonResponse(data)
    else:
        return JsonResponse({'status':400})


@login_required(login_url='/e-billing/login')
@check_permission()
def addGroup(request):
    companyObj=Company.objects.filter(user=request.user)[0]
    units=Group.objects.filter(company=companyObj)
    if request.method == "POST":
        unitId=request.POST.get('unitId')
        name=request.POST.get('name')
        isEnabled=request.POST.get('isEnabled')
        hsn_sac_code=request.POST.get('hsn_sac_code',None)
        vat=request.POST.get('vat',0)
        myStatus=0
        if(name != ""):
            if(isEnabled == "true"):
                isEnabled=True
            else:
                isEnabled=False
            if(unitId == ''):
                obj=Group(name=name,is_enabled=isEnabled,hsn_or_sac_code=hsn_sac_code,vat=vat,company=companyObj)
                myStatus=201
                
                Log(request ,f"A New Group has created in this Company, Name:{obj.name}, Vat:{obj.vat}.")          # Log messages
                
            else:
                obj=Group(id=unitId,name=name,is_enabled=isEnabled,hsn_or_sac_code=hsn_sac_code,vat=vat,company=companyObj)
                myStatus=200
                
                Log(request ,f"A Group has modified, Name:{obj.name}, Enabled:{obj.is_enabled}.")          # Log messages
                
            obj.save()
            units=Group.objects.filter(company=companyObj).values()
            unitsData=list(units)
            
            
            
            return JsonResponse({'status':myStatus,"units":unitsData})
            # messages.success(request,"New Unit Added ")
        else:
            return JsonResponse({'status':400})
    return render(request,"ebilling/GroupPage.html",{"units":units})

@login_required(login_url='/e-billing/login')
@check_permission()
def deleteGroup(request):
    if request.method == "POST":
        sid=request.POST.get('sid')
        u=Group.objects.get(pk=sid)
        Log(request ,f"A Group has deleted, Name:{u.name}.")          # Log messages
        u.delete()
        return JsonResponse({'status':200})
    else:
        return JsonResponse({'status':400})

@login_required(login_url='/e-billing/login')
@check_permission()
def editGroup(request):
    if request.method == "POST":
        sid=request.POST.get('sid')
        u=Group.objects.get(pk=sid)
        data={"id":u.id,"name":u.name,"vat":u.vat,"hsn_sac_code":u.hsn_or_sac_code,"is_enabled":u.is_enabled,}
        Log(request ,f"A Group has modified, Name:{u.name}, Enabled:{u.is_enabled}.")          # Log messages
        return JsonResponse(data)
    else:
        return JsonResponse({'status':400})



@login_required(login_url='/e-billing/login')
@check_permission(name="Allow Purchase")
def draftNewPurchase(request):
    
    companyObj=Company.objects.filter(user=request.user)[0]
   
    suppliers=Supplier.objects.filter(company=companyObj)
    products=Product.objects.filter(company=companyObj)

    if request.method == "POST":
        print(request.POST)
        sName=request.POST.get('supplierName')
        purchaseType=request.POST.get('purchaseType')
        billDate=request.POST.get('billDate')

        paymentTerms=request.POST.get('paymentTerms')
        dueDate=request.POST.get('dueDate')
        placeOfSupply=request.POST.get('placeOfSupply')
        purchaseBillNo=request.POST.get('purchaseBillNo')

        purchaseOrderDate=request.POST.get('placeOfSupply')
        purchaseOrderNo=request.POST.get('purchaseOrderNo')
        eWayBillNo=request.POST.get('eWayBillNo')
        payMode=request.POST.get('payMode')
        ref_no=request.POST.get('ref_no')
        amountPaid=request.POST.get('amountPaid')
        balance=request.POST.get('balance')
        remark=request.POST.get('remark')
        p = Purchase(type=purchaseType,bill_date=billDate,supplier=sName,payment_terms=paymentTerms,due_date=dueDate,
        place_of_supply=placeOfSupply,bill_no=purchaseBillNo,order_no=purchaseOrderNo,
        order_date=purchaseOrderDate,e_way_bill_no=eWayBillNo,pay_mode=payMode,transaction_id=ref_no,
        amount_paid=amountPaid,balance=balance,
        )
        particularsData= request.POST.getlist("data[]")
        
        Log(request ,f"A New Item has Purchased, Purchase ID: #{p.id}, Amount Paid: {p.amount_paid}, Order No: {p.order_no}")          # Log messages
        


    return render(request,"ebilling/DraftPurchasePage.html",{"suppliers":suppliers,"products":products})








@login_required(login_url='/e-billing/login')
@check_permission(name="Allow Dashboard")
def dashboardPage(request):
    return render(request,"ebilling/Homepage.html")






@login_required(login_url='/e-billing/login')
@check_permission()
def categoryPage(request):
    cats_type=CategoryType.objects.all()
    cats=Category.objects.all()
    if request.method == 'POST':
        name=request.POST['name']
        type=request.POST['type']
        color=request.POST['color']
        is_enabled=request.POST['is_enabled']
        if(is_enabled == "on"):
            is_enabled=True 
        else:
            is_enabled=False
        Category(name=name,type=CategoryType.objects.filter(id=type)[0],color=color,is_enabled=is_enabled).save()
        messages.success(request,"New Category Type Added !")
        return redirect(request.META.get('HTTP_REFERER'))

    return render(request,"ebilling/category_page.html",{"cats_type":cats_type,"cats":cats})

@login_required(login_url='/e-billing/login')
@check_permission()
def categoryTypePage(request):
    cat_types=CategoryType.objects.all();
    if request.method == 'POST':
        name=request.POST['name']
        is_enabled=request.POST['is_enabled']
        if(is_enabled == "on"):
            is_enabled=True 
        else:
            is_enabled=False
        CategoryType(name=name,is_enabled=is_enabled).save()
        messages.success(request,"New Category Type Added !")
        return redirect(request.META.get('HTTP_REFERER'))

    return render(request,"ebilling/category_type_page.html", {"cat_types":cat_types})



@login_required(login_url='/e-billing/login')
@check_permission()
def settingsPage(request):
    return render(request,"ebilling/SettingsPage.html")

@login_required(login_url='/e-billing/login')
@check_permission()
def taxesPage(request):
    try:
        taxes=Tax.objects.all()
    except:
        taxes=[]
    return render(request,"ebilling/TaxesPage.html",{"taxes":taxes})

@login_required(login_url='/e-billing/login')
@check_permission()
def createUpdateTax(request):
    taxTypes=TaxType.objects.all()
    if request.method == 'POST':
        name=request.POST['tname']
        type=request.POST['type']
        rate=request.POST['rate']
        is_enabled=request.POST['is_enabled']
        if(is_enabled == "on"):
            is_enabled=True 
        else:
            is_enabled=False
        if(len(Tax.objects.filter(name=name))>0):
            t=Tax.objects.filter(name=name)[0]
            t.name=name
            t.type=TaxType.objects.filter(id=type)[0]
            t.rate=rate 
            t.is_enabled=is_enabled
            t.save()
            Log(request ,f"A New Tax has modified, Name: {t.name}.")          # Log messages
            messages.success(request,"Tax Updated!")
            return redirect("ebilling:taxes")
        else:
            t = Tax(name=name,rate=rate,type=TaxType.objects.filter(id=type)[0],is_enabled=is_enabled)
            t.save()
            print(t)
            Log(request ,f"A New Tax has Created!, Name:{t.name}.")          # Log messages
            messages.success(request,"Tax Created!")
            return redirect("ebilling:taxes")
    return render(request,"ebilling/Add_Edit_Tax.html",{"tax_type":taxTypes})


@login_required(login_url='/e-billing/login')
@check_permission()
def addProduct(request):
    company=Company.objects.filter(user=request.user)[0]
    groups=Group.objects.filter(company=company)
    brands=Brand.objects.filter(company=company)
    units=Unit.objects.all()
    item_type=ItemCategory.objects.all()
   
    if request.method == "POST":
        if request.FILES:
            item_pic=request.FILES['sample']    
        groupID=request.POST.get('group')
        if(groupID != ''):
            group=Group.objects.filter(id=groupID,company=company)[0]
        brandID=request.POST.get('brand')
        if(brandID != ''):
            brand=Brand.objects.filter(id=brandID)[0]
        name = request.POST.get('name')
        print_name = request.POST.get('print_name')
        item_code=request.POST.get('item_code',None)
        sale_price = request.POST.get('sale_price')
        purchase_price=request.POST.get('purchase_price')
        min_sale_price=request.POST.get('min_sale_price',0)
        mrp=request.POST.get('mrp',0)
        unitID=request.POST.get('unit')
        if(unitID != ''):
            unit=Unit.objects.filter(id=unitID)[0]
        opening_stock=request.POST.get('opening_stock',0)
        opening_stock_value=request.POST.get('opening_stock_value',None)
        hsn_sac_code=request.POST.get('hsn_sac_code',None)
        vat=request.POST.get('vat')
        item_typeID=request.POST.get('item_type')
        if(item_typeID != ''):
            item_type=ItemCategory.objects.filter(id=item_typeID)[0]
        serial_no=request.POST.get('serial_no',None)
       
        sale_discount=request.POST.get('sale_discount')
        if(sale_discount == ''):
            sale_discount=0
        description=request.POST.get('description',None)
        isPrintDescription=request.POST.get('isPrintDescription')
        if(isPrintDescription == "on"):
            isPrintDescription=True
        else:
            isPrintDescription=False

        one_click_sale=request.POST.get('one_click_sale')
        if(one_click_sale == "on"):
            one_click_sale=True
        else:
            one_click_sale=False

        enable_tracking=request.POST.get('enable_tracking')
        if(enable_tracking == "on"):
            enable_tracking=True
        else:
            enable_tracking=False
        print_serial_no=request.POST.get('print_serial_no')
        if(print_serial_no == "on"):
            print_serial_no=True
        else:
            print_serial_no=False
        not_for_sale=request.POST.get('not_for_sale')
        if(not_for_sale == "on"):
            not_for_sale=True
        else:
            not_for_sale=False
        try:
            p=Product(group=group,brand=brand,item_code=item_code,name=name,print_name=print_name,sale_price=sale_price,purchase_price=purchase_price,min_sale_price=min_sale_price,mrp=mrp,unit=unit,opening_stock=opening_stock,opening_stock_price=opening_stock_value,
            hsn_or_sac_code=hsn_sac_code,vat=vat,category=item_type,serial_no=serial_no,discount=sale_discount,description=description,picture=item_pic,is_print_description=isPrintDescription,
            is_one_click_sale=one_click_sale,is_enabled_for_tracking=enable_tracking,is_print_serial_no=print_serial_no,is_not_for_sale=not_for_sale,company=company)
        except:
            p=Product(group=group,brand=brand,item_code=item_code,name=name,print_name=print_name,sale_price=sale_price,purchase_price=purchase_price,min_sale_price=min_sale_price,mrp=mrp,unit=unit,opening_stock=opening_stock,opening_stock_price=opening_stock_value,
            hsn_or_sac_code=hsn_sac_code,vat=vat,category=item_type,serial_no=serial_no,discount=sale_discount,description=description,is_print_description=isPrintDescription,
            is_one_click_sale=one_click_sale,is_enabled_for_tracking=enable_tracking,is_print_serial_no=print_serial_no,is_not_for_sale=not_for_sale,company=company)
        p.save()
        StockSummary(product=Product.objects.latest('id'),opening_qty=0,inward_qty=opening_stock,outward_qty=0,closing_qty=opening_stock,net_change=opening_stock,company=company).save()
        messages.success(request,"New Item Added :"+name)
        Log(request ,f"A New Product Item has Added!, Item Code: {p.item_code}, Sale price: {p.sale_price} Opening stock: {p.opening_stock}.")          # Log messages
        return redirect(request.META.get('HTTP_REFERER'))
        
    return render(request,"ebilling/AddProductPage.html",{"groups":groups,"units":units,"brands":brands,"categories":item_type})

@login_required(login_url='/e-billing/login')
@check_permission()
def editProduct(request,pk):
    company=Company.objects.filter(user=request.user)[0]
    groups=Group.objects.filter(company=company)
    brands=Brand.objects.filter(company=company)
    units=Unit.objects.all()
    item_type=ItemCategory.objects.all()
    product=Product.objects.filter(id=pk)[0]
    if request.method == "POST":
        if request.FILES:
            product.picture=request.FILES['sample']    
        groupID=request.POST.get('group')
        if(groupID != ''):
            product.group=Group.objects.filter(id=groupID,company=company)[0]
        brandID=request.POST.get('brand')
        if(brandID != ''):
            product.brand=Brand.objects.filter(id=brandID)[0]
        product.name = request.POST.get('name')
        product.print_name = request.POST.get('print_name')
        product.item_code=request.POST.get('item_code',None)
        product.sale_price = request.POST.get('sale_price')
        product.purchase_price=request.POST.get('purchase_price')
        product.min_sale_price=request.POST.get('min_sale_price',None)
        product.mrp=request.POST.get('mrp',None)
        unitID=request.POST.get('unit')
        if(unitID != ''):
            product.unit=Unit.objects.filter(id=unitID)[0]
        product.opening_stock=request.POST.get('opening_stock',0)
        product.opening_stock_value=request.POST.get('opening_stock_value',None)
        product.hsn_or_sac_code=request.POST.get('hsn_sac_code',None)
        product.vat=request.POST.get('vat')
        item_typeID=request.POST.get('item_type')
        if(item_typeID != ''):
            product.category=ItemCategory.objects.filter(id=item_typeID)[0]
        product.serial_no=request.POST.get('serial_no',None)
        product.discount=request.POST.get('sale_discount',0)
        product.description=request.POST.get('description',None)
        isPrintDescription=request.POST.get('isPrintDescription')
        if(isPrintDescription == "on"):
            product.is_print_description=True
        else:
            product.is_print_description=False

        one_click_sale=request.POST.get('one_click_sale')
        if(one_click_sale == "on"):
            product.is_one_click_sale=True
        else:
            product.is_one_click_sale=False

        enable_tracking=request.POST.get('enable_tracking')
        if(enable_tracking == "on"):
            product.is_enabled_for_tracking=True
        else:
            product.is_enabled_for_tracking=False
        print_serial_no=request.POST.get('print_serial_no')
        if(print_serial_no == "on"):
            product.is_print_serial_no=True
        else:
            product.is_print_serial_no=False
        not_for_sale=request.POST.get('not_for_sale')
        if(not_for_sale == "on"):
            product.is_not_for_sale=False
        else:
            product.is_not_for_sale=False
        product.save()
        messages.success(request,"Product Details Updated")
        Log(request ,f"A Product Item has modified, Name: {product.name}, Serial No: {product.serial_no},")          # Log messages
        return redirect("ebilling:searchManageProductService")
        
    return render(request,"ebilling/addProductPage.html",{"groups":groups,"units":units,"brands":brands,"categories":item_type,"product":product})


@login_required(login_url='/e-billing/login')
@check_permission()
def addService(request):
    company=Company.objects.filter(user=request.user)[0]
    groups=Group.objects.filter(company=company)
    if request.method == "POST":
        groupID=request.POST.get('group')
        if(groupID != ''):
            group=Group.objects.filter(id=groupID,company=company)[0]
        name = request.POST.get('name')
        print_name = request.POST.get('print_name')
        item_code=request.POST.get('item_code',None)
        service_charge = request.POST.get('service_charge')
        min_service_charge=request.POST.get('min_service_charge')
        unit=Unit.objects.filter(name="NOS")[0]
        hsn_sac_code=request.POST.get('hsn_sac_code',None)
        vat=request.POST.get('vat')
        sale_discount=request.POST.get('sale_discount',0)
        description=request.POST.get('description',None)
        isPrintDescription=request.POST.get('isPrintDescription')
        if(isPrintDescription == "on"):
            isPrintDescription=True
        else:
            isPrintDescription=False 
       
        s = Service(group=group,item_code=item_code,name=name,print_name=print_name,service_charge=service_charge,min_service_charge=min_service_charge,unit=unit,
            hsn_or_sac_code=hsn_sac_code,vat=vat,discount=sale_discount,decription=description,is_print_description=isPrintDescription,
           company=company)
        s.save()
        messages.success(request,"New Service Added : "+name)
        Log(request ,f"A New Service Item has Added!, Name:{s.name}, Vat:{s.vat}, Service Charge:{s.service_charge}.")          # Log messages
        return redirect(request.META.get('HTTP_REFERER'))
        
    return render(request,"ebilling/AddServicePage.html",{"groups":groups})


@login_required(login_url='/e-billing/login')
@check_permission()
def editService(request,pk):
    company=Company.objects.filter(user=request.user)[0]
    groups=Group.objects.filter(company=company)
    service=Service.objects.filter(id=pk)[0]
    if request.method == "POST":
        groupID=request.POST.get('group')
        if(groupID != ''):
            service.group=Group.objects.filter(id=groupID,company=company)[0]
        service.name = request.POST.get('name')
        service.print_name = request.POST.get('print_name')
        service.item_code=request.POST.get('item_code',None)
        service.service_charge = request.POST.get('service_charge')
        service.min_service_charge=request.POST.get('min_service_charge')
        service.unit=Unit.objects.filter(name="NOS")[0]
        service.hsn_or_sac_code=request.POST.get('hsn_sac_code',None)
        service.vat=request.POST.get('vat')
        service.discount=request.POST.get('sale_discount',0)
        service.decription=request.POST.get('description',None)
        isPrintDescription=request.POST.get('isPrintDescription')
        if(isPrintDescription == "on"):
            service.is_print_description=True
        else:
            service.is_print_description=False 
        service.save()
        messages.success(request,"Service Updated ")
        Log(request ,f"A Service Item has modified, Name: {service.name}, Service Charge: {service.service_charge}, Vat: {service.vat}.")          # Log messages
        return redirect('ebilling:searchManageProductService')
    return render(request,"ebilling/addServicePage.html",{"groups":groups,"service":service})


@login_required(login_url='/e-billing/login')
@check_permission()
def deleteService(request,pk):
    service=Service.objects.filter(id=pk,company=Company.objects.filter(user=User.objects.filter(id=request.user.id)[0])[0])
    if(len(service)>0):
        Log(request ,f"A Service Item has deleted!, Name:{service[0].name}.")          # Log messages
        service[0].delete()
        messages.success(request,"Service deleted")
    else:
        messages.error(request,"Don't have permission to delete!")
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/e-billing/login')
@check_permission()
def deleteProduct(request,pk):
    product=Product.objects.filter(id=pk,company=Company.objects.filter(user=User.objects.filter(id=request.user.id)[0])[0])
    if(len(product)>0):
        Log(request ,f"A product Item has deleted!, Name:{product[0].name}, Item Code:{product[0].item_code}.")          # Log messages
        product[0].delete()
        messages.success(request,"Product deleted")
    else:
        messages.error(request,"Don't have permission to delete!")
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/e-billing/login')
@check_permission()
def SearchManageProductAndServicePage(request):
    company=Company.objects.filter(user=request.user)[0]
    products=Product.objects.filter(company=company)
    services=Service.objects.filter(company=company)
    data=[]
    i=1
    for d in products:
        data.append([i,"Product",d.group.name,d.brand.name,d.name,d.print_name,d.unit.name,d.purchase_price,d.sale_price,d.min_sale_price,d.mrp,d.hsn_or_sac_code,d.vat,d.discount,d.id])
        i+=1
    for d in services:
        data.append([i,"Service",d.group.name,"None",d.name,d.print_name,d.unit.name,"None","None","Null","Null",d.hsn_or_sac_code,d.vat,d.discount,d.id])
        i+=1
    return render(request,"ebilling/SearchAndManageProductService.html",{"mydata":data})

@login_required(login_url='/e-billing/login')
@check_permission()
def StockSummaryPage(request):
    try:
        company=Company.objects.filter(user=request.user)[0]
        data=[]
        i=1
        if request.method == 'POST':
            groupName=request.POST.get('group',None)
            brandName=request.POST.get('brand',None)
            itemName=request.POST.get('name',None)
            # clients=Client.objects.filter(Q(id__icontains=ID) | Q(name__icontains=fname) | Q(mobile__icontains=phone))
            if(groupName and len(Product.objects.filter(group=Group.objects.filter(name__icontains=groupName)[0],company=company))>0 ):
                products=Product.objects.filter(group=Group.objects.filter(name__icontains=groupName)[0],company=company)
            elif(brandName and len(Product.objects.filter(brand=Brand.objects.filter(name__icontains=brandName)[0],company=company))>0 ):
                products=Product.objects.filter(brand=Brand.objects.filter(name__icontains=brandName)[0],company=company)
            elif(itemName and len(Product.objects.filter(name=itemName,company=company))>0 ):
                products=Product.objects.filter(name__icontains=itemName,company=company)
            else:
                products=[]
            if(len(products) > 0):
                for d in products:
                    pStock=StockSummary.objects.filter(product=d,company=company)[0]
                    data.append([i,pStock.product.name,pStock.opening_qty,pStock.inward_qty,pStock.outward_qty,pStock.closing_qty,pStock.net_change])
            else:
                data=[]
            return render(request,"ebilling/stock_summary_page.html",{"mydata":data})
    except:
        data=[]

    return render(request,"ebilling/stock_summary_page.html",{"mydata":data})






# Reports View Start Here 

@login_required(login_url='/e-billing/login')
@check_permission()
def clientAmountDueReport(request):
    clientResult=Client.objects.filter(company=Company.objects.filter(user=User.objects.filter(id=request.user.id)[0])[0],account_type="Debit").order_by('-opening_balance')
    totalDueAmount=0
    for d in clientResult:
        totalDueAmount+=d.opening_balance

    return render(request,"ebilling/client_amount_dueReportPage.html",{"clients":clientResult,"dueAmount":totalDueAmount})

@login_required(login_url='/e-billing/login')
@check_permission()
def supplierAccountBalanceReport(request):
    supplierResult=Supplier.objects.filter(company=Company.objects.filter(user=User.objects.filter(id=request.user.id)[0])[0]).order_by('-opening_balance')
    amountBalance=0
    for d in supplierResult:
        if(d.account_type == "Debit"):
            amountBalance+=d.opening_balance
        else:
            amountBalance-=d.opening_balance
    return render(request,"ebilling/supplier_account_balanceReportPage.html",{"suppliers":supplierResult,"amountbalance":amountBalance})

from datetime import date
@login_required(login_url='/e-billing/login')
@check_permission()
def expensesReport(request):
    userCompany=Company.objects.filter(user=User.objects.filter(id=request.user.id)[0])[0]
    expenseType=ExpenseType.objects.all()
    expenses=Expense.objects.filter(company=userCompany)
    setGlobalExpensesResultSet(expenses)
    totalAmount=0
    amountInCash=0
    amountThroughBank=0
    amountThroughOthers=0
    for e in expenses:
        totalAmount+=int(e.amount)
        if(e.pay_mode == "Cash"):
            amountInCash+=int(e.amount)
        elif(e.pay_mode == "Bank"):
            amountThroughBank+=int(e.amount)
        else:
            amountThroughOthers+=int(e.amount)
    if request.method == "POST":
        eType = request.POST.get('expense_type')
        paidTo = request.POST.get('paid_to')
        paidBy = request.POST.get('paid_by')
        payMode=request.POST.get('pay_mode')
        fromdate=request.POST.get('from_date')
        to_date=request.POST.get('to_date')
        fromdate=  datetime.datetime.strptime(fromdate, "%d/%m/%Y").strftime("%Y-%m-%d")
        to_date=  datetime.datetime.strptime(to_date, "%d/%m/%Y").strftime("%Y-%m-%d")
        setFromDateAndToDate(fromdate,to_date)
        if(eType != "None" and len(Expense.objects.filter(expense_type=ExpenseType.objects.filter(name=eType)[0],date__range=[fromdate,to_date],company=userCompany))>0):
            expenses=Expense.objects.filter(expense_type=ExpenseType.objects.filter(name=eType)[0],date__range=[fromdate,to_date],company=userCompany)
            setGlobalExpensesResultSet(expenses)
            totalAmount=0
            amountInCash=0
            amountThroughBank=0
            amountThroughOthers=0
            for e in expenses:
                totalAmount+=int(e.amount)
                if(e.pay_mode == "Cash"):
                    amountInCash+=int(e.amount)
                elif(e.pay_mode == "Bank"):
                    amountThroughBank+=int(e.amount)
                else:
                    amountThroughOthers+=int(e.amount)
        elif(paidTo != "" and len(Expense.objects.filter(Q(paid_to__icontains=paidTo),date__range=[fromdate,to_date],company=userCompany))>0):
            expenses = Expense.objects.filter(Q(paid_to__icontains=paidTo),date__range=[fromdate,to_date],company=userCompany)
            setGlobalExpensesResultSet(expenses)
            totalAmount=0
            amountInCash=0
            amountThroughBank=0
            amountThroughOthers=0
            for e in expenses:
                totalAmount+=int(e.amount)
                if(e.pay_mode == "Cash"):
                    amountInCash+=int(e.amount)
                elif(e.pay_mode == "Bank"):
                    amountThroughBank+=int(e.amount)
                else:
                    amountThroughOthers+=int(e.amount)
        elif(paidBy != "" and len(Expense.objects.filter(Q(paid_by__icontains=paidBy),date__range=[fromdate,to_date],company=userCompany))>0):
            expenses = Expense.objects.filter(Q(paid_by__icontains=paidBy),date__range=[fromdate,to_date],company=userCompany) 
            setGlobalExpensesResultSet(expenses)
            totalAmount=0
            amountInCash=0
            amountThroughBank=0
            amountThroughOthers=0
            for e in expenses:
                totalAmount+=int(e.amount)
                if(e.pay_mode == "Cash"):
                    amountInCash+=int(e.amount)
                elif(e.pay_mode == "Bank"):
                    amountThroughBank+=int(e.amount)
                else:
                    amountThroughOthers+=int(e.amount)
        elif(payMode != "Any" and len(Expense.objects.filter(pay_mode=payMode,date__range=[fromdate,to_date],company=userCompany))>0):
            expenses = Expense.objects.filter(pay_mode=payMode,date__range=[fromdate,to_date],company=userCompany)
            setGlobalExpensesResultSet(expenses)
            totalAmount=0
            amountInCash=0
            amountThroughBank=0
            amountThroughOthers=0
            for e in expenses:
                totalAmount+=int(e.amount)
                if(e.pay_mode == "Cash"):
                    amountInCash+=int(e.amount)
                elif(e.pay_mode == "Bank"):
                    amountThroughBank+=int(e.amount)
                else:
                    amountThroughOthers+=int(e.amount)
    return render(request,"ebilling/expensesReportPage.html",{"expenses":expenses,"expenseType":expenseType,"TotalAmount":totalAmount,"amountInCash":amountInCash,"amountThroughBank":amountThroughBank,"amountThroughOthers":amountThroughOthers})







# All Export Links Views will start from here 
@login_required(login_url='/e-billing/login')
@check_permission()
def exportClientDueAmountReportExcel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Client_Due_Amount_Report.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Clients')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = xlwt.Style.colour_map['pale_blue']
    font_style.pattern = pattern
    font_style.font.bold = True

    columns = ['Client Name', 'A/c Balance', 'City','Contact No.', 'Address' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Client.objects.filter(company=Company.objects.filter(user=User.objects.filter(id=request.user.id)[0])[0],account_type="Debit").order_by('-opening_balance').values_list('fullname', 'opening_balance', 'city','mobile','billing_address')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


@login_required(login_url='/e-billing/login')
@check_permission()
def exportSupplierAccountBalancesReportExcel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Supplier_Account_Balance_Report.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Suppliers Account Balances')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = xlwt.Style.colour_map['pale_blue']
    font_style.pattern = pattern
    font_style.font.bold = True

    columns = ['Supplier Name',  'City','District', 'Province', 'A/c Balance']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    rows=Supplier.objects.filter(company=Company.objects.filter(user=User.objects.filter(id=request.user.id)[0])[0]).order_by('-opening_balance').values_list('company_name','city','district','province', 'opening_balance')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


@login_required(login_url='/e-billing/login')
@check_permission()
def exportExpensesSearchResultReportExcel(request):
    response = HttpResponse(content_type='application/ms-excel')
    dateRange=getFromDateAndToDate()
    if(dateRange[0] == '' and dateRange[1] == ''):
        fileName="Expenses_Report.xls"
    else:
        fileName="ExpensesReport_from_"+dateRange[0] +"_to_"+dateRange[1]+".xls"
  
    response['Content-Disposition'] = 'attachment; filename='+fileName

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Expenses')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = xlwt.Style.colour_map['pale_blue']
    font_style.pattern = pattern
    font_style.font.bold = True

    columns = ['S.No','Date', 'Type', 'Amount','Paid To', 'Paid By','Mode','Payment Ref.','Remark','User']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    data=getGlobalExpensesResultSet()
    if(len(data)>0):
        rows = []
        c=0
        for dd in data:
            c+=1
            rows.append([c,str(dd.date),dd.expense_type.name,dd.amount,dd.paid_to,dd.paid_by,dd.pay_mode,dd.pay_ref_no,dd.remark,dd.company.user.username])
    else:
        messages.error(request,"Empty Search Result, Search Again")
        return redirect(request.META.get('HTTP_REFERER'))
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    setGlobalExpensesResultSet(data)
    return response







@login_required(login_url='/e-billing/login')
@check_permission()
def exportClientDueAmountReportPdf(request):

    company=Company.objects.filter(user=User.objects.filter(id=request.user.id)[0])[0]
    rows = Client.objects.filter(company=Company.objects.filter(user=User.objects.filter(id=request.user.id)[0])[0],account_type="Debit").order_by('-opening_balance').values_list('fullname', 'mobile','city','opening_balance' )
    data=[]
    i=1
    for d in rows:
        data.append([i,d[0],d[1],d[2],d[3]])
        i+=1
    context={"companyName":company.name,"reportName":"CLIENT AMOUNT DUE",
    "address":company.address,"title":"Client Due Amount - Report","columns":["S.NO","CLIENT NAME","CONTACT NO.","CITY","BALANCE DUE"],"data":data
    }

    pdf = render_to_pdf('ebilling/exportHtmlToPdfTemplate/pdfTemplate.html', context)
    return HttpResponse(pdf, content_type='application/pdf')
    
    


@login_required(login_url='/e-billing/login')
@check_permission()
def exportExpensesSearchResultReportPdf(request):
    dateRange=getFromDateAndToDate()
    myDate="From "+dateRange[0]+" To "+dateRange[1]
    data=getGlobalExpensesResultSet()
    company=Company.objects.filter(user=User.objects.filter(id=request.user.id)[0])[0]
    totalAmount=0
    if(len(data)>0):
        rows = []
        c=0
        for dd in data:
            c+=1
            totalAmount+=int(dd.amount)
            rows.append([c,str(dd.date),dd.expense_type.name,dd.paid_to,dd.paid_by,dd.pay_mode,dd.pay_ref_no,dd.company.user.username,dd.amount])
        rows.append(["","","","","","","","Total :",totalAmount])
    context={"companyName":company.name,"reportName":"EXPENSES","from_to_Date":myDate,
    "address":company.address,"title":"Expenses - Report","columns": ['S.NO.','DATE', 'TYPE','PAID TO', 'PAID BY','MODE','PAYMENT REF.','USER','AMOUNT'],"data":rows
    }

    pdf = render_to_pdf('ebilling/exportHtmlToPdfTemplate/pdfTemplate.html', context)
    return HttpResponse(pdf, content_type='application/pdf')
    








from django.apps import apps 
from django.db import connection
from django.contrib import admin 
from django.contrib.admin.sites import AlreadyRegistered 

# django logged in user backup view 
@login_required(login_url='/e-billing/login')
@check_permission()
def getUserBackUp(request):
    table_info = []
    tables = connection.introspection.table_names()
    seen_models = connection.introspection.installed_models(tables)
    for model in apps.get_models():
        if model._meta.proxy:
            continue

        table = model._meta.db_table
        if table not in tables:
            continue

        columns = [field.column for field in model._meta.fields]
        table_info.append((table, columns))
    print(table_info)

    print("======================")

    for model in apps.get_models():
        for field in model._meta.local_many_to_many:
            # if not field.creates_table:
            #     continue

            table = field.m2m_db_table()
            if table not in tables:
                continue
            columns = ['id'] # They always have an id column
            columns.append(field.m2m_column_name())
            columns.append(field.m2m_reverse_name())
            table_info.append((table, columns))
    print(table_info)
    return HttpResponse(200);












from ebilling.serializer import *
from json import dumps,loads
from datetime import datetime
@login_required(login_url='/e-billing/login')
@check_permission()
def backup_restore(request):

        backup_file_data = {"user":request.user.pk}                                              #BACKUP PART
        get_r = request.GET
        if get_r.get("download_backup"):
            company_obj = Company.objects.filter(user=request.user)[0]
            
            Company__serializer = CompanySRZ(company_obj, many=False)
            Bank__serializer = BankSRZ(Bank.objects.filter(company=company_obj),many=True)
            Brand__serializer = BrandSRZ(Brand.objects.filter(company=company_obj),many=True)
            Client__serializer = ClientSRZ(Client.objects.filter(company=company_obj),many=True)
            
            
            
            Supplier__serializer = SupplierSRZ(Supplier.objects.filter(company=company_obj),many=True)
            Group__serializer = GroupSRZ(Group.objects.filter(company=company_obj),many=True)
            Product__serializer = ProductSRZ(Product.objects.filter(company=company_obj),many=True)
            Particular__serializer = ParticularSRZ(Particular.objects.filter(company=company_obj),many=True)
            Purchase__serializer = PurchaseSRZ(Purchase.objects.filter(company=company_obj),many=True)
            Stock_summary__serializer = Stock_summarySRZ(StockSummary.objects.filter(company=company_obj),many=True)
            Bank_account_adjustment__serializer = Bank_account_adjustmentSRZ(BankAccountAdjustment.objects.filter(company=company_obj),many=True)
            Bank_account_ledger__serializer = Bank_account_ledgerSRZ(BankAccountLedger.objects.filter(company=company_obj),many=True)
            Expense__serializer = ExpenseSRZ(Expense.objects.filter(company=company_obj),many=True)
            CashBookAdjustment__serializer = CashBookAdjustmentSRZ(CashBookAdjustment.objects.filter(company=company_obj),many=True)
            Service__serializer = ServiceSRZ(Service.objects.filter(company=company_obj),many=True)
            CashBook__serializer = CashBookSRZ(CashBook.objects.filter(company=company_obj),many=True)

            
            backup_file_data.update({
                "Company":Company__serializer.data,
                "Client":Client__serializer.data,
                "Supplier":Supplier__serializer.data,
                "Expense": Expense__serializer.data,
                "Brand":Brand__serializer.data,
                "Group":Group__serializer.data,
                "Bank":Bank__serializer.data,
                "Product":Product__serializer.data,
                "Service":Service__serializer.data,
                "StockSummary":Stock_summary__serializer.data,
                "BankAccountLedger":Bank_account_ledger__serializer.data,
                "BankAccountAdjustment":Bank_account_adjustment__serializer.data,
                "CashBook":CashBook__serializer.data,
                "CashBookAdjustment":CashBookAdjustment__serializer.data,
                "Particular":Particular__serializer.data,
                "Purchase":Purchase__serializer.data,
            })
            
            backup_file_data = dumps(backup_file_data)
            response = HttpResponse(backup_file_data,content_type='application/json')
            response['Content-Disposition'] = f'attachment; filename={request.user.username}({datetime.now()}).sbu'
            return response
        
        
        
        
        
        
        
                                                  #RESTORE PART
        if request.method == "POST":
            backup_file = loads(request.FILES["backUpFile"].read().decode("utf-8"))
            
            if backup_file['user'] == request.user.pk:          #checking user (validation)
                
                # restoring  company table
                a = CompanySRZ(data=backup_file['Company'])
                if a.is_valid():
                    data = a.data
                    data.update({"user":request.user,"id":backup_file['Company']['id']})
                    Company.objects.update_or_create(user=request.user,defaults=data)
                    
                    
                    
                # restoring  Bank table
                a = BankSRZ(data=backup_file['Bank'],many=True)
                if a.is_valid():
                    for i in backup_file['Bank']:
                        i.update({"company":Company.objects.get(pk=i['company'])})
                        Bank.objects.update_or_create(pk=i["id"],defaults=i)
                
                
                
                # restoring  Brand table
                a = BrandSRZ(data=backup_file['Brand'],many=True)
                if a.is_valid():
                    for i in backup_file['Brand']:
                        i.update({"company":Company.objects.get(pk=i['company'])})
                        Brand.objects.update_or_create(pk=i["id"],defaults=i)
                        
                        
                        
                # restoring  Client table
                a = ClientSRZ(data=backup_file['Client'],many=True)
                if a.is_valid():
                    for i in backup_file['Client']:
                        i.update({"company":Company.objects.get(pk=i['company'])})
                        Client.objects.update_or_create(pk=i["id"],defaults=i)
                        
                        
                # restoring  Supplier table
                a = SupplierSRZ(data=backup_file['Supplier'],many=True)
                if a.is_valid():
                    for i in backup_file['Supplier']:
                        i.update({"company":Company.objects.get(pk=i['company'])})
                        Supplier.objects.update_or_create(pk=i["id"],defaults=i)


                # restoring  Group table
                a = GroupSRZ(data=backup_file['Group'],many=True)
                if a.is_valid():
                    for i in backup_file['Group']:
                        i.update({"company":Company.objects.get(pk=i['company'])})
                        Group.objects.update_or_create(pk=i["id"],defaults=i)
                        


                # restoring  Product table
                a = ProductSRZ(data=backup_file['Product'],many=True)
                if a.is_valid():
                    for i in backup_file['Product']:
                        i.update({
                                "company":Company.objects.get(pk=i['company']),
                                "unit":Unit.objects.get(pk=i['unit']),
                                "brand":Brand.objects.get(pk=i['brand']),
                                "group":Group.objects.get(pk=i['group']),
                                "category":ItemCategory.objects.get(pk=i['category'])
                                  })
                        Product.objects.update_or_create(pk=i["id"],defaults=i)

        
           
                        
                        
                        
                # restoring  Purchases  table
                a = PurchaseSRZ(data=backup_file['Purchase'],many=True)
                if a.is_valid():
                    for i in backup_file['Purchase']:
                        i.update({
                                "supplier":Supplier.objects.get(pk=i['supplier']),
                                "company":Company.objects.get(pk=i['company']),
                                "pay_mode":PayMode.objects.get(pk=i['pay_mode']),
                               
                                  })
                        Purchase.objects.update_or_create(pk=i["id"],defaults=i)
                        
        
        
        
        
                # restoring  Particular table
                a = ParticularSRZ(data=backup_file['Particular'],many=True)
                if a.is_valid():
                    for i in backup_file['Particular']:
                        i.update({
                                "company":Company.objects.get(pk=i['company']),
                                "unit":Unit.objects.get(pk=i['unit']),
                                "item":Product.objects.get(pk=i['item']),
                                "purchasebill":Purchase.objects.get(pk=i['purchasebill'])
                                  })
                        Particular.objects.update_or_create(pk=i["id"],defaults=i)     
                        
                        
                        
                                         
                        
                # restoring  Stock summarys  table
                a = Stock_summarySRZ(data=backup_file['StockSummary'],many=True)
                if a.is_valid():
                    for i in backup_file['StockSummary']:
                        i.update({
                                "product":Product.objects.get(pk=i['product']),
                                "company":Company.objects.get(pk=i['company']),
                                  })
                        StockSummary.objects.update_or_create(pk=i["id"],defaults=i)
                        
                        
                # restoring  Bank account adjustments table
                a = Bank_account_adjustmentSRZ(data=backup_file['BankAccountAdjustment'],many=True)
                if a.is_valid():
                    for i in backup_file['BankAccountAdjustment']:
                        i.update({
                                "bank":Bank.objects.get(pk=i['bank']),
                                "company":Company.objects.get(pk=i['company']),
                                  })
                        BankAccountAdjustment.objects.update_or_create(pk=i["id"],defaults=i)
                        
                        
                        
                # restoring Bank account ledgers table
                a = Bank_account_ledgerSRZ(data=backup_file['BankAccountLedger'],many=True)
                if a.is_valid():
                    for i in backup_file['BankAccountLedger']:
                        i.update({
                                "bank":Bank.objects.get(pk=i['bank']),
                                "company":Company.objects.get(pk=i['company']),
                                  })
                        BankAccountLedger.objects.update_or_create(pk=i["id"],defaults=i)
                      
                      
                       
                # restoring Expenses table
                a = ExpenseSRZ(data=backup_file['Expense'],many=True)
                if a.is_valid():
                    for i in backup_file['Expense']:
                        i.update({
                                "expense_type":ExpenseType.objects.get(pk=i['expense_type']),
                                "company":Company.objects.get(pk=i['company']),
                                  })
                        Expense.objects.update_or_create(pk=i["id"],defaults=i)
                        
                        
                        
                # restoring Service table
                a = ServiceSRZ(data=backup_file['Service'],many=True)
                if a.is_valid():
                    for i in backup_file['Service']:
                        i.update({
                                "group":Group.objects.get(pk=i['group']),
                                "unit":Unit.objects.get(pk=i['unit']),
                                "company":Company.objects.get(pk=i['company']),
                                  })
                        Service.objects.update_or_create(pk=i["id"],defaults=i)
                        



                # restoring CashBook table
                a = CashBookSRZ(data=backup_file['CashBook'],many=True)
                if a.is_valid():
                    for i in backup_file['CashBook']:
                        i.update({
                                "company":Company.objects.get(pk=i['company']),
                                  })
                        CashBook.objects.update_or_create(pk=i["id"],defaults=i)       
                        
                        
                # restoring CashBookAdjustment table
                a = CashBookAdjustmentSRZ(data=backup_file['CashBookAdjustment'],many=True)
                if a.is_valid():
                    for i in backup_file['CashBookAdjustment']:
                        i.update({
                                "company":Company.objects.get(pk=i['company']),
                                  })
                        CashBookAdjustment.objects.update_or_create(pk=i["id"],defaults=i)       
                        
                              
                      
                        
                        
                        
                        
                        
                messages.success(request, _("Your backup has restored successfully."))       
            else:
                messages.error(request, _("Sorry, you are not authenticate for this file."))
                
        
        
        return render(request,"ebilling/backup_restore.html")
    
    







from polib import pofile
from googletrans import Translator
from django.core.management import execute_from_command_line
import os
@login_required(login_url='/e-billing/login')
@check_permission()
def translation_update(request):
    if request.user.is_superuser:
        execute_from_command_line(["manage.py","makemessages","--all","-i","env"])
        
        po_file = pofile(os.path.join(BASE_DIR,"locale/ne/LC_MESSAGES/django.po"))
        
        
        
        for msg in po_file.untranslated_entries():
       
            msg.msgstr = Translator().translate(text=msg.msgid,dest="ne",src="en").text
 
            
        
        for msg in po_file.fuzzy_entries():

            msg.msgstr = Translator().translate(text=msg.msgid,dest="ne",src="en").text
            msg.flags.remove('fuzzy')
            
        po_file.save()
        execute_from_command_line(["manage.py","compilemessages","-i","env"])


       
    return JsonResponse({"message":"Completed translation"})

from django.core.paginator import Paginator

@login_required(login_url='/e-billing/login')
@check_permission()
def HistoryView(request):

    paginator  = Paginator(History.objects.filter(company=request.user.getCompany.get()).order_by("-pk"),25)
    current_page = request.GET.get('page') or 1
    history = paginator.page(current_page)
    context = {
        "Historys":history,
        "is_paginated":True,
        "page_obj":{
            "has_previous":history.has_previous(),
            "has_next":history.has_next(),
            "previous_page_number":history.previous_page_number() if history.has_previous() else "",
            "next_page_number":history.next_page_number() if history.has_next() else "",
            "num_pages":paginator.num_pages,
            "number":current_page
        }
        
    }
    return render(request,"ebilling/history.html",context)
    
    
    
    
    
from django.utils.decorators import method_decorator

from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from ebilling.models import UserPermission


class UserView(ListView):

    template_name  = "ebilling/User.html"
    context_object_name = "users"
    
    @method_decorator(login_required(login_url='/e-billing/login'))
    @method_decorator(check_permission())
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:           #cheack for auth
            raise Http404()
            
            
            
            
        if request.GET.get("addUser") == "True" or request.GET.get("updateUser"):       #code.......
            context ={
                'title':_("User Registration"),
                "permission": UserPermission.objects.all(),
                "action":"addUser=True"
            }
            
            if request.GET.get("updateUser"):
                user = User.objects.filter(pk=request.GET.get("updateUser"))
                
                if user.exists():
                    user = user[0]
                    
                    context.update({
                        "title":_("Update User Details"),
                        "action":f"updateUser={user.pk}",
                        "data":self.getUserData(user),
                        "updateStatus":True
                    })
                
                else:
                    raise Http404()
                    
                
            
            return render(request,"ebilling/UserFromPage.html",context)
        
        
        
        if request.GET.get("removeUser"):
            self.removeUser()
            print(self.request.GET.get("removeUser"))
        
        return super(UserView, self).get(request, *args, **kwargs)
    
    
    def getUserData(self,user):
        return {
            "is_staff":user.is_staff,
            "first_name":user.first_name,
            "last_name":user.last_name,
            "username":user.username,
            "email":user.email,
            "permission":user.getPermissions.all(),
            "is_active":user.is_active
        }
        
    def removeUser(self):
        print(self.request.GET.get("removeUser"))
        user = User.objects.filter(pk=self.request.GET.get("removeUser"))
        if user.exists():
            messages.success(self.request, user[0].username +_("(User) Has Been Removed Form Your Company"))
            Log(self.request, user[0].username +"(User) Has Been Removed Form Your Company")
            
            user.delete()
        
            
    
    
    
    def UpdateUser(self,post):
        
        user = User.objects.filter(pk=self.request.GET.get('updateUser'))
      
        if user.exists():
            
                
            user.update(username=post.get('username').strip(),
                        first_name= post.get('first_name'),
                        last_name= post.get('last_name'),
                        email=post.get('email'),
                        is_active=bool(post.get('is_active'))
                        )
            
            if post.get('old_password'):
                form = PasswordChangeForm(user[0],post)
                
                if form.is_valid():
                    form.save()
                    messages.success(self.request, _("User Password Has Been Changed"))
                else:
                    messages.error(self.request,form.errors)
                    return self.get(self.request)
            
          
            self.RemoveAllPermissionToUser(user[0])
            self.addPermissionToUser(user[0],post)
            
            
            messages.success(self.request, post.get('username').strip() + _("'s information has been updated") +_(" ID: ") + str(user[0].pk))
            Log(self.request, post.get('username').strip() + "'s information has been updated" +" ID: #" + str(user[0].pk))
            
            
            return redirect("ebilling:user")
            
        
        else:
            raise Http404()
        
        
    @method_decorator(login_required(login_url='/e-billing/login'))
    @method_decorator(check_permission()) 
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise Http404()
        
        post = request.POST
        
        if request.GET.get("updateUser"):
            return self.UpdateUser(post)
            
            
        form = UserCreationForm(post)
        if form.is_valid():
            user = form.save()
            user.first_name = post.get('first_name')
            user.last_name = post.get('last_name')
            user.email = post.get('email')
            user.is_active = bool(post.get('is_active'))
            user.save()
            
            
            
            self.addPermissionToUser(user,post)
            self.addCompanyToUser(user)
            
            messages.success(request, _("A new user has been created successfully"))
            Log(request, f"A new user has been created successfully, Name:{user.username}")
            
            
            return redirect("ebilling:user")
            
            
        else:
            messages.error(request, form.errors)
            
            return self.get(request)
    
    
    
    def get_queryset(self):
        company = Company.objects.filter(user=self.request.user)
        if company.exists():
            
            return company[0].user.all()
            
        raise Http404()
    
    
    def addPermissionToUser(self,user,post):
            permission_list = dict(post).get('permission')
            try:
                for item in permission_list:
                    
                    permission = UserPermission.objects.get(task=item)
                    permission.user.add(user)
                
            except UserPermission.DoesNotExist:
                raise Http404()
            
    def RemoveAllPermissionToUser(self,user):
        user.getPermissions.clear()

            
    def addCompanyToUser(self,user):
        self.request.user.getCompany.get().user.add(user)
                

    

    