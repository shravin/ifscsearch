from rest_framework.serializers import ModelSerializer

from bankifscsearchapp.models import BankDetails


class BankDetailsSerializer(ModelSerializer):
    class Meta:
        model = BankDetails

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = BankDetails.objects.all()
        ifscCode = self.request.query_params.get('ifsc', None)
        if ifscCode is not None:
            queryset = queryset.filter(ifsc=ifscCode)
        return queryset