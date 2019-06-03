import re

from django.shortcuts import render
from .forms import PhoneForm


def get_numbers(request):
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            r = re.compile('\d{3}[-\.\s]??\d{3}\s?[-\.\s]??\s??\d{4}|\(\d{3}\)\s*\d{3}\s??[-\.\s]??\s??\d{4}|\b\d{3}\s??[-\.\s]??\s??\d{4}\b')
            bad_phone = r.findall(form.cleaned_data['text'])
            phone = []
            for p in bad_phone:
                p = re.sub("[^0-9]", "", p)
                if len(p) == 10:
                    p1 = p[0:3]
                    p2 = p[3:6]
                    p3 = p[6:10]
                    p = "(" + p1 + ") " + p2 + "-" + p3
                elif len(p) == 7:
                    p1 = p[0:3]
                    p2 = p[3:7]
                    p = p1 + "-" + p2
                phone.append(p)
    else:
        form = PhoneForm()
        phone = None
    return render(request, "phone.html", {'form': form, 'phone': phone})
