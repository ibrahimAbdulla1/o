from django.http import JsonResponse
import requests
from django.shortcuts import render
import requests

url = "https://chatgpt-gpt4-ai-chatbot.p.rapidapi.com/ask"
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "2fed437b0fmsh38546fc6cab015dp1f4627jsn7de328a4128e",
    "X-RapidAPI-Host": "chatgpt-gpt4-ai-chatbot.p.rapidapi.com"
}

def post_diagnose(data):
    # Make the API request
    response = requests.post(url, headers=headers, json=data)
    print(response.status_code)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Request failed with status code {response.status_code}"}


def diagnosis_view(request):
    if request.method == 'POST':
        # extract sex, age, and symptom_ids from the request
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        symptom_ids = request.POST.get('symptoms')  # assuming it's a list

        # Prepare the data
        qry = f'age: {age}, sex: {sex}, symptoms: {symptom_ids}'

        data = {
            "query":qry

        }
        """print("function")
        print(data)
        print(headers)
        print(url)
        print("function end")
        data, headers, url = get_diagnosis(sex, age, symptom_ids)
        print("function 2")
        print(data)
        print(headers)
        print(url)
        print("function end")"""
        print(data)
        result = post_diagnose(data)
        print(result)
        return JsonResponse(result)
    else:
        # Handle GET or other methods
        return JsonResponse({'message': 'This view only supports POST requests.'})


def api_view(request):
    response = requests.get(
        "https://chatgpt-gpt4-ai-chatbot.p.rapidapi.com/ask")  # Make a GET request to the API
    data = response.json()  # Parse the response as JSON

    # Process the data

    return JsonResponse(data)  # Return the processed data as a JSON response


def homePage(request):
    return render(request, "welcomePage.html")


def registerPage(request):
    return render(request, "register.html")


def guestPage(request):
    return render(request, "omarTheChatbot.html")
