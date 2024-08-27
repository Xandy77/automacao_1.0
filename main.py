
import pyautogui as auto
import time

# Define o atraso padrão para os comandos
auto.PAUSE = 0.5

def upload_to_github():
    # Abre o menu iniciar e busca pelo navegador
    auto.hotkey('win', 'r')  # Abre a caixa de execução
    auto.write('chrome')
    auto.press('enter')
    
    # Aguarda o navegador abrir
    time.sleep(5)
    
    # Maximiza a janela do navegador
    auto.hotkey('alt', 'space')
    auto.press('x')
    
    # Acessa o site do GitHub
    auto.write('github.com')
    auto.press('enter')
    
    # Aguarda a página do GitHub carregar
    time.sleep(10)
    
    # Navega para a página de login
    for _ in range(12):  # Ajuste o número de pressões se necessário
        auto.press('tab')
    
    # Pressiona 'enter' para ir para o formulário de login
    auto.press('enter')
    
    # Aguarda a página de login carregar
    time.sleep(5)
    
    # Digita o nome de usuário e senha (preencha com suas credenciais)
    auto.write('Xandy77')  # Substitua pelo seu nome de usuário
    auto.press('tab')
    auto.write('Bonekinh@@@.12')  # Substitua pela sua senha
    auto.press('enter')
    
    # Aguarda o login ser realizado
    time.sleep(10)
    
    # Acessa a página do repositório (substitua pela URL do seu repositório)
    auto.write('https://github.com/Xandy77/automacao_1.0.git')  # Substitua pela URL do seu repositório
    auto.press('enter')
    
    # Aguarda a página do repositório carregar
    time.sleep(10)
    
    # Navega para a aba de "Code"
    auto.hotkey('alt', 'c')
    
    # Aguarda a aba de "Code" carregar
    time.sleep(3)
    
    # Entra na opção de "Upload files"
    auto.press('tab', presses=5, interval=0.5)
    auto.press('enter')
    
    # Aguarda a página de upload carregar
    time.sleep(5)

# Executa a função
upload_to_github()