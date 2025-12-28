import sys
import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Adw
from window import MainWindow

class WhatPenguinApp(Adw.Application):
    def __init__(self):
        super().__init__(application_id='com.taha.whatpenguin',
                         flags=0)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = MainWindow(application=self)
        win.present()

if __name__ == '__main__':
    app = WhatPenguinApp()
    app.run(sys.argv)
