from Home.forms import AdviseFreeForm
from Home.models import Services, Contact


def get_lenta_elem(request):
    floor = Services.objects.values('name', 'slug',).all()
    contact = Contact.objects.first()
    advise_form = AdviseFreeForm()
    return {'floor': floor, 'contact': contact, 'AdviseForm': advise_form}
