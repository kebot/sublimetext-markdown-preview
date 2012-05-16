#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
This script use [appscript](http://appscript.sourceforge.net/py-appscript/) 
instead of `open` command to open url in MacOSX.When a user alread open the 
url, it will reload the browser instead of open 
a new one.
	Author: Keith Yao<i@yaofur.com>
"""


def reload_browser(url):
	# "Google Chrome \ Safari "
	browser_name = "Google Chrome"
	import appscript
	app = appscript.app(browser_name)
	current_window = app.windows[0]
	current_tab = current_window.active_tab

	if current_tab.URL.get() == url:
		current_tab.reload()
	else:
		tab = app.windows[0].make(
			new=appscript.k.tab,
			with_properties={appscript.k.URL: url}
			)
		tab.reload()

reload_browser('file:///var/folders/k4/6y1cn3bj2vvby9g15yw8nr6c0000gn/T/31.html')
# reload_browser('http://www.douban.com/')
