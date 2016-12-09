# coding :utf-8
# tapin_status.py
# Autor Jiri Holzinger
# Program pro oznamovani stavu tapinradia a otevreni okna
# Zkratka nvda +shift +t

import addonHandler
addonHandler.initTranslation()
import globalPluginHandler,IAccessibleHandler
import scriptHandler
from ui import message
import ctypes
import NVDAObjects
from api import getFocusObject, copyToClip
import winUser


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def script_tapinradio(self, gesture):
		WM_COMMAND=0x111
		WM_SYSCOMMAND=0x112
		CMD_RESTORE_MAIN_WINDOW=0xF030
		CMD_SET_STATUS_TEXT=2
		l1="tapinradio_status_wnd"
		l2="Qt5QWindowIcon"
		h,FindWindowExA =0,ctypes.windll.user32.FindWindowExA
		h=FindWindowExA(h,0,l1,0)
		h2=getFocusObject().windowHandle
		h2=FindWindowExA(0,0,l2,0)
		isSameScript =scriptHandler.getLastScriptRepeatCount()
		if isSameScript == 0: 
			winUser.sendMessage(h,WM_COMMAND,CMD_SET_STATUS_TEXT,0)
			name=winUser.getWindowText(h)
			copyToClip(name)
			message(name)
		elif isSameScript==1: 
			try:
				winUser.sendMessage(h2,WM_SYSCOMMAND,CMD_RESTORE_MAIN_WINDOW,0)
				message (_("Maximized window"))
			except:
				pass
	# Documentation
	script_tapinradio.__doc__ = _("Tapinradio status announcer")

	__gestures={
		"kb:NVDA+shift+t": "tapinradio",
	}

