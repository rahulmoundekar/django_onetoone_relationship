from django.forms import Textarea, TextInput
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.template import RequestContext

from person_license.forms import LicenseForm, PersonForm
from person_license.models import Person, License

from django.forms.models import inlineformset_factory


def viewAll():
    licenses = License.objects.all()
    return licenses


def personView(request):
    InlineFormSet = inlineformset_factory(Person, License, fields=('license_number', 'issue_date', 'expiry_date'),
                                          widgets={
                                              'license_number': TextInput(
                                                  attrs={'name': 'license_number',
                                                         'class': 'form-control form-control-user',
                                                         'placeholder': 'Enter License No.'}),
                                              'issue_date': TextInput(attrs={'name': 'issue_date',
                                                                             'class': 'form-control form-control-user',
                                                                             'placeholder': 'Enter Issue Date'}),
                                              'expiry_date': TextInput(attrs={'name': 'expiry_date',
                                                                              'class': 'form-control form-control-user',
                                                                              'placeholder': 'Enter Expiry Date'})
                                          })

    # create a form instance and populate it with data from the request:
    form = PersonForm(request.POST or None)
    formset = InlineFormSet(request.POST or None, instance=Person())
    if form.is_valid() and formset.is_valid():
        try:
            print("in save")
            person = form.save()
            formset.instance = person
            formset.save()
            print("saved")
            return redirect('/')
        except Exception as e:
            print(str(e))
    licenses = viewAll
    return render(request, 'index.html', {'form': form, 'formset': formset, 'licenses': licenses})


def deletePersonById(request, id):
    try:
        person = Person.objects.get(id=id)
    except person.DoesNotExist:
        person = None
    if person != None:
        person.delete()
    return redirect('/')
