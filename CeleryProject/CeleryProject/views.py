from django.http import HttpResponse
from .task import test_func,send_mail_func


def task(request):
    test_func.delay()
    return HttpResponse("done")

def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Mail Sent...")