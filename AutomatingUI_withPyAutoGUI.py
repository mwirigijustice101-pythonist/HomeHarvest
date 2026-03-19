#PyAutoGUI>allows one to automate on-screen mouse and keyboard actions.Its especially useful when Selenium cannot interact with certain elements like native pop-ups,custom menus or non-HTML components
import pyautogui

# move the mouse to a position on the screen
pyautogui.moveTo(519, 1060, duration=1)
pyautogui.click()

#move to another position and click again
pyautogui.moveTo(1717, 352, duration=1)
pyautogui.click()
