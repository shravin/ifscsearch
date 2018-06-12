from django.db.models import Model, IntegerField, CharField, TextField


class BankDetails(Model):
    bankId = IntegerField()
    name = CharField(max_length=500)
    ifsc = CharField(max_length=12, null=False)
    address = TextField()
    state = CharField(max_length=100, null=False)
    city = CharField(max_length=100, null=False)

