

#Mexe no teu pc para automacoes
import pyautogui
import time


# Passo 1: Entrar no sistema da empresa

def main():
    pyautogui.PAUSE = 0.5
    link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
    pyautogui.press("win")
    pyautogui.write("Chrome")
    pyautogui.press("enter")
    pyautogui.click(x=835, y=475) #Selecionar o perfil do chrome


    pyautogui.write(link)
    pyautogui.press("enter")
# Fazer uma pausa maior pois mexe com a internet e pra dar tempo pro site carregar
    time.sleep(3)
    pyautogui.click(x=674, y=447) #Baseado em 1920x1080
    pyautogui.write("pythonimpressionador@gmail.com") #Email
    pyautogui.press("tab")
    pyautogui.write("sua senha") #Senha
    pyautogui.press("tab")
    pyautogui.press("enter")

    #Pausa pro formulario carregar
    time.sleep(3)

# Passo 2: Fazer login
# Passo 3: Abrir a base de dados
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o passo 4 ate acabar a lista de produtos
main()