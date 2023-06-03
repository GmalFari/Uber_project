from rest_framework import generics
from .models import Enquiry
from .serializers import MyEnquirySerializer


class MyEnquiryList(generics.ListCreateAPIView):
    queryset = Enquiry.objects.all()
    serializer_class = MyEnquirySerializer


class MyEnquiryGetList(generics.ListAPIView):
    queryset = Enquiry.objects.all()
    serializer_class = MyEnquirySerializer
    lookup_field = 'id'


class MyEnquiryUpdate(generics.UpdateAPIView):
    queryset = Enquiry.objects.all()
    serializer_class = MyEnquirySerializer
    lookup_field = 'id'


class MyEnquiryDelete(generics.DestroyAPIView):
    queryset = Enquiry.objects.all()
    serializer_class = MyEnquirySerializer
    lookup_field = 'id'
