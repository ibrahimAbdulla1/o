from django.shortcuts import render
import requests
import os


API_KEY = os.getenv('501588c1c1msh544b3773c444627p150970jsn392a2f52d7d4')


def make_api_request(symptoms):
    data = {"query": symptoms}
    url = 'https://chatgpt-gpt4-ai-chatbot.p.rapidapi.com/ask'
    headers = {
        "Content-Type": "application/json",
        "X-RapidAPI-Key":'501588c1c1msh544b3773c444627p150970jsn392a2f52d7d4',
        "X-RapidAPI-Host":'chatgpt-gpt4-ai-chatbot.p.rapidapi.com'
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()  # Assuming the API returns a message
    else:
        return "Error in connecting to ChatGPT: {}".format(response.status_code)


def diagnosis_view(request):
    if request.method == "POST":
        symptoms = request.POST.get('symptoms')
        response_data = make_api_request(symptoms)
    else:
        response_data = None

    context = {'response_data': response_data}
    return render(request, 'omarTheChatbot.html', context)



