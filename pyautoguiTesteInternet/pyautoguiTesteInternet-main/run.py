import pyautogui

def go():
    pyautogui.PAUSE = 1.0
    pyautogui.hotkey('win', 'r')
    pyautogui.write('cmd')
    pyautogui.press('enter')
    pyautogui.write('pip install --upgrade speedtest-cli') # É preciso ter o python instalado para utilizar o speedtest-cli.
    pyautogui.press('enter')
    pyautogui.write('speedtest-cli')
    pyautogui.press('enter')
