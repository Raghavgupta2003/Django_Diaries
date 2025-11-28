from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hello(request):
    return HttpResponse("Hello, world!");

def home(request):
    return HttpResponse("<h1 style='color:blue;'>Welcome to the Home Page</h1>")

def menuitem(request):
    item = 'pizza'
    # return HttpResponse("The name of items is: "+item)
    return HttpResponse(f"The name of items is: {item}")

def menuitems(request):
    items = {
        'pizza': 'cost $10',
        'burger': 'cost $5',    
        'pasta': 'cost $8'
    }
    content = '<h1>Menu Items</h1>'
    for item, cost in items.items():
        content += f'<li>{item}: {cost}</li>'
    return HttpResponse(content)


# ------------------Dynamic Url(Route Parameteras)-----------

def greet(request, name):
    return HttpResponse(f"Good Morning! {name}, Welcome to our website.")

def menuitems1(request, dish):
    items = {
        'pizza': 'cost $10',
        'burger': 'cost $5',    
        'pasta': 'cost $8'
    }
    if(dish not in items):
        return HttpResponse("Dish not found")
    content = items[dish]
    return HttpResponse(f"The cost of {dish} is {content}")

# ------------------Dynamic Url(Query String Parameteras)-----------

def recipe(request):
    food = request.GET.get('food')
    return HttpResponse(f"The recipe for {food} is available here.")

# 2 parameters in query string

