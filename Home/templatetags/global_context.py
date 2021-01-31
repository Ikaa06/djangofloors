from Home.models import Services, Contact


def get_lenta_elem(request):
    floor = Services.objects.values('name', 'slug',).all()
    contact = Contact.objects.first()
    return {'floor': floor, 'contact': contact}
