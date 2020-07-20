from django.contrib import admin
from .models import *

RANDOM_SLUG_LENGTH = 16
MAX_SLUG_GENERATION_ATTEMPTS = 32


@admin.register(ShortenedURLModel)
class ShortenedURLAdmin(admin.ModelAdmin):
    list_display = ('entry_name', 'full_url', 'shortened_url_slug', 'created_by')
    list_filter = ('created_by', )
    exclude = ('created_by', )

    @staticmethod
    def generate_random_slug():
        for _ in range(MAX_SLUG_GENERATION_ATTEMPTS):
            slug = ''.join(random.choices(string.ascii_letters + string.digits, k=RANDOM_SLUG_LENGTH))
            try:
                ShortenedURLModel.objects.get(shortened_url_slug=slug)
            except ShortenedURLModel.DoesNotExist:
                return slug

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['shortened_url_slug'].initial = self.generate_random_slug()
        return form

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.created_by = request.user
        super().save_formset(request, form, formset, change)
