import curses

def window(stdscr):

  print the window message.
  stdscr.addstr("hello curses!")
  
  stdscr.getch()

curses.wrapper (window)