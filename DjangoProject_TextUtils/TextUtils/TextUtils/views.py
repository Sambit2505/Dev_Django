from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    print("printing"+str(removepunc))
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for i in djtext:
            if i not in punctuations:
                analyzed=analyzed+i
        params = {'purpose': "Removing Punctuations", 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if uppercase == 'on':
        analyzed = ""
        for i in djtext:
            analyzed=analyzed+i.upper()
        params = {'purpose': "Removing Punctuations", 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if newlineremover == 'on':
        analyzed = ""
        print(djtext)
        for i in djtext:
            print(i)
            if i != "\n" and i != "\r":
                analyzed=analyzed+i
        params = {'purpose': "Removing Punctuations", 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if extraspaceremover == 'on':
        analyzed = ""
        for index, i in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + i
        params = {'purpose': "Removing Punctuations", 'analyzed_text': analyzed}
    if extraspaceremover != 'on' and newlineremover != 'on' and uppercase != 'on' and removepunc != 'on':
        return HttpResponse('Error')
    return render(request, 'analyze.html', params)