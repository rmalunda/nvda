# -*- coding: UTF-8 -*-
#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2018 NV Access Limited
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.


def scaleSize(scaleFactor, size):
	"""Helper method to scale a size using the logical DPI
	@param size: The size (x,y) as a tuple or a single numerical type to scale
	@returns: The scaled size, returned as the same type"""
	if isinstance(size, tuple):
		return (scaleFactor * size[0], scaleFactor * size[1])
	return scaleFactor * size

def getScaleFactor(windowHandle):
	"""Helper method to get the window scale factor. The window needs to be constructed first, in
	order to get the window handle, this likely means calling the wx.window __init__ method prior
	to calling self.GetHandle()"""
	import windowUtils
	return windowUtils.getWindowScalingFactor(windowHandle)
