# in your Django views.py
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def diagnosis_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('symptoms')
        user_sex = request.POST.get('sex')
        user_age = request.POST.get('age')

        # Check if all inputs are not None or empty
        if user_input and user_sex and user_age:
            symptoms = user_input.split(',')  # symptoms are separated by commas
            try:
                user_age = int(user_age)  # Ensure age is an integer
            except ValueError:
                return render(request, 'omarTheChatbot.html',
                              {'omarTheChatbot_response': 'Invalid age. Please enter a number.'})

            chatbot_response = get_diagnosis(symptoms, user_sex, user_age)

            # Check if there was an error with the API request
            if 'error' in chatbot_response:
                return render(request, 'omarTheChatbot.html',
                              {'omarTheChatbot_response': 'Error getting diagnosis: ' + chatbot_response['error']})

            return render(request, 'omarTheChatbot.html', {'omarTheChatbot_response': chatbot_response})
        else:
            return render(request, 'omarTheChatbot.html',
                          {'omarTheChatbot_response': 'Please enter all details: symptoms, sex, and age.'})
    else:
        return render(request, 'omarTheChatbot.html')









