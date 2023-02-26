from sacco1.models import loan

def get_loans():
    return loan.objects.all()

def get_loan(loan_id):
    return loan.objects.get(pk=loan_id)

