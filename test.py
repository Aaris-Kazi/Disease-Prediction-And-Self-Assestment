import pyautogui as pg

# pg.doubleClick()
# pg.tripleClick()
# pg.hotkey('ctrl', 'c')
# pg.hotkey('ctrl', 'v')


# img_cv = cv2.imread(r'')

# # By default OpenCV stores images in BGR format and since pytesseract assumes RGB format,
# # we need to convert from BGR to RGB format/mode:
# img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
# cv2.imshow('Frame', img_rgb)
# cv2.waitKey(0)
# print(pytesseract.image_to_string(img_rgb))
# # OR
# img_rgb = Image.frombytes('RGB', img_cv.shape[:2], img_cv, 'raw', 'BGR', 0, 0)
# print(pytesseract.image_to_string(img_rgb))

import pyperclip as pc
import keyboard as kb
text1 = "it works"
  
# copying text to clipboard

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if kb.is_pressed(';'):  # if key 'q' is pressed ;it works b
            pg.press('backspace')
            pg.hotkey('ctrl', 'a')
            pg.hotkey('ctrl', 'c')
            print('You Pressed A Key!')
            pc.copy(text1)
            # pc.paste()
            
        elif kb.is_pressed('"'):
            pg.press('backspace')
            pg.hotkey('ctrl', 'v')
            
    except:
        break 
# pasting the text from clipboard;;it works;;;;;;;;it works'pg.hotkey('ctrl', 'v')'pg.hotkey('ctrl', 'v')pg.hotkey('ctrl', 'v')'pg.hotkey('ctrl', 'v')
# 'pg.hotkey('ctrl', 'v')'
# pg.hotkey('ctrl', 'v')