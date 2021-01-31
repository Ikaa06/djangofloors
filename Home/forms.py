from django import forms

from .models import AdviseFree, Resume, OrderPayment


class AdviseFreeForm(forms.ModelForm):
    class Meta:
        model = AdviseFree
        fields = ('name', 'phone')


class ResumeFreeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('name', 'phone', 'url')


class OrderPaymentForm(forms.ModelForm):
    class Meta:
        model = OrderPayment
        fields = ('name', 'phone', 'service')
