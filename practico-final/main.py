import time
import curses
from curses.textpad import Textbox, rectangle

def main(stdscr):
    curses.curs_set(0)

    h, w = stdscr.getmaxyx()

    saludo = "Bienvenido al sistemai"
    saludo2 = "Presione una tecla para continuar"
    x = w // 2 - len(saludo) // 2
    y = h // 2

    stdscr.addstr(y-1, x, saludo)
    stdscr.addstr(y, x, saludo2)
    
    stdscr.refresh()

    time.sleep(2)

curses.wrapper(main)
