from django.http import HttpResponse

'''
In views we 
'''

def home(request):
    return HttpResponse("Hello, Django!")

def testpage(request):
    return HttpResponse("This is a test page.")