# Copyright (C) 2007, Red Hat, Inc.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

"""
Test the sugar3.graphics.icon.Icon widget.
"""

from gi.repository import Gtk

from sugar3.graphics.tray import HTray, VTray
from sugar3.graphics.tray import TrayButton, TrayIcon

import common

test = common.Test()

vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

tray = HTray()
vbox.pack_start(tray, False, False, 0)
tray.show()

theme_icons = Gtk.IconTheme.get_default().list_icons(context=None)

for i in range(0, 100):
    button = TrayButton(icon_name=theme_icons[i])
    tray.add_item(button)
    button.show()

tray = HTray()
vbox.pack_start(tray, False, False, 0)
tray.show()

for i in range(0, 10):
    icon = TrayIcon(icon_name=theme_icons[i])
    tray.add_item(icon)
    icon.show()

hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

tray = VTray()
hbox.pack_start(tray, False, False, 0)
tray.show()

for i in range(0, 100):
    button = TrayButton(icon_name=theme_icons[i])
    tray.add_item(button)
    button.show()

tray = VTray()
hbox.pack_start(tray, False, False, 0)
tray.show()

for i in range(0, 4):
    button = TrayButton(icon_name=theme_icons[i])
    tray.add_item(button)
    button.show()

vbox.pack_start(hbox, True, True, 0)
hbox.show()

test.pack_start(vbox, True, True, 0)
vbox.show()

test.show()

if __name__ == '__main__':
    common.main(test)
