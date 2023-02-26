from sacco1.models import expenses

def get_expenses():
    return expenses.objects.all()

def get_expense(expenses_id):
    return expenses.objects.get(pk=expenses_id)

