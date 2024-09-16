from django.db import models

class AgendamentoPagamento(models.Model):
    data_pagamento = models.DateField()
    permite_recorrencia = models.BooleanField(default=False)
    quantidade_recorrencia = models.PositiveIntegerField()
    intervalo_recorrencia = models.PositiveIntegerField()
    status_recorrencia = models.CharField(max_length=50)
    agencia = models.PositiveIntegerField()
    conta = models.PositiveIntegerField()
    valor_pagamento = models.IntegerField()  # Armazenado como inteiro

    def save(self, *args, **kwargs):
        # Convertendo o valor_pagamento de decimal para inteiro antes de salvar
        if isinstance(self.valor_pagamento, float):
            self.valor_pagamento = int(self.valor_pagamento * 100)  # Corrigido: multiplicar por 100
        super(AgendamentoPagamento, self).save(*args, **kwargs)

    def __str__(self):
        return f"Agendamento {self.id} - {self.data_pagamento}"
