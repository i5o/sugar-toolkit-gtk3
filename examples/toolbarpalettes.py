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
Test palette positioning for toolbar and tray.
"""

from gi.repository import Gtk

from sugar3.graphics.tray import HTray, TrayButton
from sugar3.graphics.toolbutton import ToolButton

import common

test = common.Test()

box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

theme_icons = Gtk.IconTheme.get_default().list_icons()

toolbar = Gtk.Toolbar()
box.pack_start(toolbar, False, False, 0)
toolbar.show()

for i in range(0, 5):
    button = ToolButton(icon_name=theme_icons[i])
    button.set_tooltip('Icon %d' % i)
    toolbar.insert(button, -1)
    button.show()

content = Gtk.Label()
box.pack_start(content, True, True, 0)
content.show()

tray = HTray()
box.pack_start(tray, False, False, 0)
tray.show()

for i in range(0, 30):
    button = TrayButton(icon_name=theme_icons[i])
    button.set_tooltip('Icon %d' % i)
    tray.add_item(button)
    button.show()

test.pack_start(box, True, True, 0)
box.show()

test.show()

if __name__ == '__main__':
    common.main(test)
