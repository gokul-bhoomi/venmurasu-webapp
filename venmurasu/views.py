from django.shortcuts import redirect, render
from django.http import HttpResponse
import pymongo
from .forms import NumberForm

client = pymongo.MongoClient("mongodb+srv://keerthana:keerthana@cluster0.2jruk.mongodb.net/venmurasuDB?retryWrites=true&w=majority")
db = client["venmurasuDB"]
col = db["venmurasu-text"]

# Create your views here.
def largeWords(request):
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            x = form.cleaned_data['number']
            mydoc = col.find().limit(x)
            return render(request, 'home.html', {'mydoc': mydoc, 'form': form})
    else:
        form = NumberForm()

    return render(request, 'home.html', {'form': form})