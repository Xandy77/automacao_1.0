# importa a biblioteca de automação
# NOTE: instale a biblioteca: pip install pyautogui
import pyautogui as auto

# atrasa os comandos da biblioteca
auto.PAUSE = 0.5

auto.press('win') # abre o menu iniciar
auto.write('chrome') # digita a palavra "chrome"
auto.press('enter') # aperta "Enter"



# a tecla atalho para maximizar tela
auto.hotkey('alt', 'space')
auto.press('x')

auto.write('github.com') # acessa o site do GitHub
auto.press('enter') # aperta "Enter"

# entrar na página do GitHub
for i in range(12):
    auto.press('tab')

auto.press('enter')