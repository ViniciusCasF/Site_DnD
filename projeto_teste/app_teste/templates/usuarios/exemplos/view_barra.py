# views.py
from django.shortcuts import render
from django.http import HttpResponse

def editar_progresso(request):
    if request.method == 'POST':
        progress_values = {
            'progress_value_1': request.POST.get('progress_value_1'),
            'progress_value_2': request.POST.get('progress_value_2'),
            # Adicione mais conforme necessário
        }
        
        # Aqui você pode processar os valores como desejar, por exemplo, salvando no banco de dados
        response_text = '<br>'.join([f'{key} salvo com sucesso: {value}' for key, value in progress_values.items()])
        return HttpResponse(response_text)
    
    # Exemplo de valores iniciais e pontos disponíveis
    context = {
        'initial_value_1': 8,
        'initial_value_2': 9,
        # Adicione mais valores iniciais conforme necessário
        'total_points': 27
    }
    return render(request, 'points_progress_bars.html', context)
