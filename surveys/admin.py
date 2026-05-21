from django.contrib import admin
from .models import Quiz, Question, Answer, UserSession, UserResponse

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UserSession)
admin.site.register(UserResponse)