from django.contrib import admin
from fieldsets_with_inlines import FieldsetsInlineMixin

from Home.models import Services, Slider_os, Slider_four, Demands, Advantages, Contact, Work, Employee, \
    LegalDocumentation, AdviseFree, Vacancy, Requirement, Tasks, Conditions, Resume, Solutions, Pluses, \
    SliderSolutionsOs, DemandsSolutionOne, DemandsSolutionTwo, DemandsSolution, ExampleSlider, Object, SliderObject, \
    PhotoObject, OrderPayment


# Админка для Services услуг
class Slider_os_Inline(admin.TabularInline):
    """Слайдер на Основе"""
    model = Slider_os
    extra = 1
    verbose_name_plural = 'Слайдер для основаниея'
    classes = ['collapse']


class Slider_fourInline(admin.TabularInline):
    """Слайдер на блоке 4"""
    model = Slider_four
    extra = 1
    verbose_name_plural = 'Слайдер на блоке 4'
    classes = ['collapse']


class DemandsInline(admin.TabularInline):
    """Требованиея"""
    model = Demands
    extra = 1
    verbose_name_plural = 'Список Требований'
    classes = ['collapse']
    max_num = 5


class AdvantagesInline(admin.TabularInline):
    """Преимущества"""
    model = Advantages
    extra = 1
    verbose_name_plural = 'Преимущества'
    classes = ['collapse']
    max_num = 3


class ExampleSliderInline(admin.TabularInline):
    """Примера работ"""
    model = ExampleSlider
    extra = 1
    verbose_name_plural = 'Примеры'
    classes = ['collapse']


@admin.register(Services)
class ServicesAdmin(FieldsetsInlineMixin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ("name", 'slug')
    save_on_top = True
    fieldsets_with_inlines = [
        ('Начало', {
            "fields": ("name", 'slug', 'price', "osv_image",)
        }),
        ('Основание', {
            "classes": ("collapse",),
            "fields": ("description_os", "images_os",),
        }),
        Slider_os_Inline,
        ('Блок два', {
            "classes": ("collapse",),
            "fields": ("title", 'images_two', 'description_two')
        }),
        ("Блок три", {
            "classes": ("collapse",),
            "fields": ("title_three", "description_three_1", "description_three_2", "description_three_3",
                       'images_three')
        }),
        ('Блок четыре', {
            "classes": ("collapse",),
            "fields": ("title_four", "description_four_1", "description_four_2", "description_four_3"),
        }),
        Slider_fourInline,
        ("Требования", {
            "classes": ("collapse",),
            "fields": ('demand',),
        }),
        DemandsInline,
        AdvantagesInline,
        ExampleSliderInline
    ]


# Конец настройки для услуг
# Контакты
class WorkInline(admin.TabularInline):
    """технология работы"""
    model = Work
    extra = 1
    verbose_name = 'Техналогия работы'
    verbose_name_plural = 'технологии работ'
    classes = ['collapse']


class EmployeeInline(admin.StackedInline):
    """Ключевые сотрудники"""
    model = Employee
    extra = 1
    verbose_name = 'Сотрудник'
    verbose_name_plural = 'Ключевые сотрудники'
    classes = ['collapse']


class LegalDocumentationInline(admin.TabularInline):
    """ПРАВОВАЯ ДОКУМЕНТАЦИЯ"""
    model = LegalDocumentation
    extra = 1
    verbose_name = 'Документ'
    verbose_name_plural = 'ПРАВОВАЯ ДОКУМЕНТАЦИЯ'
    classes = ['collapse']


@admin.register(Contact)
class ContactAdmin(FieldsetsInlineMixin, admin.ModelAdmin):
    list_display = ("phone", 'email')
    fieldsets_with_inlines = [
        ('Контакты', {
            "fields": ("phone", 'email')
        }),
        ('Адресс', {
            "fields": ("address", 'address_map')
        }),
        ('Реквизиты', {
            "classes": ("collapse",),
            "fields": ["inn", 'kpp', 'payment', 'bank', 'ogrn']
        }),
        ('Документы', {
            "classes": ("collapse",),
            "fields": ("doc_potent", 'doc_licenses', 'doc_bank')
        }),
        WorkInline,
        EmployeeInline,
        LegalDocumentationInline,
    ]

    def has_add_permission(self, request):
        # check if generally has add permission
        retVal = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if retVal and Contact.objects.exists():
            retVal = False
        return retVal


# Формы
@admin.register(AdviseFree)
class AdviseFree(admin.ModelAdmin):
    list_display = ('name', 'phone', 'data', 'state',)
    list_editable = ('state',)
    readonly_fields = ('name', 'phone', 'data',)
    list_filter = ('state',)

    def has_add_permission(self, request):
        return False

    # def save_model(self, request, obj, form, change):
    #     pass


# Вакансии
class RequirementInline(admin.TabularInline):
    """Трабования к вакансии"""
    model = Requirement
    extra = 1
    # verbose_name = 'Техналогия работы'
    # verbose_name_plural = 'технологии работ'
    classes = ['collapse']


class TasksInline(admin.TabularInline):
    """Задачи к вакансии"""
    model = Tasks
    extra = 1
    # verbose_name = 'Техналогия работы'
    # verbose_name_plural = 'технологии работ'
    classes = ['collapse']


class ConditionsInline(admin.TabularInline):
    """Условния к вакансии"""
    model = Conditions
    extra = 1
    # verbose_name = 'Техналогия работы'
    # verbose_name_plural = 'технологии работ'
    classes = ['collapse']


# class ResumeInline(admin.TabularInline):
#     """Условния к вакансии"""
#     model = Resume
#     extra = 1
#     readonly_fields = ['name', 'phone', 'url', 'data']
#     # verbose_name = 'Техналогия работы'
#     # verbose_name_plural = 'технологии работ'
#     classes = ['collapse']


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ("name", 'price', 'state')
    list_editable = ('state',)
    inlines = [RequirementInline, TasksInline, ConditionsInline]
    save_on_top = True
    fields = ("name", 'slug', 'price', 'description', "state",)


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'url', 'data', 'state')
    readonly_fields = ('name', 'phone', 'data', 'url',)
    list_editable = ('state',)
    list_filter = ('state',)

    def has_add_permission(self, request):
        return False


