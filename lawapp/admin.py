from django.contrib import admin
from clientapp.models import *
from lawyerapp.models import *

# Register your models here.
admin.site.register(Client)
admin.site.register(Lawyer)