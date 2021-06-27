import pyautogui
import time
#tecla windows 
#pyautogui.press('winleft')
pyautogui.alert(text='Atenção, não mexa no pc agora, o mestre vai trabalhar', title='Atenção', button='OK')
#pyautogui.PAUSE = 0.5
time.sleep(1)
#control+alt+t
pyautogui.hotkey('ctrl','alt','t')
time.sleep(1)
#Mostra o trenzinho
#pyautogui.write('sl')
#pyautogui.press('enter')
a = pyautogui.password(text='teste', title='testeS', default='', mask='*')
print("Esta é a senha: "+ a)
time.sleep(3)
pyautogui.write(a)
pyautogui.alert(text='Olhaaa, se passou o trem na sua frente, dê OK', title='Trenzinho', button='OK')
time.sleep(1)
pyautogui.write('exit')
pyautogui.press('enter')


