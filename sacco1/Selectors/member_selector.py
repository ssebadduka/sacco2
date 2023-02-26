from sacco1.models import members

def get_members():
    return members.objects.all()

def get_member(member_id):
    return members.objects.get(pk=member_id)

