from django.db import models
from django.urls import reverse


# Услуги
class Services(models.Model):
    name = models.CharField(verbose_name='Наименование Услуги', max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    price = models.IntegerField(verbose_name='Цена')
    osv_image = models.ImageField(verbose_name='Фотография главная', upload_to='images/osv/')
    # CEO
    seo_keywords = models.TextField(verbose_name='Слова поиска', help_text='Полы;Полы по 400 руб;')
    seo_description = models.TextField(verbose_name='Описание сео', help_text='')
    # Основание
    description_os = models.TextField(verbose_name='Описание Основания')
    images_os = models.ImageField(verbose_name='Фото Основания', upload_to='images/base/')
    # slider_os
    # Блок два
    images_two = models.ImageField(verbose_name='Фото Основания', upload_to='images/two/')
    title = models.CharField(max_length=200, verbose_name='Название второго блока')
    description_two = models.TextField(verbose_name='Описание второго блока')
    # Блок три
    images_three = models.ImageField(verbose_name='Фото Основания', upload_to='images/three/')
    title_three = models.CharField(max_length=200, verbose_name='Название третьего блока')
    description_three_1 = models.TextField(verbose_name='Описание_1 третьего блока')
    description_three_2 = models.TextField(verbose_name='Описание_2 третьего блока')
    description_three_3 = models.TextField(verbose_name='Описание_3 третьего блока')
    # Блок четыре
    title_four = models.CharField(max_length=200, verbose_name='Название четвертого блока')
    description_four_1 = models.TextField(verbose_name='Описание_1 четвертого блока')
    description_four_2 = models.TextField(verbose_name='Описание_2 четвертого блока')
    description_four_3 = models.TextField(verbose_name='Описание_3 четвертого блока')
    # slider_four
    # Требования
    demand = models.CharField(max_length=100, verbose_name='Описание требования')

    # demands
    # Преимущества
    # Advantages
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('concrete_floors', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class Slider_os(models.Model):
    service = models.ForeignKey(Services, verbose_name="Услуга", on_delete=models.CASCADE)
    img = models.ImageField(verbose_name='Фотография', upload_to='images/slider/base/')


class Slider_four(models.Model):
    service = models.ForeignKey(Services, verbose_name="Услуга", on_delete=models.CASCADE)
    img = models.ImageField(verbose_name='Фотография', upload_to='images/slider/four/')


class Demands(models.Model):
    service = models.ForeignKey(Services, verbose_name="Услуга", on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Наименование требования', max_length=50)
    description = models.CharField(verbose_name='Краткое пояснение требования', max_length=100, null=True, blank=True)


class Advantages(models.Model):
    service = models.ForeignKey(Services, verbose_name="Услуга", on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Наименование требования', max_length=50)
    img = models.ImageField(verbose_name='Фотография', upload_to='images/advantages/')


class ExampleSlider(models.Model):
    service = models.ForeignKey(Services, verbose_name="Услуга", on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Наимемование примера', max_length=50)
    img = models.ImageField(verbose_name='Фотография', upload_to='images/Example/')


# Конец Услуги
# Готовые решения
class Solutions(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    images_png = models.TextField(verbose_name='Фотография иконки')
    description = models.TextField(verbose_name='Краткое описание')
    slug = models.SlugField(max_length=200, unique=True)
    price = models.IntegerField(verbose_name='Цена')
    # SEO
    seo_keywords = models.TextField(verbose_name='Слова поиска', help_text='ПолыПполы по 400 руб;')
    seo_description = models.TextField(verbose_name='Описание сео', help_text='')
    # Плюсы
    images_fon = models.ImageField(verbose_name='Фотография для фона', upload_to='images/solutions/fon')
    # Pluses
    # Основание
    description_os_1 = models.TextField(verbose_name='Описание Основания')
    description_os_2 = models.TextField(verbose_name='Описание Основания')
    # SliderSolutionsOs
    # Блок два
    images_two = models.ImageField(verbose_name='Фото Блок два', upload_to='images/solutions/two/')
    title_two = models.CharField(max_length=200, verbose_name='Название второго блока')
    description_two_1 = models.TextField(verbose_name='Описание второго блока 1')
    description_two_2 = models.TextField(verbose_name='Описание второго блока 2')
    # Блок три
    title_three = models.CharField(max_length=200, verbose_name='Название третьего блока')
    description_three_1 = models.TextField(verbose_name='Описание_1 третьего блока')
    description_three_2 = models.TextField(verbose_name='Описание_2 третьего блока')
    description_three_3 = models.TextField(verbose_name='Описание_3 третьего блока')
    # Блок четыре
    title_four = models.CharField(max_length=200, verbose_name='Название четвертого блока')
    subtitle = models.CharField(max_length=200, verbose_name='Подзаголовок  третьего блока')
    images_four_1 = models.ImageField(verbose_name='Фото Блок четыре 1', upload_to='images/solutions/four/one/')
    # DemandsSolutionOne
    images_four_2 = models.ImageField(verbose_name='Фото Блок четыре 2', upload_to='images/solutions/four/two/')
    # DemandsSolutionTwo
    # Требования
    demand = models.CharField(max_length=100, verbose_name='Описание требования')
    # DemandsSolution
    # Конец
    description_finish = models.TextField(verbose_name='Описание в конце')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ready_solution', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Готовое решение"
        verbose_name_plural = "Готовые решения"


class Pluses(models.Model):
    """Плюсы готовых решений """
    solution = models.ForeignKey(Solutions, verbose_name="Готовое решение", on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание', max_length=100)


class SliderSolutionsOs(models.Model):
    solution = models.ForeignKey(Solutions, verbose_name="Готовое решение", on_delete=models.CASCADE)
    img = models.ImageField(verbose_name='Фотография', upload_to='images/slider/solution/base/')


class DemandsSolutionOne(models.Model):
    solution = models.ForeignKey(Solutions, verbose_name="Готовое решение", on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Действие', max_length=200)
    index = models.IntegerField(verbose_name='Индекс шага')


class DemandsSolutionTwo(models.Model):
    solution = models.ForeignKey(Solutions, verbose_name="Готовое решение", on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Действие', max_length=200)
    index = models.IntegerField(verbose_name='Индекс шаг')


class DemandsSolution(models.Model):
    solution = models.ForeignKey(Solutions, verbose_name="Готовое решение", on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Наименование требования', max_length=50)
    description = models.CharField(verbose_name='Краткое пояснение требования', max_length=100, null=True, blank=True)


# Конец

# Контакты
class Contact(models.Model):
    address = models.CharField(verbose_name='Адрес', max_length=500)
    address_map = models.CharField(verbose_name='Адрес на карте', max_length=500)
    phone = models.CharField(verbose_name='Телефон', max_length=10)
    email = models.EmailField(verbose_name='Email')
    inn = models.CharField(verbose_name='ИНН', max_length=200)
    kpp = models.CharField(verbose_name='КПП', max_length=200)
    payment = models.CharField(verbose_name='Расчетный счет', max_length=200)
    bank = models.CharField(verbose_name='Банк', max_length=200)
    ogrn = models.CharField(verbose_name='ОГРН', max_length=200)
    doc_potent = models.FileField(verbose_name='Документ о патенте', upload_to='file/doc/')
    doc_licenses = models.FileField(verbose_name='Лицензии', upload_to='file/doc/')
    doc_bank = models.FileField(verbose_name='Файл Реквезитов', upload_to='file/doc/')

    class Meta:
        verbose_name = "Кантакт"
        verbose_name_plural = "Контакты"


class Work(models.Model):
    """технология работы"""
    contact = models.ForeignKey(Contact, verbose_name="Услуга", on_delete=models.CASCADE)
    index = models.IntegerField(verbose_name='Индекс шага')
    images = models.ImageField(verbose_name='Фотография', upload_to='images/work/')
    description = models.TextField(verbose_name='Краткое описание')


class Employee(models.Model):
    """Ключевые сотрудники"""
    contact = models.ForeignKey(Contact, verbose_name='Сайт', on_delete=models.CASCADE)
    fio = models.CharField(verbose_name='ФИО сотрудника', max_length=500)
    images = models.ImageField(verbose_name='Фотография сотрудника', upload_to='images/user/')
    description = models.TextField(verbose_name='Описание')
    phone = models.CharField(verbose_name='Телефон', max_length=10)
    email = models.EmailField(verbose_name='Email')


class LegalDocumentation(models.Model):
    """ПРАВОВАЯ ДОКУМЕНТАЦИЯ"""
    contact = models.ForeignKey(Contact, verbose_name='Сайт', on_delete=models.CASCADE)
    images = models.ImageField(verbose_name='Фотография Документа', upload_to='images/doc/')
    description = models.TextField(verbose_name='Описание', max_length=500)


# Конец
# Вакансии
class Vacancy(models.Model):
    name = models.CharField(verbose_name='Наименование Вакансии', max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    price = models.IntegerField(verbose_name='Зарплата')
    description = models.TextField(verbose_name='Описание', max_length=500)
    state = models.BooleanField(verbose_name='Открытая вакансия', default=False)
    # CEO
    seo_keywords = models.TextField(verbose_name='Слова поиска', help_text='Полы;Полы по 400 руб;')
    seo_description = models.TextField(verbose_name='Описание сео', help_text='')

    def get_absolute_url(self):
        return reverse('vacancy', kwargs={"slug": self.slug})

    # Требования
    # requirement
    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"


class Requirement(models.Model):
    vacancy = models.ForeignKey(Vacancy, verbose_name='Вакансия', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание', max_length=500)

    class Meta:
        verbose_name = "Требование"
        verbose_name_plural = "Трепования"


class Tasks(models.Model):
    vacancy = models.ForeignKey(Vacancy, verbose_name='Вакансия', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание', max_length=500)

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class Conditions(models.Model):
    vacancy = models.ForeignKey(Vacancy, verbose_name='Вакансия', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание', max_length=500)

    class Meta:
        verbose_name = "Условие"
        verbose_name_plural = "Условия"


class Resume(models.Model):
    """ Форма для резюме"""
    name = models.CharField(verbose_name='Имя', max_length=200)
    phone = models.CharField(verbose_name='Телефон', max_length=25)
    url = models.URLField(verbose_name='Ссылка на резюме', blank=True)
    data = models.DateTimeField(verbose_name='Время запроса', auto_now=True)
    state = models.BooleanField(verbose_name='Провели консультацию', default=False)

    def __str__(self):
        return f"Резюме от {self.name}"

    class Meta:
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"


# Конец
# Формы связи
class AdviseFree(models.Model):
    """Форма бесплатной консультации"""
    name = models.CharField(verbose_name='Имя', max_length=200)
    phone = models.CharField(verbose_name='Телефон', max_length=25)
    data = models.DateTimeField(verbose_name='Время запроса', auto_now=True)
    state = models.BooleanField(verbose_name='Провели консультацию', default=False)

    def __str__(self):
        return f"Заявка от {self.name}"

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"


class OrderPayment(models.Model):
    """Форма Заказа расчета"""
    service = models.ForeignKey(Services, verbose_name="Услуга", on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Имя', max_length=200)
    phone = models.CharField(verbose_name='Телефон', max_length=25)
    data = models.DateTimeField(verbose_name='Время запроса', auto_now=True)
    state = models.BooleanField(verbose_name='Провели консультацию', default=False)

    def __str__(self):
        return f"Заказ расчета от {self.name}"

    class Meta:
        verbose_name = "Заказа расчета"
        verbose_name_plural = "Заказы расчета"


# Конец


# Объекты
class Object(models.Model):
    """" Объекты """
    # Основыне на list
    name = models.CharField(verbose_name='Наименование Объекта', max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(verbose_name='Описание', max_length=500)
    address = models.CharField(verbose_name='Адресс', max_length=50)
    square = models.IntegerField(verbose_name='Площадь')
    images = models.ImageField(verbose_name='Фотография Объекта', upload_to='images/item/')
    # CEO
    seo_keywords = models.TextField(verbose_name='Слова поиска', help_text='Полы;Полы по 400 руб;')
    seo_description = models.TextField(verbose_name='Описание сео', help_text='')
    # Детально
    address_all = models.CharField(verbose_name='Адресс полностью', max_length=200)
    banner = models.ImageField(verbose_name='Баннер', upload_to='images/banner/')
    # Мы хотим рассказать об этом проекте
    title_1 = models.CharField(verbose_name='Название задачи', max_length=200, help_text='Основная задача')
    description_1 = models.TextField(verbose_name='Описание основной задачи')
    images_main = models.ImageField(verbose_name='Фотография Основная задача', upload_to='images/item/')
    # два
    title_2 = models.CharField(verbose_name='Название задачи', max_length=200, help_text='Мы составили план работы')
    description_2 = models.TextField(verbose_name='Описание')
    images_main2 = models.ImageField(verbose_name='Фотография', upload_to='images/item/')
    # три
    title_3 = models.CharField(verbose_name='Название задачи', max_length=200, help_text='Как пошло производство')
    description_3 = models.TextField(verbose_name='Описание')
    images_main3 = models.ImageField(verbose_name='Фотография', upload_to='images/item/')
    images_main31 = models.ImageField(verbose_name='Фотография', upload_to='images/item/')
    # четыре
    title_4 = models.CharField(verbose_name='Название задачи', max_length=200, help_text='Сдача проекта')
    description_4 = models.TextField(verbose_name='Описание')

    # слайдер
    # SliderObject
    # Фото объекта PhotoObject
    def get_absolute_url(self):
        return reverse('ready_object', kwargs={"slug": self.slug})

    def __str__(self):
        return f"Объект {self.name}"

    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"


class SliderObject(models.Model):
    object = models.ForeignKey(Object, verbose_name="Объекты", on_delete=models.CASCADE)
    img = models.ImageField(verbose_name='Фотография', upload_to='images/slider/object/base/')


class PhotoObject(models.Model):
    object = models.ForeignKey(Object, verbose_name="Объекты", on_delete=models.CASCADE)
    img = models.ImageField(verbose_name='Фото объекта', upload_to='images/slider/object/end/')
    title = models.CharField(verbose_name='Название', max_length=200, help_text='Фасад')


# Виды промышленных полов
class TypeFloor(models.Model):
    service = models.ForeignKey(Services, verbose_name="Услуга", on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание')
    images = models.ImageField(verbose_name='Основанное фото', upload_to='images/slider/TypeFloor')
    images2 = models.ImageField(verbose_name='Фото разреза', upload_to='images/slider/TypeFloor')

    class Meta:
        verbose_name = 'Промышленный пол'
        verbose_name_plural = 'Виды промышленных полов'


# конец

class OrderPaymentObject(models.Model):
    """Форма Заказа расчета"""
    service = models.ForeignKey(Object, verbose_name="Объект", on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Имя', max_length=200)
    phone = models.CharField(verbose_name='Телефон', max_length=25)
    data = models.DateTimeField(verbose_name='Время запроса', auto_now=True)
    state = models.BooleanField(verbose_name='Провели консультацию', default=False)

    def __str__(self):
        return f"Заказ расчета от {self.name}"

    class Meta:
        verbose_name = "Заказа расчета объект"
        verbose_name_plural = "Заказы расчета объект"
