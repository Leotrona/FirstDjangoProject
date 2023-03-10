from django.shortcuts import render
# Create your views here.

job_title = [
    "First Job",
    "Second Job",
    "Third Job",
    "Fourth Job",
]


def home(request):
    return render(request, 'home.html')

def rifles(request):
    return render(request, 'rifles.html')

def knives(request):
    return render(request, 'knives.html')

def pistols(request):
    return render(request, 'pistols.html')

def smg(request):
    return render(request,'smg.html')

def cases(request):
    return render(request, 'cases.html')

def stickers(request):
    return render(request,'stickers.html')

def heavy(request):
    return render(request, 'heavy.html')

def gloves(request):
    return render(request, 'gloves.html')

def ak47(request):
    try:
        # return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3"
        # return HttpResponse(return_html)
        context = {'job_title': job_title}
        return render(request, 'ak47.html', context)
    except:
        return render("Item not found!")
    return render(request, 'ak47.html')

def current_rifle(request):
    return render(request, 'current_rifle.html')

