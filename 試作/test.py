"""テストです"""

import wx
app = wx.App()
frame = wx.Frame(None, -1, 'Hello,World!',size=(500,500))
frame.Show()
app.MainLoop()
