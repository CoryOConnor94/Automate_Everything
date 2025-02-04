import pyautogui
import pyperclip

# Open text file at specified coordinates
position = pyautogui.position()
print(position)
pyautogui.moveTo(1198, 330, duration=1)
pyautogui.click(clicks=2)
pyautogui.moveTo(1526, 148, duration=1)

# Select text from file
pyautogui.hotkey('ctrl', 'a')
# Copy text from file
pyautogui.hotkey('ctrl', 'c')

text = pyperclip.paste()
print(text)