from django.shortcuts import render


def make_api_request(symptoms):
    data = {"query": symptoms}
    url = 'chatgpt-gpt4-ai-chatbot.p.rapidapi.com'
    headers = {
        "Content-Type": "application/json",
        "X-RapidAPI-Key": "2fed437b0fmsh38546fc6cab015dp1f4627jsn7de328a4128e",

    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()  # Assuming the API returns a message
    else:
        return "Error in connecting to ChatGPT"


def diagnosis_view(request):
    if request.method == "POST":
        symptoms = request.POST.get('symptoms')
        chatbot_response = make_api_request(symptoms)
    else:
        chatbot_response = None

    context = {'chatbot_response': chatbot_response}
    return render(request, 'omarTheChatbot.html', context)

