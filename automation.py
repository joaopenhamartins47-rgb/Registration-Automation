

#Mexe no teu pc para automacoes
import pyautogui
import time
import pandas as pd


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

    # Passo 2: Fazer login
    pyautogui.click(x=840, y=411) #Baseado em 1920x1080
    pyautogui.write("pythonimpressionador@gmail.com") #Email
    pyautogui.press("tab")
    pyautogui.write("sua_senha") #Senha
    pyautogui.press("tab")
    pyautogui.press("enter")

    #Pausa pro formulario carregar
    time.sleep(3)

    # Passo 3: Abrir a base de dados


    df = pd.read_csv("produtos.csv", encoding='utf-8')

    # Passo 4: Cadastrar 1 produto

    for row in df.index:
        pyautogui.click(x=682, y=301) #Clica no campo do codigo
        codigo = str(df.loc[row, "codigo"])
        pyautogui.write(codigo)
        pyautogui.press("tab")

        marca = str(df.loc[row, "marca"])
        pyautogui.write(marca)
        pyautogui.press("tab")

        tipo = str(df.loc[row, "tipo"])
        pyautogui.write(tipo)
        pyautogui.press("tab")

        cat = str(df.loc[row, "categoria"])
        pyautogui.write(cat)
        pyautogui.press("tab")

        preco = str(df.loc[row, "preco_unitario"])
        pyautogui.write(preco)
        pyautogui.press("tab")

        custo = str(df.loc[row, "custo"])
        pyautogui.write(custo)
        pyautogui.press("tab")

        obs = df.loc[row, "obs"]

        if not pd.isna(obs):
            pyautogui.write(str(obs))


        pyautogui.press("tab")
        pyautogui.press("enter")
        #Depois do enter volta para o inicio
        pyautogui.scroll(5000)

# Passo 5: Repetir o passo 4 ate acabar a lista de produtos
main()