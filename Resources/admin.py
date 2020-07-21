from django.contrib import admin
from .models import Technology,Skill, People, Experience, Rating, Edu_Qualification, Resume

# Register your models here.
admin.site.register(Technology)
admin.site.register(Skill)
admin.site.register(People)
admin.site.register(Experience)
admin.site.register(Rating)
admin.site.register(Edu_Qualification)
admin.site.register(Resume)
