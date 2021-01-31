from django.templatetags.tz import register
import pymorphy2


@register.filter
def inflect_name(name: str, data: str):
    case, number = data.split(',')
    morph = pymorphy2.MorphAnalyzer()
    word = morph.parse(name)[0]
    return word.inflect({case, number}).word


@register.filter
def phone_set(number: str):
    return '+7 ({}{}{}) {}{}{}-{}{}-{}{}'.format(*number)


@register.filter
def order_all(model, method):
    return model.order_by(method).all()


@register.filter
def look_title(number, name):
    morph = pymorphy2.MorphAnalyzer()
    butyavka = morph.parse(name)[0]
    return f'{number} {butyavka.make_agree_with_number(number).word}'


@register.filter(name='times')
def times(number):
    return range(number)
# техналогия бетоннгого inflect({'gent','sing'}) пола
# Приемущества бетонных plur,gent полов
