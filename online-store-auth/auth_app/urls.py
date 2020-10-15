from django.conf.urls import url
from auth_app import views


urlpatterns = [
    url(r'^apps/$', views.OAuthAppsView.as_view()),
    url(r'^token/$', views.GetTokenPairForThirdPartyApp.as_view()),
    url(r'^refresh/$', views.OAuthTokenRefreshView.as_view()),
]