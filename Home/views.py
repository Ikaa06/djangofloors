from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from Home.forms import AdviseFreeForm, ResumeFreeForm, OrderPaymentForm
from Home.models import Services, Vacancy, Solutions, Object, TypeFloor


class index(ListView):
    """ Основаная страница """
    model = Solutions
    template_name = 'home/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['object_list'] = Object.objects.all()
        context['type_floors'] = TypeFloor.objects.all()
        context['description'] = ""
        context['keywords'] = ""
        return context

    def get_queryset(self):
        return self.model.objects.values('slug', 'description', 'title', 'images_png')


class about(ListView):
    """ О нас  """
    template_name = 'home/about-us.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О компании'
        context['description'] = ""
        context['keywords'] = ""
        return context

    def get_queryset(self):
        return


class contacts(ListView):
    """ Контакты """
    template_name = 'home/contacts.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        context['description'] = ""
        context['keywords'] = ""
        return context

    def get_queryset(self):
        return


class polymer(ListView):
    """ Услуга тип 2 """
    template_name = 'home/polymer-floor.html'

    def get_queryset(self):
        return


class concrete_floors(DetailView):
    """ Услуга """
    template_name = 'home/concrete-floors.html'
    model = Services


class vacancies(ListView):
    """ Вакансии """
    model = Vacancy
    template_name = 'home/vacancies.html'
    context_object_name = 'vacancies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вакансии'
        context['description'] = ""
        context['keywords'] = ""
        return context

    def get_queryset(self):
        return self.model.objects.filter(state=True)


class vacancy(DetailView):
    """ Вакансия """
    model = Vacancy
    template_name = 'home/vacancy.html'

    # def get_queryset(self):
    #     return self.model.objects.prefetch_related('requirement', 'tasks_set')


class ready_solutions(ListView):
    """ Готовые решения список """
    model = Solutions
    template_name = 'home/ready-solutions.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Готовые решения'
        context['description'] = ""
        context['keywords'] = ""
        return context

    def get_queryset(self):
        return self.model.objects.values('slug', 'description', 'title', 'images_png')


class ready_solution(DetailView):
    """ Готовые решения detail """
    model = Solutions
    template_name = 'home/solution.html'


class ready_objects(ListView):
    """ Объекты """
    model = Object
    template_name = 'home/objects_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Объекты'
        context['description'] = ""
        context['keywords'] = ""
        return context


class ready_object(DetailView):
    """ Объект """
    model = Object
    template_name = 'home/object.html'

    # def get_queryset(self):
    #     return


class AdviseFreeView(View):
    """Заявки"""

    def post(self, request):
        response_data = {}
        form = AdviseFreeForm(request.POST)
        if form.is_valid():
            form.save()
            response_data['status'] = True
            response_data['message'] = 'Спасибо'
        else:
            response_data['status'] = False
            response_data['message'] = 'Ошибка'
        return JsonResponse(response_data, safe=False)


class ResumeFreeView(View):
    """Резюме"""

    def post(self, request):
        response_data = {}
        form = ResumeFreeForm(request.POST)
        if form.is_valid():
            form.save()
            response_data['status'] = True
            response_data['message'] = 'Спасибо'
        else:
            response_data['status'] = False
            response_data['message'] = 'Ошибка'
        return JsonResponse(response_data, safe=False)


class OrderPaymentView(View):
    """Форма Заказа расчета"""

    def post(self, request):
        response_data = {}
        form = OrderPaymentForm(request.POST)
        if form.is_valid():
            form.save()
            response_data['status'] = True
            response_data['message'] = 'Спасибо'
        else:
            response_data['status'] = False
            response_data['message'] = 'Ошибка'
        return JsonResponse(response_data, safe=False)
