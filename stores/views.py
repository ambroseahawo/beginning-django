from django.shortcuts import render

# Create your views here.
def stores_list_view(request, location=None):
    context = { "location": location }

    return render(request, 'stores/stores_list.html', context=context)

def stores_detail_view(request, store_id='1', location=None):
    # access store_id param with 'store_id' variable
    # and location param with 'location' variable

    # extract 'hours' or'map' value appended to url as
    # ?hours=sunday&map=flash
    hours = request.GET.get('hours', '')
    map = request.GET.get('map', '')

    print(hours, map) # if available

    # create fixed data structures to pass to template
    STORE_NAME = 'Downtown'
    store_address = { 'street':'Main #385', 'city':'San Diego', 'state':'CA' }
    store_amenities = ['WiFi', 'A/C']
    store_menu = ((0, ''), (1, 'Drinks'), (2, 'Food'))
    
    context = { "store_id": store_id, "location": location,
                "store_name":STORE_NAME, "store_address":store_address,
                "store_amenities":store_amenities, "store_menu":store_menu }

    return render(request, 'stores/stores_detail.html', context=context)