from django import forms
from .models import Aldeia


class AldeiaForm(forms.ModelForm):

    class Meta:
        model = Aldeia
        fields = [
            'nome',
            'municipio',
            'populacao',
            'etnia',
            'quantidade_reservatorios',
            'capacidade_total',
            'possui_energia',
            'possui_espaco_ubsi',
            'observacoes',
        ]

        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nome da Aldeia'
                }
            ),
             'municipio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Município'
                }
            ),

            'populacao': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min': 0
                }
            ),

            'etnia': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'quantidade_reservatorios': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min': 0
                }
            ),

            'capacidade_total': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min': 0
                }
            ),

            'observacoes': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4
                }
            ),
        }
        