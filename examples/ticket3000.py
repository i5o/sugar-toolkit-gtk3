# Copyright (C) 2007, One Laptop Per Child
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
Spec in ticket #3000.
"""

from gi.repository import Gtk

from sugar3.graphics.toolbutton import ToolButton

import common

test = common.Test()

toolbar = Gtk.Toolbar()
test.pack_start(toolbar, False, False, 0)
toolbar.show()

button = ToolButton('go-previous')
toolbar.insert(button, -1)
button.show()

separator = Gtk.SeparatorToolItem()
toolbar.add(separator)
separator.show()

button = ToolButton('go-next')
toolbar.insert(button, -1)
button.show()


if __name__ == '__main__':
    common.main(test)
