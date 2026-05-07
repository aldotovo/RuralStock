from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=150)
    unidade = models.CharField(max_length=20)
    quantidade_atual = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome


class Movimentacao(models.Model):
    TIPOS = (
        ('E', 'Entrada'),
        ('S', 'Saída'),
    )
    
    tipo = models.CharField(max_length=1, choices=TIPOS)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.FloatField()
    data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.get_tipo_display()} - {self.produto.nome}"
    
    class Meta:
        verbose_name = "Movimentação"
        verbose_name_plural = "Movimentações"

    def save(self, *args, **kwargs):

        if not self.pk:  # só aplica na criação (evita duplicar)

            if self.tipo == 'E':
                self.produto.quantidade_atual += self.quantidade

            elif self.tipo == 'S':
                    if self.produto.quantidade_atual < self.quantidade:
                        raise ValueError("Estoque insuficiente")

                    self.produto.quantidade_atual -= self.quantidade

            self.produto.save()

        super().save(*args, **kwargs)

