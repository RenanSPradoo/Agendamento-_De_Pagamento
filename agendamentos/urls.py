from django.urls import path
from .views import AgendamentoPagamentoCreateView, AgendamentoPagamentoListView, AgendamentoPagamentoDetailView

urlpatterns = [
    path('api/agendamentos/', AgendamentoPagamentoCreateView.as_view(), name='criar_agendamento'),
    path('api/agendamentos/list/', AgendamentoPagamentoListView.as_view(), name='listar_agendamentos'),
    path('api/agendamentos/<int:pk>/', AgendamentoPagamentoDetailView.as_view(), name='detalhar_agendamento'),
]
