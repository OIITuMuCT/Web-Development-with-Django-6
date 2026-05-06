from django.contrib import admin
from reviews.models import (Publisher, Contributor, Book,
BookContributor, Review)

class BookAdmin(admin.ModelAdmin):
    date_hierarchy = "publication_date"
    list_display = ("title", "isbn13", "has_isbn")
    list_filter = ("publisher", "publication_date")
    search_fields = ("title", "isbn", "publisher__name")

    @admin.display(ordering="isbn", description="ISBN-13", empty_value="-")
    def isbn13(self, obj):
        """ '9780316769174' => '978-0-31-676917-4'
        '0316769174' => '0316769174'
        None => '' """
        if obj.isbn:
            if len(obj.isbn)==13:
                return "-".join([obj.isbn[0:3], obj.isbn[3:4], obj.isbn[4:6], obj.isbn[6:12], obj.isbn[12:13]])
            return obj.isbn
        return ""
    @admin.display(boolean=True, description="Has ISBN")
    def has_isbn(self, obj):
        """ '9780316769174' => True """
        return bool(obj.isbn)


def initialed_name(obj):
    """ obj.first_name="Jerome David", 
    obj.last_name="Salinger" => 'Salinger JD'
    obj.first_names="Plato", obj.last_names='' 
    => 'Plato' """
    initials = "".join([name[0] for name in obj.first_names.split(" ")])
    if obj.last_names:
        return f"{obj.last_names}, {initials}"
    return obj.first_names


class ContributorAdmin(admin.ModelAdmin):
    list_display = (initialed_name, )

class BookContributorAdmin(admin.ModelAdmin):
    list_display = ("book__title",  "contributor",  "role")

admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor, BookContributorAdmin)
admin.site.register(Review)
