import pyautogui

# Open text file at specified coordinates
position = pyautogui.position()
print(position)
pyautogui.moveTo(1198, 330, duration=1)
pyautogui.click(clicks=2)
pyautogui.moveTo(1526, 148, duration=1)
# Press enter to go to new line in file
pyautogui.press('enter')
# Enter text
pyautogui.write('Python is good too!\n')
# Select text from file
pyautogui.hotkey('ctrl', 'a')
# Copy text from file
pyautogui.hotkey('ctrl', 'c')
pyautogui.press('down')
# Paste text from file
pyautogui.hotkey('ctrl', 'v')