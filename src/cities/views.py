from django.shortcuts import render
from django.http import HttpResponse

import io

# Create your views here.

# def cities(request, code):
#     with io.open ('airports_codes.txt', encoding='utf-8') as code_base:
#         response = "Code ", code, " not found"
#         e = '"'
#         for line in code_base:
#             if code.upper() in line[:3]:
#                 response = line[line.index(e) + 1: line.rindex(e)]
#                 break
#     return HttpResponse(response)

def cities(request, code):
    with io.open ('airports_codes.txt', encoding='utf-8') as code_base:
        ctx = {
            'city': "Code not found",
            'country': '',
            'code': code.upper()
        }        
        for line in code_base:
            if code.upper() in line[:3]:
                ctx['city'] = line[line.index('"') + 1: line.index(',')]
                ctx['country'] = line[line.index(',') + 1: line.rindex('"')]
                break
    return render(request, template_name="cities.html", context=ctx)

def cities_home(request):

    return render(request, template_name="home.html", context={})