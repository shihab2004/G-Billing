"""GMCNEPAL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from unicodedata import name
from django.urls import path,include

from .views import *



app_name = "ebilling"

urlpatterns = [
    path('login/',loginPage,name='login'),
    path('register/',registerPage),
    path('logout/', Logout),
    path('updateCompanyDetail/',updateCompanyDetailPage,name="updatecompany"),
    path('addClient/',addClientPage,name="addClient"),
    path('clients/',clientsPage,name="clients"),
    path('deleteClient/<int:pk>',deleteClientPage,name='deleteClient'),
    path('updateClient/<int:pk>',updateClientPage,name="updateClient"),
    path('addSupplier/',addSupplierPage,name="addSupplier"),
    path('suppliers/',suppliersPage,name="suppliers"),
    path('deleteSupplier/<int:pk>',deleteSupplierPage,name="deleteSupplier"),
    path('updateSupplier/<int:pk>',updateSupplierPage,name="updateSupplier"),
    path('addExpense/',addExpensePage,name="addExpense"),
    path('expenses/',expensesPage,name="expenses"),
    path('deleteExpense/<int:pk>',deleteExpensePage,name='deleteExpense'),
    path('updateExpense/<int:pk>',updateExpensePage,name="updateExpense"),
    # Master Urls Start Here 
    # path('addBank/',addBank,name="addBank"),
    path('addBank/',addBank,name="addBank"),
    path('deleteBank/',deleteBank,name="deleteBank"),
    path('editBank/',editBank,name="editBank"),
    path('viewBankAccounts/',viewBankAccounts),
    path('adjustBankAccount/<int:pk>',addBankAdjustment),
    path('addExpenseType/',addExpenseType,name="addExpenseType"),
    path('editExpenseType/',editExpenseType,name="editExpenseType"),
    path('deleteExpenseType/',deleteExpenseType,name="deleteExpenseType"),
    path('addDesignation/',addDesignation,name="addDesignation"),
    path('editDesignation/',editDesignation,name="editDesignation"),
    path('deleteDesignation/',deleteDesignation,name="deleteDesignation"),
    path('addDepartment/',addDepartment,name="addDepartment"),
    path('editDepartment/',editDepartment,name="editDepartment"),
    path('deleteDepartment/',deleteDepartment,name="deleteDepartment"),
    path('addUnit/',addUnit,name="addUnit"),
    path('deleteUnit/',deleteUnit,name="deleteUnit"),
    path('editUnit/',editUnit,name="editUnit"),
    path('addBrand/',addBrand,name="addBrand"),
    path('deleteBrand/',deleteBrand,name="deleteBrand"),
    path('editBrand/',editBrand,name="editBrand"),
    path('addGroup/',addGroup,name="addGroup"),
    path('deleteGroup/',deleteGroup,name="deleteGroup"),
    path('editGroup/',editGroup,name="editGroup"),


    path('dashboard/',dashboardPage,name="dashboard"),

    path('companyDetail/',companyDetailPage), # no log messages
    path('category/',categoryPage),# no log messages
    path('category-type/',categoryTypePage),# no log messages
    path('settings/',settingsPage,name="settings"),
    path('taxes/',taxesPage,name="taxes"),
    path('create-update-tax/',createUpdateTax,name="createUpdateTax"),
    path('addProduct/',addProduct,name="addProduct"),
    path('addService/',addService,name="addService"),
    path('deleteService/<int:pk>',deleteService,name="deleteService"),
    path('deleteProduct/<int:pk>',deleteProduct,name="deleteProduct"),
    path('editService/<int:pk>',editService,name="editService"),
    path('editProduct/<int:pk>',editProduct,name='editProduct'),
    path('searchManageProductService/',SearchManageProductAndServicePage,name="searchManageProductService"),
    path('draftPurchase/',draftNewPurchase,name="draftPurchase"),
# Report Link Start here 
    path('reports/clients/amountDueReport',clientAmountDueReport),
    path('reports/suppliers/accountBalanceReport',supplierAccountBalanceReport),
    path('reports/expenses/expensesReport',expensesReport),# no log messages



# Export Links with start from here 
    path('reports/clients/amountDueReport/exportExcel',exportClientDueAmountReportExcel),
    path('reports/clients/amountDueReport/exportPDF',exportClientDueAmountReportPdf),
    path('reports/suppliers/accountBalancesReport/exportExcel',exportSupplierAccountBalancesReportExcel),
    path('reports/expenses/expensesReport/exportExcel',exportExpensesSearchResultReportExcel),
    path('reports/expenses/expensesReport/exportPDF',exportExpensesSearchResultReportPdf),

#Summary Pages Url Here 
    path('summary/stockSummary',StockSummaryPage),




    path('getUserBackup',getUserBackUp),


#Backup and Translation
    path('translation_update/',translation_update),
    path('backup_restore/',backup_restore,name="backup_restore"),
    
    
    path('history/',HistoryView,name="history"),
    
    path('user/',UserView.as_view(),name="user"),
    
    
    
] 



