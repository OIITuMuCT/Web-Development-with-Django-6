from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Book, Contributor, Publisher
from .forms import PublisherForm
from .utils import average_rating


# Create your views here.
def index(request):
    name = "world"
    return render(request, "base.html", {"name": name})


def book_search(request):
    search_text = request.GET.get("search", "")
    return render(request, "search-results.html", {"search_text": search_text})


def home(request):
    context_data = {"template_variable": "I am a template variable."}
    return render(request, "base.html", context=context_data)


def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        book_list.append(
            {
                "book": book,
                "book_rating": book_rating,
                "number_of_reviews": number_of_reviews,
            }
        )
    context = {"book_list": book_list}
    return render(request, "reviews/book_list.html", context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.review_set.all()
    if reviews:
        book_rating = average_rating([review.rating for review in reviews])
        context = {"book": book, "book_rating": book_rating, "reviews": reviews}
    else:
        context = {"book": book, "book_rating": None, "reviews": None}
    return render(request, "reviews/book_detail.html", context)

def publisher_edit(request, pk=None):
    if pk is not None:
        publisher = get_object_or_404(Publisher, pk=pk)
    else:
        publisher = None
    if request.method == "POST":
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            updated_publisher = form.save()
            if publisher is None:
                messages.success(request,
                                 f'Publisher "{updated_publisher}" 'f'was created.')
            else:
                form = PublisherForm(instance=publisher)
                messages.success(request, f'Publisher "{updated_publisher}" 'f'was updated.')
                return redirect("publisher_edit", updated_publisher.pk)
    else:
        form = PublisherForm(instance=publisher)
    return render(
        request, 
        "reviews/instance_form.html", 
        {
            "method":request.method, 
            "form": form,
            "model_type": "Publisher",
            "instance": publisher,
        }
    )
