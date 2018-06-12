from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from bankifscsearchapp.models import BankDetails
from bankifscsearchapp.serializers import BankDetailsSerializer

class BankModelsViewSet(ModelViewSet):
    model = BankDetails
    serializer_class = BankDetailsSerializer
    queryset = BankDetails.objects.all()


class IfscList(ListAPIView):
    serializer_class = BankDetailsSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        ifscCode = self.kwargs['ifsc']
        return BankDetails.objects.filter(ifsc=ifscCode)