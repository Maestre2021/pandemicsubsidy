from django.contrib import admin
from .models import Psrsignup, Familyinfo, Subsidyconfirmation, Receivingplacedate, Receivingbankpawnshop, PSRStatus, Additionalassistance, Inquries
admin.site.register(Psrsignup)
admin.site.register(PSRStatus)
admin.site.register(Familyinfo)
admin.site.register(Subsidyconfirmation)
admin.site.register(Receivingplacedate)
admin.site.register(Receivingbankpawnshop)
admin.site.register(Additionalassistance)
admin.site.register(Inquries)

# Register your models here.
