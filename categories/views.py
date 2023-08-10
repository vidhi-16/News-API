import requests
from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    records = {}
    url = requests.get("https://inshorts.me/news/all?offset=0&limit=21")
    inshorts_data = url.json()
    records['sportsdata'] = inshorts_data
    return render(request,'index.html',records)