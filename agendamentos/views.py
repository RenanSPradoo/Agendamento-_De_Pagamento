from rest_framework import generics
from .models import AgendamentoPagamento
from .serializers import AgendamentoPagamentoSerializer

class AgendamentoPagamentoCreateView(generics.CreateAPIView):
    queryset = AgendamentoPagamento.objects.all()
    serializer_class = AgendamentoPagamentoSerializer

class AgendamentoPagamentoListView(generics.ListAPIView):
    queryset = AgendamentoPagamento.objects.all()
    serializer_class = AgendamentoPagamentoSerializer

class AgendamentoPagamentoDetailView(generics.RetrieveDestroyAPIView):
    queryset = AgendamentoPagamento.objects.all()
    serializer_class = AgendamentoPagamentoSerializer