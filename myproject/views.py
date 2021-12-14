# i have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    uppercase = request.POST.get('uppercase','off')
    lowercase = request.POST.get('lowercase','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    
    if removepunc == 'on':
        punctuations = '''!"#$%&'()*+,-./:;?@[\]^_`{|}~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
                
        params = {'analyzed_text':analyzed,'purpose':'Removing Punctuations'}
        djtext = analyzed
    
    if uppercase == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        
        params = {'analyzed_text':analyzed,'purpose':'Upper Case'}
        djtext = analyzed
    
    if lowercase == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.lower()
            
        params = {'analyzed_text':analyzed,'purpose':'Lower Case'}
        djtext = analyzed
        
    
    if newlineremover == 'on':
        analyzed = ''
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed = analyzed + char
        params = {'analyzed_text':analyzed,'purpose':'New Line Remover'}
        djtext = analyzed
    
    if extraspaceremover == 'on':
        analyzed = ''
        for index, char in enumerate(djtext):
            if djtext[index] == ' ' and djtext[index+1]==' ':
                pass
            else:
                analyzed = analyzed + char
        params = {'analyzed_text':analyzed,'purpose':'Extra Space Remover'}
    
    if (removepunc!='on' and uppercase=='on' and lowercase=='on' and newlineremover=='on' and extraspaceremover=='on'):
        return HttpResponse('Error! Please Select')
    return render(request, 'analyze.html',params)
    
 