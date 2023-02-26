from operator import index
from unicodedata import name
from django.urls import path

from operator import index
from unicodedata import name
from django.urls import path

import sacco1.views as index_view

urlpatterns = [
    path('register1', index_view.registerPage, name='register1'),
    path('',index_view.index_page, name="login"),
    path('login', index_view.login, name="login"),
    path('index', index_view.index1_page, name="index"), 
    path('member', index_view.manage_member, name="member"),
    path('Edit/<int:member_id>/', index_view.edit_member, name="Edit"),
    path('Delete/<int:member_id>/', index_view.delete_member, name="Delete"),    
    path('savings', index_view.manage_savings, name="savings"), 
    path('Edit/<int:savings_id>/', index_view.edit_savings, name="Edit"),
    path('Delete/<int:savings_id>/', index_view.delete_savings, name="Delete"),    
    path('loan', index_view.manage_loan, name="loan"), 
    path('Edit/<int:loan_id>/', index_view.edit_loan, name="Edit"),
    path('Delete/<int:loan_id>/', index_view.delete_loan, name="Delete"),    
    path('loanOfficer', index_view.manage_loanofficer, name="loanOfficer"), 
    path('Edit/<int:loanOfficer_id>/', index_view.edit_loanofficer, name="Edit"),
    path('Delete/<int:loanOfficer_id>/', index_view.delete_loanofficer, name="Delete"),  
    path('expenses', index_view.manage_expenses, name="expenses"), 
    path('Edit/<int:expenses_id>/', index_view.edit_expenses, name="Edit"),
    path('Delete/<int:expenses_id>/', index_view.delete_expenses, name="Delete"),   
] 


