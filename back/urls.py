# from django.conf import settings
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers                    # add this
from game import views
from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter()                      # add this
# router.register(r'user', views.UserView, 'user')     # add this

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('token-auth', obtain_jwt_token),
    path('users/', views.UserList.as_view())
]

# if settings.DEBUG:
#    import debug_toolbar
#    urlpatterns = [
#        url(r'^__debug__/', include(debug_toolbar.urls)),
#    ] + urlpatterns
