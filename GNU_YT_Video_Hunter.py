#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
from subprocess import call


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs) 
        self.InitUI()
        self.CreateStatusBar()
        

    def InitUI(self):
		
        menubar = wx.MenuBar()#iniciando barra de menu

        #menu ayuda
        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_HELP, '&Ayuda', 'Ingrese una url del video que desesa descargar y seleccione una opcion')
        menubar.Append(fileMenu, '&Ayuda')
        self.SetMenuBar(menubar)
        fileMenu.AppendSeparator()
        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+Q')
        fileMenu.AppendItem(qmi)
        
        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)
        
        
        #menu acerca de
        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_ABOUT, '&Acerca de','Desarrolladores: Ricardo Garcia Gonzalez, Danny Colligan y 190+ || Interfaz grafica: Alexander Carṕintero -Estudiante Ingenieria en Sistemas')
        menubar.Append(fileMenu, '&Acerca de')
        self.SetMenuBar(menubar)
        
        #Menu Actualizar
        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_REFRESH, '&Actualizar')
        menubar.Append(fileMenu, '&Actualizar')
        self.SetMenuBar(menubar)
        
        #controles
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(4, 4)
        
        text = wx.StaticText(panel, label="Ingrese url")#StaticText
        sizer.Add(text, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        
        self.tc = wx.TextCtrl(panel)#TextCtrl
        sizer.Add(self.tc, pos=(1, 0), span=(1, 5), flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=50)
        
        #creando checkbox
        self.check1 = wx.CheckBox(panel, -1, "MP4 [720 x 1280]",(320,180))
        self.check2 = wx.CheckBox(panel, -1, "MP4 [320 x 640]",(320,220))
        self.check3 = wx.CheckBox(panel, -1, "WEBM [720 x 1280]",(320,260))
        self.check4 = wx.CheckBox(panel, -1, "M4a [audio format]",(320,300))
        
        buttonDL = wx.Button(panel, label="Descargar", size=(90, 28))
       
		#Agregando al sizer
        sizer.Add(buttonDL, pos=(3, 3))
        sizer.AddGrowableCol(1)
        sizer.AddGrowableRow(2)
        panel.SetSizerAndFit(sizer)
        
        #eventos
        self.Bind(wx.EVT_BUTTON, self.onClick)
        self.Bind(wx.EVT_CHECKBOX, self .EvtCB_MP41, self.check1)
        self.Bind(wx.EVT_CHECKBOX, self .EvtCB_MP42, self.check2)
        self.Bind(wx.EVT_CHECKBOX, self .EvtCB_WEBM, self.check3)
        self.Bind(wx.EVT_CHECKBOX, self .EvtCB_M4a, self.check4)
        
        self.SetSize((800, 600))
        self.SetTitle('GNU/YT- Video Hunter')
        self.Centre()
        self.Show(True)
    
    def onClick(self,event):
        edit_text = self.tc.GetValue()
        comm = "youtube-dl "+edit_text
        call(comm.split(), shell = False)
    
    def EvtCB_MP41(self,event):
        edit_text = self.tc.GetValue()
        comm = "youtube-dl -f 22 "+edit_text
        call(comm.split(), shell = False)
   
    def EvtCB_MP42(self,event):
        edit_text = self.tc.GetValue()
        comm = "youtube-dl -f 18 "+edit_text
        call(comm.split(), shell = False)
    
    def EvtCB_WEBM(self,event):
        edit_text = self.tc.GetValue()
        comm = "youtube-dl -f 45 "+edit_text
        call(comm.split(), shell = False)
    
    def EvtCB_M4a(self,event):
        edit_text = self.tc.GetValue()
        comm = "youtube-dl -x --audio-format mp3 "+edit_text
        call(comm.split(), shell = False)
        
    def OnQuit(self, e):
        self.Close()

def main():

    ex = wx.App()
    Example(None)
    ex.MainLoop()    

if __name__ == '__main__':
    main()

