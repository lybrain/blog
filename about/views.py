from django.shortcuts import render
from about.forms import ContactModelForm


def about(request):
    request.session['views'] = request.session.get('views',0) + 1
    if request.method == "POST":
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
    form = ContactModelForm()
    print(request.session['views'])
    return render(request, 'about.html', {"form": form})

