from sacco1.models import savings

def get_savings():
    return savings.objects.all()

def get_saving(savings_id):
    return savings.objects.get(pk=savings_id)

