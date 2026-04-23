from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): #args and kwargs are used to pass any number of arguments to the view function
         print(args, kwargs) #print the arguments passed to the view function
         print(request.user) #print the user object associated with the request
         #return HttpResponse("<h1>Hello World</h1>") #return HttpResponse object with html content
         return render(request, "home.html", {}) #return render function to render the home.html template with an empty context

def contact_view(request, *args, **kwargs):
   # return render(request, "contact.html", {}) #return render function to render the contact.html template with an empty context
    return render(request, "contact.html", {}) #return render function to render the contact.html template with an empty context

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us page.",
        "this is true": True,
        "my_number": 123,
        "my_list": [1, 2, 3, 4, 5],
    }
    return render(request, "about.html", my_context) #return render function to render the about.html template with the context

def social_view(*args, **kwargs):
    return HttpResponse("<h1>Social Page</h1>") #return HttpResponse object with html content
