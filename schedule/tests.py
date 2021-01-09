from django.http import HttpResponse


r = HttpResponse()
print(r["Content-Type"])