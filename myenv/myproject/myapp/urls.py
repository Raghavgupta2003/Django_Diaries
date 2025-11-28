from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('home/', views.home),
    path('dish/', views.menuitem),
    path('dishes/', views.menuitems),
# --------Dynamic Url(Route Parameteras)-----------
    path('greet/<str:name>/', views.greet),
    path('dish/<str:dish>/', views.menuitems1),

# --------Dynamic Url(Query String Parameters)-----------
    path('recipe/', views.recipe),
            # check with: http://127.0.0.1:8000/recipe/?food=pizza
    path('addition/', views.addition),
            # check with: http://127.0.0.1:8000/addition/?num1=5&num2=10
            # if multiple parameters then separated by &
    path('calculator/', views.calculator),
            # check with: http://127.0.0.1:8000/calculator/?num1=5&num2=10&operation=add

# ---------REGULAR EXPRESSIONS---------------------------
    
    # re_path(r'^user/(?P<username>[a-zA-Z]+)/$', views.user_profile),
            # check with: http://127.0.0.1:8000/user/rajG/
            # re_path → allows regex-based URLs.
            # ^user/ → URL must start with user/.
            # (?P<username>[a-zA-Z]+) → captures a route parameter named username
            # + → one or more letters required (so username cannot be empty)
            # Only letters (A–Z, a–z) are allowed.
            # $ → URL must end with /.
            # Example URL: /user/Raghav/
    
    # re_path(r'^user/(?P<username>[a-zA-Z]*)', views.user_profile),
            # * → zero or more letters allowed (so username can be empty)
    
    # re_path(r'^user/(?P<username>[a-zA-Z]*)/?$', views.user_profile),
            # /? → makes the trailing slash optional

    re_path(r'^user/(?P<username>[a-zA-Z])/?$', views.user_profile),
            # {n} → exactly n letters required (so username must have exactly 1 letter)
            # if Quantifiers (*, +, {n}) are not used, it means exactly one character is required.
            # for 2 characters use {2}, and so on.
            # e.g., r'^user/(?P<username>[a-zA-Z]{2})/?$' for exactly 2 letters.

    # re_path(r'^item/(?P<item_id>[0-9]+)/$', views.item_detail),
    # re_path(r'^item/(?P<item_id>\d+)/$', views.item_detail),
            # /d → matches any digit (0-9)
            # /d is equivalent to [0-9]+

    # re_path(r'^item/(?P<item_id>\d{4})/$', views.item_detail),
            # {n} → exactly n digits required (so item_id must have exactly 4 digits)

    # re_path(r'^item/(?P<item_id>[\w]+)/$', views.item_detail),
            # \w → matches any alphanumeric character (letters, digits, and underscores)
            # [\w]+ is equivalent to [a-zA-Z0-9_]+
            # + → one or more characters required

    # re_path(r'^item/(?P<item_id>[\w-]+)/$', views.item_detail),
            # - → hyphen is also allowed in item_id


    # re_path(r'^item/(?P<item_id>[\w-]{3,10})/$', views.item_detail),
            # {3,10} → between 3 and 10 characters required (so item_id must be 3 to 10 characters long)
    
    re_path(r'^item/(?P<item_id>[\w\s%&-]+)/$', views.item_detail),
            # \s → matches any whitespace character (spaces, tabs, etc.)
            # % & - → special characters allowed in item_id

    re_path(r'^restaurant/(?P<category>[\w-]+)/(?P<subcategory>[\w-]*)/?$', views.restro_detail),


#-------------TEMPLATE RENDERING---------------------------
    path('home1/', views.home1),

    path('menu/', views.menu),

    path('menu1/', views.menu1),

# -----------------Template Inheritance--------------------
    path('restroHome/', views.restroHome, name='Home'),
    path('restroAbout/', views.restroAbout, name='About'),
    path('restroMenu/', views.restroMenu, name='Menu'),
    path('menuitems/<str:item_name>/', views.restroMenuitems, name='MenuItemsDetail'),

#------------------FORMS--------------------
    path('simpleform/', views.simpleform),

    path('templateform/', views.templateform),

    path('djangoform/', views.form1),

#---------------FORM VALIDATION--------------
    path('validation/', views.Validation),

    path('validation1/', views.Validation1),

#-----------POST REDIRECT REFRESH PATTERN-------------
    path('postredirect/', views.postredirect),
    path('success/', views.success, name ='success'),

#-----------SIGNUP FORM WITH MODEL----------------
    path('signup/', views.signup),

    path('signup1/', views.signup1),

    path('signup2/', views.signup2, name='signup2'), # we use name because while edit and update function we can redirect to same page.

    path('delete/<int:id>/', views.delete, name='delete'),

    path('edit/<int:id>/', views.edit, name='edit'),
#-----------BLOG POST WITH MODEL----------------
    path('blogpost/', views.insertblogpost, name='blogpost'),

    path('blogposts/', views.displayblogposts, name='blogposts'),

    path('singleblogpost/<int:id>/', views.singleblogpost, name='singleblogpost'),

#-------------Cookies-----------------------------------------
    path('set-cookie/', views.set_cookie, name='setcookie'),
    path('get-cookie/', views.get_cookie, name='getcookie'),
    path('delete-cookie/', views.delete_cookie, name='deletecookie'),
#-------------SESSION---------------------
        path('set-session/', views.set_session, name='setsession'),
        path('get-session/', views.get_session, name='getsession'),
        path('delete-session/', views.delete_session, name='deletesession'),

]