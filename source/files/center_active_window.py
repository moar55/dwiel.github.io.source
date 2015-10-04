#!/usr/bin/python

import popen2
import re

(f, _) = popen2.popen2('wmctrl -d')
desktop_str = f.readline()
desktop_size = re.search('WA: \d,\d (\d+)x(\d+)', desktop_str)
desktop_width = int(desktop_size.group(1))
desktop_height = int(desktop_size.group(2))

(f, _) = popen2.popen2('wmctrl -r :ACTIVE: -L -G')
window_str = f.readline()
window_size = re.search(' +\d+ *\d+ *\d+ *(\d+) *(\d+)', window_str)
window_width = int(window_size.group(1))
window_height = int(window_size.group(2))

new_window_position_x = (desktop_width - window_width) / 2
new_window_position_y = (desktop_height - window_height) / 2

popen2.popen2('wmctrl -r :ACTIVE: -e 0,%d,%d,-1,-1' % (new_window_position_x, new_window_position_y))
