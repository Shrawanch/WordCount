from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return render (request, 'home.html')

def count(request):
    full_text = request.GET['Texts for counting']
    wordlist = full_text.split()
    worddictionary = {}


    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    return render(request, 'count.html', {'fulltext': full_text,'wordcount': len(wordlist), 'worddictionary': worddictionary.items()})

def about(request):
    return render (request, 'about.html')
