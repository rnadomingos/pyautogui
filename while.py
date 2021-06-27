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

# abrir arquivo excel
pyautogui.write('et /home/renan/Documentos/teste_rpa.xlsx&')
pyautogui.press('enter')
time.sleep(1)

#acessa linha 2 do arquivo
pyautogui.hotkey('ctrl', 'home')
pyautogui.press('down')
time.sleep(1)

eof = 0

eof_teste = str('##EOF##')

while eof < 1:
        #copia do excel e armazena em var
        pyautogui.hotkey('ctrl', 'c')
        
        r = Tk()
        clipboard = str(r.selection_get (selection = "CLIPBOARD")).strip()
        r.destroy()
        
        print("clipboard:",len(clipboard))
        print("clipboard:",clipboard)
        print("eof_teste:",len(eof_teste))
        print("eof_teste:",eof_teste)

        pyautogui.press('tab')
        pyautogui.hotkey('ctrl','v')
        pyautogui.press('enter')      
        pyautogui.press('enter')

        pyautogui.sleep(1)

        if clipboard == eof_teste:
            print(eof)
            eof+=1

print("eof:", eof)
print("clipboard:", clipboard)

print('fim do while')