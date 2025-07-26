
from django.urls import path
from .import views

urlpatterns = [
    path("",views.index,name="home"),
    path("search",views.search,name="search"),
    path("registration",views.registration,name="donor_registration"),
    path("contact_us",views.contact_us,name='contact_us'),
    path("about_us",views.about_us,name='about_us'),

    # path('login',views.login,name='login'),
    
    path('user_login',views.user_login,name='user_login'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('account',views.account,name='account'),
    # path('showdata',views.showdata,name='showdata'),
    path('edit_profile',views.edit_profile,name='edit_profile'),

    path("searchDta",views.searchDta,name='searchDta')

    

]

