from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from sp import views
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/auth/', include('rest_framework.urls')),
    path('', include('blog.urls', namespace="blog")),
    path("user/autocomplete/", login_required(views.UserLinkedDataAutocompleteView.as_view()), name="user_autocomplete"),
    path('fifarank/', include('fifarank.urls', namespace='fifarank')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('beers/', include('beers.urls', namespace='beers')),
    path('sews/', include('sews.urls', namespace='sews'))
]
