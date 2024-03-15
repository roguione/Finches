from django.contrib import admin
from .models import finch, Feeding, Toy, Photo

# Register your models here.
admin.site.register(finch)
admin.site.register(Feeding)
admin.site.register(Toy)
admin.site.register(Photo)