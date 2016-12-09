# -*- coding: UTF-8 -*-

import addonHandler
import gui
import wx

addonHandler.initTranslation()

def onInstall():
	addon = [x for x in addonHandler.getAvailableAddons() if x.manifest["name"] == "TapinRadioStatusAnnouncer"]
	if len(addon) > 0:
		addon = addon[0]
		if gui.messageBox(
		# Translators: A message informing the user that he has installed an incompatible version.
		_("You have installed the TapinRadioStatusAnnouncer add-on, probably an old and incompatible version with this one. Do you want to uninstall the old version?"),
		# Translators: The title of the dialogbox.
		_("Uninstall incompatible add-on"),
		wx.YES|wx.NO|wx.ICON_WARNING)==wx.YES:
			addon.requestRemove()
