from django.shortcuts import render
from .models import Hiragana
import random
import pdb


# Create your views here.
def home(request):
    return render(request, "home.html")

def hiragana(request):
    # Obter todos os registros de hiragana
    hiragana_list = list(Hiragana.objects.all())
    
    # Inicializar a variável selected_hiragana
    selected_hiragana = None
    message = None
    correct_hiragana = None

    # Se for um POST, verificar a resposta do usuário
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '').strip()
        hiragana_id = request.POST.get('hiragana_id')

        # Recupera o kana que foi mostrado antes de submeter o formulário
        try:
            selected_hiragana = Hiragana.objects.get(id=hiragana_id)
            correct_hiragana = selected_hiragana
        except Hiragana.DoesNotExist:
            selected_hiragana = None

        # Verifica se a resposta do usuário está correta
        if selected_hiragana and user_input == selected_hiragana.romaji:
            message = "CORRETO!"
        else:
            message = "INCORRETO! O romaji correto é "

        # Gera um novo kana aleatório para a próxima exibição
        selected_hiragana = random.choice(hiragana_list) if hiragana_list else None
    else:
        # Gera um kana aleatório na primeira exibição
        selected_hiragana = random.choice(hiragana_list) if hiragana_list else None
    
    # Passar o kana selecionado e a mensagem para o template
    context = {
        'selected_hiragana': selected_hiragana,
        'correct_hiragana': correct_hiragana,
        'message': message,
    }

    return render(request, "hiragana.html", context)

def katakana(request):
    return render(request, "katakana.html")