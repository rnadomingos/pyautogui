## Acesso ao NBS e Consulta ao Sistema

import pyautogui
import time

# START
pyautogui.alert(text='Atenção, não mexa em nada agora, o robo vai iniciar o processo', 
                title='START ROBOT', 
                button='OK')
pyautogui.PAUSE = 0.5
# acessar area de trabalho

# ajusta para teclado do NOTE 
pyautogui.moveTo(1132, 0)
pyautogui.click()
pyautogui.moveTo(1132, 50) 
pyautogui.click()
time.sleep(3)


pyautogui.hotkey('winleft', 'd')
# abrir terminal
pyautogui.hotkey('ctrl', 'alt', 't')
# acessar VPN
time.sleep(1)
pyautogui.write('cd /etc/openvpn/client/grandbrasil/')
pyautogui.press('enter')
pyautogui.write('sudo openvpn grandbrasil.ovpn')
pyautogui.press('enter')
pyautogui.write('remart1ns')
pyautogui.press('enter')
time.sleep(3)

# # acessar area de trabalho
# pyautogui.hotkey('winleft', 'd')

# abrir terminal
pyautogui.hotkey('ctrl', 'alt', 't')
time.sleep(1)

# abrir arquivo excel
pyautogui.write('et /home/renan/Documentos/teste_rpa.xlsx&')
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)

#acessa linha 2 do arquivo
pyautogui.hotkey('ctrl', 'home')
pyautogui.press('down')
pyautogui.hotkey('ctrl', 'c')

# abrir TS 
pyautogui.moveTo(991, 0)
pyautogui.click()
pyautogui.moveTo(1041, 118)
pyautogui.moveTo(878, 488)
pyautogui.click()
time.sleep(5)


# abrir NBS
pyautogui.moveTo(90, 170)
pyautogui.doubleClick()
time.sleep(1)
pyautogui.write('nbs')
pyautogui.press('tab')
pyautogui.write('gr4nd2020')
pyautogui.press('tab')
pyautogui.write('nbsgrand')
pyautogui.press('enter')
time.sleep(2)

# abrir modulo clientes
pyautogui.click(1288, 146)
pyautogui.write('clientes')
pyautogui.press('enter')
time.sleep(5)

# Fecha msg lgpd
pyautogui.click(1053, 144)
#pyautogui.hotkey('alt', 'tab')
#pyautogui.hotkey('ctrl', 'c')
#pyautogui.hotkey('alt', 'tab')

#pyautogui.click(1972, 636)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('backspace')
pyautogui.press('backspace')
pyautogui.press('backspace')
pyautogui.press('enter')

time.sleep(0.5)

#Copia email
pyautogui.click(254, 119)
pyautogui.doubleClick(394, 590)
pyautogui.hotkey('ctrl', 'c')

#Alterna para o excel
pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.keyUp('alt')
pyautogui.press('tab')
pyautogui.hotkey('ctrl', 'v')

pyautogui.press('enter')
pyautogui.hotkey('ctrl', 's')

time.sleep(0.5)
pyautogui.hotkey('alt', 'F4')

# alternar para arquivo de consulta
# copiar dado para consulta
# alternar para modulo clientes
# colar dado para consulta e pesquisar
# copiar informacao do modulo clientes
# alternar para arquivo de consulta
# colar informação coletada
# salvar e fechar arquivo

# fi# m do processo
pyautogui.alert(text='Processamento concluido com sucesso', 
                title='Sucesso', 
                button='OK')