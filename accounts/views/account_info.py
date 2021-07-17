from ..models.user import User
from rest_framework.generics import RetrieveAPIView
from ..serializers.account_info_model_serializer import AccountInfoModelSerializer
from rest_framework.permissions import AllowAny


class AccountInfo(RetrieveAPIView):
    serializer_class = AccountInfoModelSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
