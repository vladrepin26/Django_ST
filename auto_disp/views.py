from django.shortcuts import render
# from .models import DateTime


def main_page(request):
    # context = {
    #     'posts': DateTime.objects.all()
    # }
    # return render(request, 'auto_disp/home_disp.html', context)
    return render(request, 'auto_disp/home_disp.html')

