from django.shortcuts import render

def home(request):#home view
    query = request.GET.get('name')#input name="name"
    message = "Hello {} This is the home page!".format(query) #querys name into message variable into home
    template = "home.html"#form for query name
    context = {
    'message': message,#message variable passed into the home.html template, based on the query
    }
    return render(request, template, context)
