from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from driver_management.views import MyModelList
from enquiry.views import MyEnquiryList, MyEnquiryDelete, MyEnquiryUpdate, MyEnquiryGetList
from booking.views import MyBookingList
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

schema_view = get_swagger_view(title='API Documentation')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='api-docs'),
    path('api/driver/', MyModelList.as_view(), name='driver-list'),
    path('api/enquiry/', MyEnquiryList.as_view(), name='enquiry-list'),
    path('api/enquiry/<int:id>', MyEnquiryGetList.as_view(), name='enquiry-list-id'),
    path('api/enquiry/<int:id>/', MyEnquiryUpdate.as_view(), name='enquiry-update-list'),
    path('api/enquiry/<int:id>/', MyEnquiryDelete.as_view(), name='enquiry-delete-list'),
    path('api/booking/', MyBookingList.as_view(), name='booking-list')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

