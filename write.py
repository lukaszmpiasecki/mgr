import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("Pierwsza linia", 1, 0)
mylcd.lcd_display_string("Druga linia", 2, 0)
