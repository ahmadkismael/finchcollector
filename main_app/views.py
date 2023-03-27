from django.shortcuts import render

# Create your views here.

cars = [
    {'make': 'Nissan', 'model': 'GTR', 'year': '2023', 'description': 'Fastest car created by Nissan'},
    {'make': 'BMW', 'model': 'm6', 'year': '2023', 'description': 'Fastest car created by BMW'},
    {'make': 'Audi', 'model': 'R8', 'year': '2023', 'description': 'Fastest car created by Audi'},
    {'make': 'Ford', 'model': 'Mustang Shelby500', 'year': '2023', 'description': 'One of the fastest cars created by Ford'},
]

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def cars_index(request):
    return render(request, 'cars/index.html', {
        'cars': cars
    })
