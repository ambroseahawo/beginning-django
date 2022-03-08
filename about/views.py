from django.shortcuts import render

# Create your views here.
def about_index_view(request):
    return render(request, 'about/about.html')

def about_contact_view(request):
    # contact from request or database extracted here
    # and passed to the template for display
    return render(request, 'about/contact.html')