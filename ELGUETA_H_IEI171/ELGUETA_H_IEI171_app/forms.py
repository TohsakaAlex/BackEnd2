from django import forms
from ELGUETA_H_IEI171_app.models import Reserva

class FormReserva(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'