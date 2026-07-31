from django.db import models

ETNIAS = [
    ("GM", "Guarani Mbyá"),
    ("KA", "Kaingang"),
    ("CH", "Charrua"),
    ("XO", "Xokleng"),
]

class Aldeia(models.Model):
    nome = models.CharField(
        max_length=150,
        verbose_name="Nome da Aldeia"
    )

    municipio = models.CharField(
        max_length=100
    )

    estado = models.CharField(
        max_length=2,
        default="RS"
    )

    populacao = models.PositiveIntegerField(
        default=0
    )

    etnia = models.CharField(
        max_length=2,
        choices=ETNIAS,
        verbose_name="Etnia"
    )

    quantidade_reservatorios = models.PositiveSmallIntegerField(
        default=0,
        verbose_name="Quantidade de reservatórios"
    )

    capacidade_total = models.PositiveIntegerField(
        default=0,
        help_text="Capacidade total instalada em litros"
    )

    possui_energia = models.BooleanField(
        default=False
    )

    possui_espaco_ubsi = models.BooleanField(
        default=False
    )

    observacoes = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.nome

