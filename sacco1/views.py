from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from ast import Import
from email import message
from imp import load_compiled
from multiprocessing import context
from django.shortcuts import render,reverse,redirect

from django.contrib import messages
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect

#  for login and registration
from django.contrib.auth.forms import  UserCreationForm

# Imports for Login
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import REDIRECT_FIELD_NAME, login,logout,authenticate
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.admin.views.decorators import staff_member_required 

#Import from Pogrammer
import sacco1.views as index_view
from sacco1.Forms.Member_form import membersForm
from sacco1.Forms.Savings_form import savingsForm
from sacco1.Forms.loan_form import loanForm
from sacco1.Forms.LoanOfficer_form import loanOfficersForm
from sacco1.Forms.Expenses_form import expensesForm
from .Selectors.expenses_selector import get_expenses,get_expense
from .Selectors.loanOfficer_selector import get_loanofficer,get_loanofficers
from .Selectors.loan_selector import get_loan,get_loans
from .Selectors.savings_selector import get_saving,get_savings
from .Selectors.member_selector import get_member,get_members


#REGISTRATION PAGE
#START REGISTRATION PAGE

def registerPage(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for=>' +user)
            return redirect('login')
            
    context = {'form':form}
    return render(request, 'register.html', context)                                                                   
#END REGISTRATION PAGE


 # FIRST PAGE(login page on the application)
def index_page(request):
    return render(request,"login.html") 
@login_required(login_url='login') 
def index1_page(request):
    return render(request,"index.html")           

def index_page(request):
    if request.user.is_authenticated:
        return render(request, "index.html")

    else:
        return render(request, "login.html")

    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            if request.GET.get('next',None):
                return redirect(request.GET['next'])
            return redirect('index')
        else:
            messages.info(request,'invalid Credentials')
            return redirect('login')
    else:
        return render (request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
                
#END FIRST PAGE



#MEMBERS
#START MEMBERS

def manage_member (request):
    member_form = membersForm() 
    Get_members = get_members()
    
    
    if request.method == "POST":
        member_form = membersForm(request.POST,request.FILES)
        if member_form.is_valid():
            member_form.save()
            messages.success(request, 'member record saved successfully')
        else:
            messages.warning(request,'operation not successful')
    context={
        "member_form": member_form,
        "Get_members": Get_members
    }        
    return render(request,"register_member.html",context)     

    

def edit_member(request, member_id):
    getmember= get_member(member_id)
    member_form = membersForm(instance = getmember)
    if request.method == "POST":
        member_form = membersForm(request.POST, request.FILES,instance = getmember)
        if member_form.is_valid():
            member_form.save()
            messages.success(request,'member changes saved successfully')
        else:
            messages.warning(request,'operation not successful')
        return HttpResponseRedirect(reverse(manage_member))

    context={
        "member_form": member_form,
        "getmember": getmember
    }        
            
    return render(request,"member_Edit.html",context)  



def delete_member(request, member_id):
    member_del = get_member(member_id)
    member_del.delete()
    messages.success(request,'member deleted successfully')
    return HttpResponseRedirect(reverse(manage_member))
#END  member


#SAVINGS
#START SAVINGS
def manage_savings (request):
    savings_form = savingsForm() 
    Get_savingss = get_savings()
    
    
    if request.method == "POST":
        savings_form = savingsForm(request.POST,request.FILES)
        if savings_form.is_valid():
            savings_form.save()
            messages.success(request, 'savings record saved successfully')
        else:
            messages.warning(request,'operation not successful')
    context={
        "savings_form": savings_form,
        "Get_savingss": Get_savingss
    }        
    return render(request,"register_savings.html",context)     

    

def edit_savings(request, savings_id):
    getsavings= get_savings(savings_id)
    savings_form = savingsForm(instance = getsavings)
    if request.method == "POST":
        savings_form = savingsForm(request.POST, request.FILES,instance = getsavings)
        if savings_form.is_valid():
            savings_form.save()
            messages.success(request,'savings changes saved successfully')
        else:
            messages.warning(request,'operation not successful')
        return HttpResponseRedirect(reverse(manage_savings))

    context={
        "savings_form": savings_form,
        "getsavings": getsavings
    }        
            
    return render(request,"savings_Edit.html",context)  



def delete_savings(request, savings_id):
    savings_del = get_savings(savings_id)
    savings_del.delete()
    messages.success(request,'savings deleted successfully')
    return HttpResponseRedirect(reverse(manage_savings))
#END  SAVINGS



#LOAN
#START LOANOFFICER
def manage_loan (request):
    loan_form = loanForm() 
    Get_loans = get_loans()
    
    
    if request.method == "POST":
        loan_form = loanForm(request.POST,request.FILES)
        if loan_form.is_valid():
            loan_form.save()
            messages.success(request, 'loan record saved successfully')
        else:
            messages.warning(request,'operation not successful')
    context={
        "loan_form": loan_form,
        "Get_loans": Get_loans
    }        
    return render(request,"register_loan.html",context)     

    

def edit_loan(request, loan_id):
    getloan= get_loan(loan_id)
    loan_form = loanForm(instance = getloan)
    if request.method == "POST":
        loan_form = loanForm(request.POST, request.FILES,instance = getloan)
        if loan_form.is_valid():
            loan_form.save()
            messages.success(request,'loan changes saved successfully')
        else:
            messages.warning(request,'operation not successful')
        return HttpResponseRedirect(reverse(manage_loan))

    context={
        "loan_form": loan_form,
        "getloan": getloan
    }        
            
    return render(request,"loan_Edit.html",context)  



def delete_loan(request, loan_id):
    loan_del = get_loan(loan_id)
    loan_del.delete()
    messages.success(request,'loan deleted successfully')
    return HttpResponseRedirect(reverse(manage_loan))
#END  LOAN

#LOANOFFICER
#START LOANOFFICER
def manage_loanofficer (request):
    loanofficer_form = loanOfficersForm() 
    Get_loanofficers = get_loanofficers()
    
    
    if request.method == "POST":
        loanofficer_form = loanOfficersForm(request.POST,request.FILES)
        if loanofficer_form.is_valid():
            loanofficer_form.save()
            messages.success(request, ' record saved successfully')
        else:
            messages.warning(request,'operation not successful')
    context={
        "loanofficer_form": loanofficer_form,
        "Get_loanofficers": Get_loanofficers
    }        
    return render(request,"register_loanofficer.html",context)     

    

def edit_loanofficer(request, loanofficer_id):
    getloanofficer= get_loanofficer(loanofficer_id)
    loanofficer_form = loanOfficersForm(instance = getloanofficer)
    if request.method == "POST":
        loanofficer_form = loanOfficersForm(request.POST, request.FILES,instance = getloanofficer)
        if loanofficer_form.is_valid():
            loanofficer_form.save()
            messages.success(request,' changes saved successfully')
        else:
            messages.warning(request,'operation not successful')
        return HttpResponseRedirect(reverse(manage_loanofficer))

    context={
        "loanofficer_form": loanofficer_form,
        "getloanofficer": getloanofficer
    }        
            
    return render(request,"loanofficer_Edit.html",context)  



def delete_loanofficer(request, loanofficer_id):
    loanofficer_del = get_loanofficer(loanofficer_id)
    loanofficer_del.delete()
    messages.success(request,' deleted successfully')
    return HttpResponseRedirect(reverse(manage_loanofficer))
#END  LOANOFFICER

#EXPENSES
#START EXPENSES
def manage_expenses (request):
    expenses_form = expensesForm() 
    Get_expensess = get_expenses()
    
    
    if request.method == "POST":
        expenses_form = expensesForm(request.POST,request.FILES)
        if expenses_form.is_valid():
            expenses_form.save()
            messages.success(request, 'expenses record saved successfully')
        else:
            messages.warning(request,'operation not successful')
    context={
        "expenses_form": expenses_form,
        "Get_expensess": Get_expensess
    }        
    return render(request,"register_expenses.html",context)     

    

def edit_expenses(request, expenses_id):
    getexpenses= get_expenses(expenses_id)
    expenses_form = expensesForm(instance = getexpenses)
    if request.method == "POST":
        expenses_form = expensesForm(request.POST, request.FILES,instance = getexpenses)
        if expenses_form.is_valid():
            expenses_form.save()
            messages.success(request,'expenses changes saved successfully')
        else:
            messages.warning(request,'operation not successful')
        return HttpResponseRedirect(reverse(manage_expenses))

    context={
        "expenses_form": expenses_form,
        "getexpenses": getexpenses
    }        
            
    return render(request,"expenses_Edit.html",context)  



def delete_expenses(request, expenses_id):
    expenses_del = get_expenses(expenses_id)
    expenses_del.delete()
    messages.success(request,'expenses deleted successfully')
    return HttpResponseRedirect(reverse(manage_expenses))

#EXPENSES END

