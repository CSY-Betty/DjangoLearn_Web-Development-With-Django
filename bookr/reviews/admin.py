from django.contrib import admin
from reviews.models import Publisher, Contributor, Book, BookContributor, Review


class BookAdmin(admin.ModelAdmin):
    model = Book
    date_hierarchy = 'publication_date'
    list_display = ('title', 'isbn13', 'get_publisher', 'publication_date')
    list_filter = ('publisher', 'publication_date')
    search_fields = ('title', 'isbn__exact', 'publisher__name__startswith')

    def get_publisher(self, obj):
        return obj.publisher.name


class ReviewAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('creator', 'book')}),
        ('Review content', {'fields': ('content', 'rating')}),
    )
    exclude = ('date_edited',)


class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    search_fields = ('last_name__startswith', 'first_name')
    list_filter = ('last_name',)


# Register your models here.
admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)
