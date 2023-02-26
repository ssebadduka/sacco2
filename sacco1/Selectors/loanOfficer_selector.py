from sacco1.models import loanOfficer

def get_loanofficers():
    return loanOfficer.objects.all()

def get_loanofficer(loanofficer_id):
    return loanOfficer.objects.get(pk=loanofficer_id)

