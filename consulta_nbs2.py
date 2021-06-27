## Acesso ao NBS e Consulta ao Sistema

import pyautogui
import time
from tkinter import Tk



# START
pyautogui.alert(text='Atenção, não mexa em nada agora, o robo vai iniciar o processo', 
                title='START ROBOT', 
                button='OK')
pyautogui.PAUSE = 0.5
# acessar area de trabalho

# ajusta para teclado do NOTE 
pyautogui.moveTo(1162, 0)
pyautogui.click()
pyautogui.moveTo(1162, 50) 
pyautogui.click()
time.sleep(3)

# acessar area de trabalho
pyautogui.hotkey('winleft', 'd')

# abrir terminal
pyautogui.hotkey('ctrl', 'alt', 't')
time.sleep(1)

# acessar VPN
pyautogui.write('cd /etc/openvpn/client/grandbrasil/')
pyautogui.press('enter')
pyautogui.write('sudo openvpn grandbrasil.ovpn')
pyautogui.press('enter')
pyautogui.write('remart1ns')
pyautogui.press('enter')
time.sleep(3)


# abrir terminal
pyautogui.hotkey('ctrl', 'alt', 't')
time.sleep(1)

# abrir arquivo excel
pyautogui.write('et /home/renan/Documentos/teste_rpa.xlsx&')
pyautogui.press('enter')
time.sleep(1)

#acessa linha 2 do arquivo
pyautogui.hotkey('ctrl', 'home')
pyautogui.press('down')
time.sleep(1)

# abrir TS 
pyautogui.moveTo(1100, 0)
pyautogui.click()
pyautogui.moveTo(1190, 98)
pyautogui.moveTo(1020, 430)
pyautogui.click()
time.sleep(5)

# abrir NBS
pyautogui.moveTo(90, 170)
pyautogui.doubleClick()
time.sleep(2)
pyautogui.write('nbs')
pyautogui.press('tab')
pyautogui.write('gr4nd2020')
pyautogui.press('tab')
pyautogui.write('nbsgrand')
pyautogui.press('enter')
time.sleep(3)

# abrir modulo clientes
pyautogui.click(1288, 146)
pyautogui.write('clientes')
pyautogui.press('enter')
time.sleep(5)

# Fecha msg lgpd
pyautogui.click(1053, 144)

#Alterna entre telas
pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.keyUp('alt')

# # Iinicializa loop
eof = 0
eof_teste = str('##EOF##')

while eof < 1:

    #copia do excel e armazena em var
    pyautogui.hotkey('ctrl', 'c')
    r = Tk()
    clipboard = str(r.selection_get (selection = "CLIPBOARD")).strip()
    r.destroy()
        
    #Alterna entre telas
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')
    pyautogui.press('tab')

    #Clica no campo para Digitar Busca
    pyautogui.click(1972, 636)
    pyautogui.write(clipboard)
    pyautogui.press('enter')

    time.sleep(0.5)
    
    #Copia email
    pyautogui.click(254, 119)
    pyautogui.doubleClick(394, 590)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(195,154)
    pyautogui.click(544,608)
    pyautogui.click(544,593)

    #Alterna para o excel
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

    #Copia próximo da lista
    pyautogui.hotkey('ctrl', 'c')
    c = Tk()
    clipboard = str(c.selection_get (selection = "CLIPBOARD")).strip()
    c.destroy()
    
    if clipboard == eof_teste:
        print(eof)
        eof+=1

    

# #Salva o arquivo
#pyautogui.hotkey('ctrl', 's')

# time.sleep(0.5)
#pyautogui.hotkey('alt', 'F4')

# retorna para area de trabalho
pyautogui.hotkey('winleft', 'd')

# fim do processo
pyautogui.alert(text='Processamento concluido com sucesso', 
                title='Sucesso', 
                button='OK')