from Home.forms import AdviseFreeForm
from Home.models import Services, Contact, Solutions, Object


def get_lenta_elem(request):
    floor = Services.objects.values('name', 'slug', ).all()
    contact = Contact.objects.first()
    advise_form = AdviseFreeForm()
    solutions_header = Solutions.objects.values('title', 'slug', ).all().order_by('-id')
    if solutions_header:
        solutions_header = solutions_header[:6]
    object_header = Object.objects.values('name', 'slug', ).all().order_by('-id')
    if object_header:
        object_header = object_header[:6]
    return {'floor': floor, 'contact': contact, 'AdviseForm': advise_form,
            'solutions_header': solutions_header, 'object_header': object_header}