def addition(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    if num1 is None or num2 is None:
        return HttpResponse("Please provide both num1 and num2 parameters.")
    sum = int(num1) + int(num2)
    return HttpResponse(f"The sum of {num1} and {num2} is {sum}.")

def calculator(request):
    operation = request.GET.get('operation')
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return HttpResponse("Please provide valid numbers for num1 and num2.")
    
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return HttpResponse("Error: Division by zero is not allowed.")
        result = num1 / num2
    else:
        return HttpResponse("Invalid operation. Please use add, subtract, multiply, or divide.")
    
    return HttpResponse(f"The result of {operation}ing {num1} and {num2} is {result}.")
    # return HttpResponse(result)

# -------------REGULAR EXPRESSIONS---------------------------

def user_profile(request, username):
    return HttpResponse(f"User Profile Page of {username}")

def item_detail(request, item_id):
    return HttpResponse(f"Details of item with ID: {item_id}")

def restro_detail(request, category, subcategory):
    if subcategory:
        return HttpResponse(f"Restaurant Category: {category}, Subcategory: {subcategory}")
    else:
        # -Error Handling in Django--
        return HttpResponse(f"Restaurant Category: {category}, <span style='color:red;'>No Subcategory Provided</span>", status=404)
    

# -------------TEMPLATE RENDERING---------------------------

def home1(request):
    return render(request, 'home.html')  # looks for home.html in templates folder
    # render function accepts 3 parameters: request, template_name, variables_dict (optional)


def menu(request):
    items = {
        'name': 'noodles',
        'price': '$12',
    }
    return render(request, 'menu.html', items)

def menu1(request):
    items = [
        {'name': 'pizza', 'price': '$10'},
        {'name': 'burger', 'price': '$5'},
        {'name': 'pasta', 'price': 'free'},
    ]
    return render(request, 'menu1.html', {'items': items}) # we cannot pass list directly, so we wrap it in a dictionary


# -----------------Template Inheritance--------------------

items = [
    {'name': 'noodles', 'cost': 400, 'details': 'Details about noodles'},
    {'name': 'burger', 'cost': 200, 'details': 'Details about burger'},
    {'name': 'pizza', 'cost': 500, 'details': 'Details about pizza'},
    {'name': 'pasta', 'cost': 300, 'details': 'Details about pasta'},
]


def restroHome(request):
    return render(request, 'restroHome.html')

def restroAbout(request):
    return render(request, 'restroAbout.html')

def restroMenu(request):
    return render(request, 'restroMenu.html', {'items': items})

def restroMenuitems(request, item_name):
    singleItem = {}
    for food in items:
        if food['name'] == item_name:
            singleItem = food
            break
    data = {'item': singleItem}
    if singleItem:
        return render(request, 'restroMenuitems.html', data)
    return HttpResponse("Item not found")

#------------------FORMS--------------------
# There are 4 ways to handle forms in Django:
# 1) Returning HTML markup as HTTP response
# 2) HTML Forms with Django Templates
# 3) Django Forms
# 4) Model Forms

#---------1) Returning HTML markup as HTTP response-----------------

from django.middleware.csrf import get_token

def simpleform(request):
    csrf_token = get_token(request)
    if(request.method == 'POST'):
        textbox1 = request.POST.get('textbox1')
        textbox2 = request.POST.get('textbox2')
        return HttpResponse(f"You submitted: Text Box 1 = {textbox1}, Text Box 2 = {textbox2}") 
    else:
        return HttpResponse(f"""
        <form method="POST">
        <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
        <label for="textbox1">Text Box 1:</label>
        <br>
        <input type="text" id="textbox1" name="textbox1">
        <br>
        <label for="textbox2">Text Box 2:</label>
        <br>
        <input type="text" id="textbox2" name="textbox2">
        <br><br>
        <input type="submit" value="Submit">
        </form>
        """)
    
#---------2) HTML Forms with Django Templates-----------------

def templateform(request):
    if(request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if name and email and password:
            return HttpResponse("Form submitted successfully!")
            # return HttpResponse(f"You submitted: Name = {name}, Email = {email}, Password = {password}")
    return render(request, 'form.html')

#--------------3) Django Forms-----------------

from .forms import InputForm
def form1(request):
    if(request.method == 'POST'):
        form = InputForm(request.POST) # creating instance of class created in forms.py
        if form.is_valid():      # checks if all fields are valid according to their types
            return HttpResponse(f"Django Form submitted successfully! and Name is {form.cleaned_data['name']}")  # cleaned_data is a dictionary that contains validated form data
        else:
            return render(request, 'djangoform.html', {'form': form})
    form = InputForm() # empty form, first time render by "GET request"
    return render(request, 'djangoform.html', {'form': form})


#--------------FORM VALIDATION-----------------

def Validation(request):
    submitted_details = None
    if(request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # creationg variables to hold error messages
        name_error = email_error = password_error = None

        # validating
        if not name:
            name_error = "Name is required."
        if not email or "@" not in email:
            email_error = "Valid email is required."
        if not password or len(password) < 6:
            password_error = "Password must be at least 6 characters long."

        # if there are any errors, re-render the form with error messages
        if name_error or email_error or password_error:
            return render(request, 'validation.html', {
                'name_error': name_error,
                'email_error': email_error,
                'password_error': password_error,
                'name': name,
                'email': email,
                'password': password,
            })
        else:
            submitted_details = {
                'name': name,
                'email': email,
                'password': password,
            }
    return render(request, 'validation.html', {'submitted_details': submitted_details})
    
#-------------Django Forms Validation---------------------------

from .forms import InputForm
def Validation1(request):
    submitted_details = None
    if(request.method == 'POST'):
        form = InputForm(request.POST) 
        if form.is_valid():
            submitted_details = form.cleaned_data
        else:
            return render(request, 'validation1.html', {'form': form, 'submitted_details': submitted_details})
    else:
        form = InputForm()
        return render(request, 'validation1.html', {'form': form, 'submitted_details': submitted_details})
    

#-------------POST REDIRECT REFRESH PATTERN---------------------------


from django.middleware.csrf import get_token
from django.shortcuts import redirect


def postredirect(request):
    csrf_token = get_token(request)
    if(request.method == 'POST'):
        textbox1 = request.POST.get('textbox1')
        textbox2 = request.POST.get('textbox2')
        # return HttpResponse(f"You submitted: Text Box 1 = {textbox1}, Text Box 2 = {textbox2}")
        return redirect('success')  # redirect to success page after form submission
    else:
        return HttpResponse(f"""
        <form method="POST">
        <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
        <label for="textbox1">Text Box 1:</label>
        <br>
        <input type="text" id="textbox1" name="textbox1">
        <br>
        <label for="textbox2">Text Box 2:</label>
        <br>
        <input type="text" id="textbox2" name="textbox2">
        <br><br>
        <input type="submit" value="Submit">
        </form>
        """)
    
def success(request):
    return HttpResponse("Form submitted successfully!") #we can also render a template here

#-------------DATABASE MODELS---------------------------
#------------Signup Form  Using HTML templates--------------------------

from .models import User

def signup(request):
    accounts_created = False
    if(request.method == 'POST'):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create(username=username, email=email, password=password)
        user.save()
        accounts_created = True
    return render(request, 'signup.html', {'accounts_created': accounts_created})

#----------Django signup forms with Models--------

from .forms import SignupForm
from .models import User

def signup1(request):
    form_submitted = False
    if(request.method == 'POST'):
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create(username=username, email=email, password=password)
            user.save()
            form_submitted = True
    else:
        form = SignupForm()
    return render(request, 'signup1.html', {'form': form, 'form_submitted': form_submitted})


#-------------Model Form-------------------------
# saving data through model form
# we also implement CRUD operations using model forms

from .forms import SignupForm1
from .models import User

def signup2(request):
    user = User.objects.all() # function to fetch all records from User table in form of queryset
    form_submitted = False
    if(request.method == 'POST'):
        form = SignupForm1(request.POST)
        if form.is_valid():
            form.save()
            form_submitted = True
            return render(request, 'signup2.html', {'form': form, 'form_submitted': form_submitted})
    else:
        form = SignupForm1()
    return render(request, 'signup2.html', {'form': form, 'users': user})

# delete

def delete(request, id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect('signup2')

# update or edit

def edit(request, id):
    user = User.objects.get(pk=id)
    if(request.method == 'POST'):
        form = SignupForm1(request.POST, instance=user) # helps to get edited data in form
        if form.is_valid():
            form.save()
            return redirect('signup2')
    else:
        form = SignupForm1(instance=user) # pre-fill the form with existing data
    return render(request, 'update.html', {'form': form, 'user': user})

#-------Blog Post Form with ModelForm-------------
#-----Model to templaate---------

from .forms import BlogPostForm

def insertblogpost(request):
    blog_created = False
    if(request.method == 'POST'):
        form = BlogPostForm(request.POST, request.FILES) # to handle file uploads, we need to pass request.FILES
        if form.is_valid():
            form.save()
            blog_created = True
    else:
        form = BlogPostForm()
    return render(request, 'insertblogpost.html', {'form': form, 'blog_created': blog_created})

# RETRIEVAL OF DATA ON TEMPLATE FROM MODELS

from .models import Blogpost
def displayblogposts(request):
    posts = Blogpost.objects.all() # fetch all blog posts from database
    return render(request, 'displayblogposts.html', {'posts': posts})

def singleblogpost(request, id):
    post = Blogpost.objects.get(pk=id)
    return render(request, 'singleblogpost.html', {'post': post})


#-------------Cookies--------------------------

def set_cookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('name', 'john_doe', max_age=30)  # three parameters: key, value, max_age (optional)
    response.set_cookie('marks', '90', max_age=30)
    return response

def get_cookie(request):
    cookie_value1 = request.COOKIES.get('name')
    cookie_value2 = request.COOKIES.get('marks')
    if(cookie_value1 or cookie_value2):
        return HttpResponse(f"Cookie Values: name = {cookie_value1}, marks = {cookie_value2}")
    else:
        return HttpResponse("No cookies found.")
    
def delete_cookie(request):
    response = HttpResponse("Cookie Deleted")
    response.delete_cookie('name')
    return response


#-------------SESSION---------------------

def set_session(request):
    request.session['username'] = 'john_doe'
    request.session['email'] = 'john_doe@example.com'
    return HttpResponse("Session Set successfully.")

def get_session(request):
    username = request.session.get('username', 'Guest')
    email = request.session.get('email','Guest@gmail.com')
    if(username or email):
        return HttpResponse(f"Welcome username = {username}, email = {email}")
    else:
        return HttpResponse("No session data found.")

def delete_session(request):
    request.session.flush()  # deletes all session data
    return HttpResponse("Session Deleted successfully.")