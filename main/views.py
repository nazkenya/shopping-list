from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Nazkya Raahiil Ramandha',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)