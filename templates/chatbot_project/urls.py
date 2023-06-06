from django.contrib import admin
from django.urls import path
from chatbot_app.views import chatbot_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chatbot/', chatbot_view, name='Omar the chatbot'),

]

