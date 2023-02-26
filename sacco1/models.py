from django.db import models
from codecs import charmap_build
from email.policy import default 
from random import choices
from django.db import models

# Create your models here.
#My Models


#Members

class members(models.Model):
    Full_Name=models.CharField(max_length=25)
    # Gender=models.CharField(max_length=6)
    # Age=models.IntegerField(default=18)
    Contact=models.CharField(max_length=15)
    National_id=models.CharField(max_length=14,null=True,blank=True)
    Address=models.CharField(max_length=35)
    Next_of_kin_Contact=models.CharField(max_length=35)
    m_image=models.ImageField(upload_to='pic')
    # Status=models.CharField(max_length=10)
    class Meta:
        verbose_name = ("member")
        verbose_name_plural = ("member")

    def __str__(self):
        return f'{self.Full_Name} - {self.Contact}'
        # return self.Full_Name

    def get_absolute_url(self):
        return reverse("member_detail", kwargs={"pk": self.pk})
    
#Savings
class savings(models.Model):
    Name=models.ForeignKey(members,on_delete=models.CASCADE)    
    Ammount_saved=models.IntegerField(default=0)
    Date_saved=models.CharField(max_length=10)

    class Meta:
        verbose_name = ("saving")
        verbose_name_plural = ("saving")

    def __str__(self):
        return f'{self.Name} - {self.Ammount_saved}'
        

    def get_absolute_url(self):
        return reverse("saving_detail", kwargs={"pk": self.pk})
    
#Loan/Ammount due
class loan(models.Model):
    Name=models.ForeignKey(members,on_delete=models.CASCADE)
    
    Ammount_received=models.IntegerField(default=0)
    Date_received=models.CharField(max_length=15)
    Purpose=models.CharField(max_length=255)
    status=models.CharField(max_length=10,null=True,blank=True)

    class Meta:
        verbose_name = ("loan")
        verbose_name_plural = ("loan")

    def __str__(self):
        return self.Name
    def get_absolute_url(self):
        return reverse("loan_detail", kwargs={"pk": self.pk})

#Loan officer
class loanOfficer(models.Model):
    Officer_name=models.CharField(max_length=25)
    Name=models.ForeignKey(members,on_delete=models.CASCADE)   
    Ammount_saved=models.ForeignKey(savings,on_delete=models.CASCADE)
    Ammount_received=models.ForeignKey(loan,on_delete=models.CASCADE )
    Date_of_Acceptance=models.DateField(max_length=15)
    status=models.CharField(max_length=10)
    Loan_data=models.CharField(max_length=255)

    class Meta:
        verbose_name = ("loanofficer")
        verbose_name_plural = ("loanofficer")

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse("Tenant_detail", kwargs={"pk": self.pk})
#Petty Cash/Expenses
class expenses(models.Model):
    # Name=models.ForeignKey(members,on_delete=models.CASCADE)
    Ammount_saved=models.ForeignKey(savings,on_delete=models.CASCADE)   
    Loan_data=models.ForeignKey(loanOfficer,on_delete=models.CASCADE)
    Ammount_spent=models.IntegerField(default=0)
    Spent_by=models.CharField(max_length=25)
    Spent_for=models.CharField(max_length=100)
    Comment=models.CharField(max_length=200)

    class Meta:
        verbose_name = ("expenses")
        verbose_name_plural = ("expenses")

    def __str__(self):
        return self.Spent_by

    def get_absolute_url(self):
        return reverse("expense_detail", kwargs={"pk": self.pk})

    
    
        
    
    
    
    
        
    
    
    
