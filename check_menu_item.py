#!/usr/bin/python
#_*_ coding: utf-8 _*_

# Check Menu.py


import wx

class Example(wx.Frame):
    def __init__(self,*args,**kwargs):
        super(Example,self).__init__(*args,**kwargs)
        
        self.InitIU()
        
    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        viewMenu = wx.Menu()
        
        self.shst = viewMenu.Append(wx.ID_ANY,'Show statubar','Show Statusbar',kind=wx.ITEM_CHECK)
        self.shtl = viewMenu.Append(wx.ID_ANY,'Show toolbar','Show Toolbar',kind=wx.ITEM_CHECK)
        
        viewMenu.Check(self.shst.GetId(),True)
        viewMenu.Check(self.shtl.GetId(),True)
        
        self.Bind(wx.EVT_MENU,self.TogglestaTusBar,self.shst)
        self.Bind(wx.EVT_MENU,self.ToggleToolBar,self.shtl)
        
        menubar.Append(fileMenu,'&File')
        menubar.Append(viewMenu,'&View')
        self.SetMenuBar(menubar)
        
        self.toolbar = self.CreateToolBar() 
        self.toolbar.AddLabelTool(1,'',wx.Bitmap('texit.png'))
        self.toolbar.Realize()
        
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('Ready')
        
        self.SetSize((500,350))
        self.SetTitle('Check Menu Item')
        self.Centre()
        self.Show(True)
        
    def ToggleStatusBar(self,e):
        
        if self.shst.IsChecked():
            self.statusbar.Show()
        else:
            self.statusbar.Hide()
            
    def ToggleToolBar(self,e):
        
        if self.shtl.IsChecked():
            self.toolbar.Show()
        else:
            self.toolbar.Hide()
            
def main():
    ex = wx.App()
    Example(None)
    ex.MainLoop()
    
if __name__ == '__main__':
    main()                                    
           