# Готовые решения
class PlusesInline(admin.TabularInline):
    """Условния к вакансии"""
    model = Pluses
    extra = 1
    max_num = 4
    verbose_name = 'Плюсь'
    verbose_name_plural = 'Плюсы'
    classes = ['collapse']


class SliderSolutionsOsInline(admin.TabularInline):
    """Слайдер на Основе"""
    model = SliderSolutionsOs
    extra = 1
    verbose_name_plural = 'Слайдер для основаниея'
    classes = ['collapse']


class DemandsSolutionOneInline(admin.TabularInline):
    """Плюсы 1 для блока 4"""
    model = DemandsSolutionOne
    extra = 1
    verbose_name_plural = 'Плюсы 1 для блока 4'
    classes = ['collapse']


class DemandsSolutionTwoInline(admin.TabularInline):
    """Плюсы 2 для блока 4"""
    model = DemandsSolutionTwo
    extra = 1
    verbose_name_plural = 'Плюсы 2 для блока 4'
    classes = ['collapse']


class DemandsSolutionInline(admin.TabularInline):
    """Требования"""
    model = DemandsSolution
    extra = 1
    verbose_name_plural = 'Требования'
    classes = ['collapse']


@admin.register(Solutions)
class SolutionsAdmin(FieldsetsInlineMixin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ("title", 'description')
    save_on_top = True
    fieldsets_with_inlines = [
        ('Начало', {
            "fields": ("title", 'slug', 'price', "images_png", 'description', 'images_fon')
        }),
        PlusesInline,
        ('Основание', {
            "classes": ("collapse",),
            "fields": ("description_os_1", "description_os_2",),
        }),
        SliderSolutionsOsInline,
        ('Блок два', {
            "classes": ("collapse",),
            "fields": ("title_two", 'images_two', 'description_two_1', 'description_two_2')
        }),
        ("Блок три", {
            "classes": ("collapse",),
            "fields": ("title_three", "description_three_1", "description_three_2", "description_three_3",)
        }),
        ('Блок четыре', {
            "classes": ("collapse",),
            "fields": ("title_four", "subtitle", "images_four_1", "images_four_2"),
        }),
        DemandsSolutionOneInline,
        DemandsSolutionTwoInline,
        ("Требования", {
            "classes": ("collapse",),
            "fields": ('demand',),
        }),
        DemandsSolutionInline,
        ("Конец", {
            "fields": ('description_finish',),
        }),
    ]


# Обекты
class SliderObjectInline(admin.TabularInline):
    """Требования"""
    model = SliderObject
    extra = 1
    verbose_name_plural = 'Cлайдер'
    classes = ['collapse']


class PhotoObjectInline(admin.TabularInline):
    """Требования"""
    model = PhotoObject
    extra = 1
    verbose_name_plural = 'Фото объекта'
    classes = ['collapse']


@admin.register(Object)
class ObjectAdmin(FieldsetsInlineMixin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ("name", 'description')
    save_on_top = True
    fieldsets_with_inlines = [
        ('На старице со списком', {
            "fields": ("name", 'slug', 'address', "square", 'description', 'images')
        }),
        ('Детально', {
            "classes": ("collapse",),
            "fields": ("address_all", "banner",),
        }),
        ('О проекте один', {
            "classes": ("collapse",),
            "fields": ("title_1", 'description_1', 'images_main')
        }),
        ("О проекте два", {
            "classes": ("collapse",),
            "fields": ("title_2", "description_2", "images_main2")
        }),
        ('О проекте три', {
            "classes": ("collapse",),
            "fields": ("title_3", "description_3", "images_main3", "images_main31"),
        }),
        ("О проекте четыре", {
            "classes": ("collapse",),
            "fields": ('title_4', 'description_4',),
        }),
        SliderObjectInline,
        PhotoObjectInline,
    ]


# Конец

# Форма заказа расчета
@admin.register(OrderPayment)
class OrderPaymentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'service', 'data', 'state')
    readonly_fields = ('name', 'phone', 'data', 'service',)
    list_editable = ('state',)
    list_filter = ('state',)

    def has_add_permission(self, request):
        return False
