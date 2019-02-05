from django.contrib.auth.forms import UserCreationForm, UsernameField

from account.models import Account


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ("username", "address")
        field_classes = {'username': UsernameField}
