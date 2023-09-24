from django.conf import settings
from django.http import HttpRequest

exposed_request = "Don't change"


def RequestExposerMiddleware(get_response):
        
    def middleware(request):
        print("request_exposer")
        global exposed_request
        
        exposed_request = request 
        
        response = get_response(request)
        return response 
    
    return middleware

# This doesn't work as I expected but i left it just to remember how i tried to return the 
# actual request without been in a view 
