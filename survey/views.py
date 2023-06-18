from django.shortcuts import render
from django.http import HttpResponse
from autoclose.autoclose import SnippetFormThree

def home(request):
    if request.method == 'POST':
        form =  SnippetFormThree(request.POST)
        if form.is_valid():

            form.save()
            return HttpResponse('testimonial_thanks')
        else:
            print(form.errors)

    form = SnippetFormThree()
    return render(request, 'registration-wizard-version.html', {'form': form})