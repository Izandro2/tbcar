from captcha.fields import CaptchaField
from django.forms import ModelForm
from core.models import Cliente, Veiculo, Marca, Tabela, Mensalista, Rotativo
from bootstrap_datepicker_plus.widgets import DateTimePickerInput


class FormCliente(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Cliente
        fields = '__all__'

class FormVeiculo(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Veiculo
        fields = '__all__'

class FormMarca(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Marca
        fields = '__all__'

class FormTabela(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Tabela
        fields = '__all__'

class FormMensalista(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Mensalista
        fields = '__all__'

class FormRotativo(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Rotativo
        fields = '__all__'

        widgets = {'entrada': DateTimePickerInput(options={"format":'DD/MM/YYYY hh:mm:ss'}), 'saida':DateTimePickerInput(options={"format":'DD/MM/YYYY hh:mm:ss'})}