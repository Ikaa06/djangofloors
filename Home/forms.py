from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from .models import AdviseFree, Resume, OrderPayment, OrderPaymentObject


class AdviseFreeForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = AdviseFree
        fields = ('name', 'phone', 'captcha')


class ResumeFreeForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Resume
        fields = ('name', 'phone', 'url', 'captcha')


class OrderPaymentForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = OrderPayment
        fields = ('name', 'phone', 'service', 'captcha')


class OrderPaymentObjectForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = OrderPaymentObject
        fields = ('name', 'phone', 'service', 'captcha')
