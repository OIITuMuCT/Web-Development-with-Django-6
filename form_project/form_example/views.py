from django.shortcuts import render
from django.core.exceptions import ValidationError
from .forms import ExampleForm, ExampleChoiceForm, OrderForm, ExampleFormField, FormTest, PublisherForm

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


def validate_email_domain(value):
    if value.split("@")[-1].lower() != "example.com":
        raise ValidationError("The email address " "must be on the domain example.com.")


def order_form_example(request):
    # method = request.POST
    initial = {"email": "user@example.com"}
    if request.method == "POST":
        form = OrderForm(request.POST, initial=initial)
        if form.is_valid():
            for name in request.POST:
                print(f"{name}: {request.POST.getlist(name)}")
            for name, value in form.cleaned_data.items():
                print(f"{name}: ({type(value)} {value})")
    else:
        form = OrderForm(initial=initial)
    return render(
        request,
        "form_example/order_form_example.html",
        {"form": form, "method": request.method},
    )

def form_example_field(request):
    if request.method == "POST":
        form = ExampleFormField(request.POST)
        if form.is_valid():
            print(f"Form name: '{form_example_field.__name__}'")
            for name in request.POST:
                if name != 'csrfmiddlewaretoken':
                    print(f"\t{name}: {request.POST.getlist(name)}")
            print("Game over\n")
        print(request.POST)
    else:
        form = ExampleFormField()
    
    return render(request, "form_example/form_example_field.html",
                  {"form": form, "method": request.method, "hello": "Kto tam?"})

def form_test(request):
    if request.method =="POST":
        form = FormTest(request.POST)
        if form.is_valid():
            for name in request.POST:
                print(f"{name}: {request.POST.getlist(name)}")
    else:
        form = FormTest()
    return render(request, "form_example/form_test.html", {"form": form})

def form_publisher(request):
    form = PublisherForm()
    if request.method == "POST":
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            print("save success")
            for obj  in request.POST:
                print(f"{obj} {request.POST.getlist(obj)}")
    else:
        form = PublisherForm()
    return render(request, "form_example/publisher_form.html", {"form": form})