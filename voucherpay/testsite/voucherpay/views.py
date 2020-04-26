from django.shortcuts import render
import requests
import json
# Create your views here.

def index(request):
    return "Hello, World!"

def reliance_documents(request, application_name, form_name, id):
    # I'm calling reliance
    if request.method == 'GET':
        url = "https://rheem.etq.com:8443/reliance_deev/rest/v1/documents/{0}/{1}/{2}".format(application_name,form_name, id)
        response = requests.get(url, auth=('rheem', 'rheem123'))

        if response.status_code == 200:
            data = response.text
            json_data = json.loads(data)
            render(request,'documents.html', context={'document': json_data})
        else:
            print ('boo')
    
