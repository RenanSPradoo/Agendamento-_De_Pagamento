from rest_framework import serializers
from .models import AgendamentoPagamento

class AgendamentoPagamentoSerializer(serializers.ModelSerializer):
    valor_pagamento = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = AgendamentoPagamento
        fields = '__all__'

    def validate_valor_pagamento(self, value):
        return int(value * 100)
