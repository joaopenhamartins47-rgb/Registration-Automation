# Registration Automation

Primeiro episódio do curso da Hashtag Treinamentos, onde aprendemos sobre a biblioteca pyautogui. O intuito do projeto é a automação de uma base de dados para cadastrar produtos de forma automática, economizando horas de trabalho manual.

O script lê um CSV com os produtos (código, marca, tipo, categoria, preço, custo e observação) e preenche cada campo sozinho num sistema web, simulando teclado e mouse, até acabar a lista inteira.

As linhas de código foram feitas especificamente pra resolver esse problema de automação no ambiente de treinamento da Hashtag. O email e a senha são meramente ilustrativos, num site sem verificação de login real, e as coordenadas de tela foram usadas de acordo com as posições na minha tela, com resolução 1920x1080 (então rodar em outra resolução provavelmente vai quebrar os cliques).

De resto, resolve um problema real de cadastro manual repetitivo e mostra um pouco do poder da automação com pyautogui.

Stack: Python, pandas (leitura do CSV) e pyautogui (simulação de mouse e teclado).

Pra rodar: `uv sync` e depois `uv run codigo.py`.