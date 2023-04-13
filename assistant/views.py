from django.shortcuts import render, redirect
from django.http import HttpResponse
# importing the openai API
import openai
# import the generated API key from the secret_key file
from .api_key import API_KEY

# loading the API key from the secret_key file
openai.api_key = API_KEY
# Create your views here.

# this is the home view for handling home page logic
def home(request):
    # the try statement is for sending request to the API and getting back the response
    # formatting it and rendering it in the template
    try:
        # checking if the request method is POST
        if request.method == 'POST':
            # getting prompt data from the form
            prompt = request.POST.get('prompt')
            # making a request to the API 
            response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=1, max_tokens=1000)
            # formatting the response input
            formatted_response = response['choices'][0]['text']
            # bundling everything in the context
            context = {
                'formatted_response': formatted_response,
                'prompt': prompt
            }
            # this will render the results in the home.html template
            return render(request, 'assistant/botPage.html', context)
        # this runs if the request method is GET
        else:
            # this will render when there is no request POST or after every POST request
            return render(request, 'assistant/botPage.html')
    # the except statement will capture any error
    except:
        # this will redirect to the 404 page after any error is caught
        
        return redirect('error')



# this is the view for handling errors
def error(request):
    return render(request, 'assistant/error.html')



def errorPage(request):
    return render(request, 'assistant/errorPage.html')


def homePage(request):
    return render(request, 'assistant/homePage.html')

def botPage(request):
    return render(request, 'assistant/botPage.html')