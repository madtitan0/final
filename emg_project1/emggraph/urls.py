from django.urls import path
from emggraph.views import emg_graph

urlpatterns = [
    # ... other URL patterns ...
    path('emggraph/', emg_graph, name='emg_graph'),
]
