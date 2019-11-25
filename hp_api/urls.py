from django.urls import path, include

urlpatterns = [
    path('contract/', include('contract.urls')),
]
