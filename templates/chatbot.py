from django.shortcuts import render
import requests


def chatbot_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('symptoms')  # Get the symptoms from the user's input
        chatbot_response = user_input

        return render(request, 'chatbot.html', {'chatbot_response': chatbot_response})

    return render(request, 'chatbot.html')
