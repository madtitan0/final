from django.shortcuts import render
from .forms import EMGGraphForm
import subprocess
import sys
def emg_graph(request):
    if request.method == 'POST':
        form = EMGGraphForm(request.POST)
        if form.is_valid():
            port = form.cleaned_data['port']
            baud_rate = form.cleaned_data['baud_rate']
            subprocess.Popen(['python', '/Users/muhammedriyaz/Desktop/gg.py', port, str(baud_rate)])
            return render(request, 'emggraph/graph.html', {'form': form})
    else:
        form = EMGGraphForm()
    return render(request, 'emggraph/form.html', {'form': form})
