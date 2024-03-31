from django.db import models
from django.core.files.storage import FileSystemStorage

class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        # If the file with the same name already exists, delete it
        if self.exists(name):
            self.delete(name)
        return name
        
        
class OverwriteStoragebusinesscheck(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        # If the file with the same name already exists, delete it
        if self.exists(name):
            self.delete(name)
        return name
class SubsNew(models.Model):
	subsname = models.CharField(max_length=100)
	black_check_number = models.IntegerField(max_length=100, default=503947156)
	amazon_check_number = models.IntegerField(max_length=100, default=5072595)
	diabetes_check_number = models.IntegerField(max_length=100, default=57045)
	treasury_check_number = models.IntegerField(default=44355757)
	total_collection = models.IntegerField(max_length=100, default=1)
	daily_collection = models.IntegerField(max_length=100, default=1)
	monthly_expense_total = models.IntegerField(max_length=100, default=1)
	daily_check_created = models.IntegerField(max_length=100, default=1)
	scott_new_check_number = models.IntegerField(max_length=100, default=50400395)
	final_scott =  models.IntegerField(max_length=100, default=50400395)
	scott_customer_number = models.IntegerField(max_length=100, default=17513)
	cashier2022_check_number = models.IntegerField(max_length=100, default=151)
	image = models.ImageField(storage=OverwriteStorage(), default="test")
	personal_check_number = models.CharField(max_length=100, default=2)
	personal_account_number = models.CharField(max_length=100, default=1)
	personal_routing_number = models.CharField(max_length=100, default=1)
	personal_check_full_name = models.CharField(max_length=1000, default=1)
	personal_check_address = models.CharField(max_length=1000, default=1)
	personal_check_city_state_zip_code = models.CharField(max_length=1000, default=1)
	personal_small_text = models.CharField(max_length=1000, default=1)
	personal_small_text_2 = models.CharField(max_length=1000, blank=True, null=True)
	personal_check_second_full_name = models.CharField(max_length=1000, blank=True, null=True)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.subsname
    
# Elements for business check
class businessCheck(models.Model):
	#subsname = models.CharField(max_length=100)
	check_image_name = models.CharField(max_length=100, default="test")
	image = models.ImageField(storage=OverwriteStoragebusinesscheck(), default="test")
	business_check_number = models.CharField(max_length=100, default=2)
	business_account_number = models.CharField(max_length=100, default=1)
	business_routing_number = models.CharField(max_length=100, default=1)
	business_check_company_name = models.CharField(max_length=1000, default=1)
	business_check_address = models.CharField(max_length=1000, default=1)
	business_check_city_state_zip_code = models.CharField(max_length=1000, default=1)
	business_small_text = models.CharField(max_length=1000, blank=True, null=True)
	business_small_text_2 = models.CharField(max_length=1000, blank=True, null=True)  
	issued_bank_name = models.CharField(max_length=1000, blank=True, null=True)
	issued_address = models.CharField(max_length=1000, blank=True, null=True)
	issued_city_state_zipcode = models.CharField(max_length=1000, blank=True, null=True)
	business_check_second_name = models.CharField(max_length=1000, blank=True, null=True)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.business_check_company_name

    
