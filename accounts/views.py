from rest_framework import generics
from .models import Account
from .serializers import AccountsSerializer


class AccountCreate(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer
    
