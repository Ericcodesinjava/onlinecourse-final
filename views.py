from django.http import HttpResponse

def submit(request):
    return HttpResponse("Submitted successfully")

def show_exam_result(request):
    return HttpResponse("Congratulations! Your score is 90%")
