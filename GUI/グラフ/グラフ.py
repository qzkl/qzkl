# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class グラフ
###########################################################################

class グラフ ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,498 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_button15 = wx.Button( self, wx.ID_ANY, u"グラフ作成", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button15, 0, wx.ALL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_textCtrl1, 0, wx.ALL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button15.Bind( wx.EVT_BUTTON, self.render )
		self.m_textCtrl1.Bind( wx.EVT_TEXT, self.deg )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def render( self, event ):
		event.Skip()

	def deg( self, event ):
		event.Skip()


