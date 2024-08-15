import os
import sqlite3
import sys
import time
sys.path.append('../')
from voice_recognition.recognition import recognize_speech

def clear_screen():
    # Limpa a tela no Windows e Unix-like sistemas
    os.system('cls' if os.name == 'nt' else 'clear')
    
def get_random_kana(kana_type, db_path='../database/japanese.db'):
    print(db_path)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f'SELECT romaji, kana FROM {kana_type} ORDER BY RANDOM() LIMIT 1')
    result = cursor.fetchone()
    conn.close()
    return result

def check_kana_input(kana_type, user_input, db_path='../database/japanese.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f'SELECT romaji, kana FROM {kana_type} WHERE romaji = ? OR kana = ?', (user_input, user_input))
    result = cursor.fetchone()
    conn.close()
    return result

def main_menu():
    clear_screen()
    print("Japanese Learner")
    print("\nO que deseja praticar hoje")
    print("1. Escrita")
    print("2. Fala")
    choice = input("\nEscolha uma opção (1 ou 2): ")
    if choice == '1':
        writing_menu()
    elif choice == '2':
        speaking_menu()
        main_menu()
    else:
        print("Opção inválida. Tente novamente.")
        input("\nPressione Enter para voltar ao menu principal.")
        main_menu()

def writing_menu():
    clear_screen()
    print("Escolha o que deseja treinar:")
    print("1. Hiragana")
    print("2. Katakana")
    choice = input("\nEscolha uma opção (1 ou 2): ")
    if choice == '1' or choice == '１':
        kana_writing_menu("hiragana")
    elif choice == '2' or choice == '２':
        kana_writing_menu("katakana")
    else:
        print("Opção inválida. Tente novamente.")
        input("\nPressione Enter para voltar ao menu anterior.")
        writing_menu()

def kana_writing_menu(kana_type):
    clear_screen()
    print(f"Escrever em {kana_type.capitalize()}")
    print("\nEscolha uma opção:")
    print("1. Escrever em kana")
    print("2. Escrever em romaji")
    choice = input("\nEscolha uma opção (1 ou 2): ")
    
    if choice == '1' or choice == '１':
        practice_kana(kana_type)
    elif choice == '2' or choice == '２':
        practice_romaji(kana_type)
    else:
        print("Opção inválida. Tente novamente.")
        input("\nPressione Enter para voltar ao menu anterior.")
        kana_writing_menu(kana_type)
    input("\nPressione Enter para voltar ao menu principal.")
    main_menu()

def practice_romaji(kana_type):
    clear_screen()
    romaji, kana = get_random_kana(kana_type)
    print(f"Escreva o seguinte kana em romaji: {kana}")
    user_input = input("Seu input: ")
    result = check_kana_input(kana_type, user_input)
    if user_input == romaji:
        print("Correto!")
    else:
        print(f"Incorreto. A resposta correta é: {romaji}")
    input("\nPressione Enter para continuar.")
    kana_writing_menu(kana_type)

def practice_kana(kana_type):
    try:
        clear_screen()
        romaji, kana = get_random_kana(kana_type)
        print(f"Escreva o seguinte romaji em kana: {romaji}")
        user_input = input("Seu input: ")
        if user_input == kana:
            print("Correto!")
        else:
            print(f"Incorreto. A resposta correta é: {kana}")
    except Exception as e:
        print(f"Erro ao acessar o banco de dados: {e}")
    input("\nPressione Enter para continuar.")
    kana_writing_menu(kana_type)    

def speaking_menu():
    clear_screen()
    print("Escolha o que deseja treinar:")
    print("1. Hiragana")
    print("2. Katakana")
    choice = input("\nEscolha uma opção (1 ou 2): ")
    if choice == '1' or choice == '１':
        kana_speaking_menu("hiragana")
    elif choice == '2' or choice == '２':
        kana_speaking_menu("katakana")
    else:
        print("Opção inválida. Tente novamente.")
        input("\nPressione Enter para voltar ao menu anterior.")
        writing_menu()
        
def kana_speaking_menu(kana_type):
    clear_screen()
    print(f"Praticar fala do {kana_type.capitalize()}")
    romaji, kana = get_random_kana(kana_type)
    answer = recognize_speech(kana, romaji)
        
    if answer == 'correto':
        print("Correto!")
    else:
        print(f"Incorreto. A resposta correta é: {romaji}")
        
    input("\nPressione Enter para continuar.")
    kana_speaking_menu(kana_type)       
        
if __name__ == "__main__":
    main_menu()
