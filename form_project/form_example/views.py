from django.shortcuts import render

from .forms import ExampleForm, ExampleChoiceForm

# Create your views here.
def home_page(request):
    return render(request, "form_example/home_page.html")

def form_example(request):
    for name in request.POST:
        print(f"{name}: {request.POST.getlist(name)}")
    return render(request, "form_example/form_example.html", {"method": request.method})

def form_example_class(request):
    form = ExampleForm()
    print("source: \nform example class:")
    for name in request.POST:
            print(f'\t{name}: {request.POST.getlist(name)}')
    return render(request, 'form_example/form.html', {"form": form})

def form_exapmle_choices(request):
    form = ExampleChoiceForm()
    return render(request, "form_example/form.html", {"form": form})

def form_example_template(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            for name in request.POST:
                print(f"{name}: {request.POST.getlist(name)}")
            for name, value in form.cleaned_data.items():
                print(f"{name}: ({type(value)} {value})")
    else:
        form = ExampleForm()
    return render(request, 'form_example/form_template.html', {"form": form})
