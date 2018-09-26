# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.3 on Wed Sep 12 18:13:50 2018
# then modified by nice and beautiful developers
#

import os
import wx
import wx.grid

# Local:
import masso


WILDCARDS = \
    "GCode files (*.nc,*.gcode)|*.nc;*.gcode|" \
    "All files (*.*)|*.*"



class Frame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Frame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.currentDirectory = os.getcwd()
        self.notebook_1 = wx.Notebook(self, wx.ID_ANY)
        self.notebook_1_pane_1 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.ip_input = wx.TextCtrl(self.notebook_1_pane_1, wx.ID_ANY, "192.168.0.22", style=wx.TE_CENTRE)
        self.ip_input.SetMinSize((136, 30))
        self.connect_bt = wx.ToggleButton(self.notebook_1_pane_1, wx.ID_ANY, "CONNECT")
        self.select_file_bt = wx.Button(self.notebook_1_pane_1, wx.ID_ANY, "SELECT FILE")
        self.send_file_bt = wx.Button(self.notebook_1_pane_1, wx.ID_ANY, "SEND")
        self.notebook_1_notebook_status = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1_notebook_tools = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.tools_grid_name = wx.grid.Grid(self.notebook_1_notebook_tools, wx.ID_ANY, size=(1, 1))

        self.__set_properties()
        self.__do_layout()
        self.Bind(wx.EVT_TOGGLEBUTTON, self.connect, self.connect_bt)
        self.Bind(wx.EVT_BUTTON, self.onOpenFile, self.select_file_bt)
        self.Bind(wx.EVT_BUTTON, self.send, self.send_file_bt)
        # end wxGlade

        # Set the file path initially (empty path):
        self.setFilePath('', update_layout=False)

        # A workaround for the Linux "Awesome" window manager:
        self.Bind(wx.EVT_ACTIVATE, self.AwesomeWM_Workaround)


    def __set_properties(self):
        # begin wxGlade: Frame.__set_properties
        self.SetTitle("Masso Sender")
        self.select_file_bt.SetMinSize((120, 22))
        self.send_file_bt.SetMinSize((120, 22))
        self.tools_grid_name.CreateGrid(2, 2)
        self.tools_grid_name.EnableEditing(0)
        self.tools_grid_name.SetColLabelValue(0, "TOOL NO.")
        self.tools_grid_name.SetColSize(0, 201)
        self.tools_grid_name.SetColLabelValue(1, "TOOL NAME")
        self.tools_grid_name.SetColSize(1, 106)
        self.tools_grid_name.SetRowSize(0, 5)
        self.tools_grid_name.SetRowSize(1, 5)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Frame.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_1 = wx.BoxSizer(wx.VERTICAL)
        self.grid_sizer_2 = wx.GridSizer(7, 1, 0, 0)
        label_4 = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, "MASSO IP ADDRESS :", style=wx.ALIGN_CENTER)
        label_4.SetMinSize((136, 15))
        label_4.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.LIGHT, 0, "Futura Std"))
        self.grid_sizer_2.Add(label_4, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.grid_sizer_2.Add(self.ip_input, 0, wx.ALIGN_CENTER, 0)
        self.grid_sizer_2.Add(self.connect_bt, 0, wx.ALIGN_CENTER | wx.SHAPED, 0)
        static_line_1 = wx.StaticLine(self.notebook_1_pane_1, wx.ID_ANY)
        self.grid_sizer_2.Add(static_line_1, 0, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 0)
        self.grid_sizer_2.Add(self.select_file_bt, 0, wx.ALIGN_CENTER, 0)
        self.file_path = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, "", style=wx.ALIGN_CENTER)
        self.file_path.SetMinSize((136, 15))
        self.file_path.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.LIGHT, 0, "Futura Std"))
        self.grid_sizer_2.Add(self.file_path, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.SHAPED, 0)
        self.grid_sizer_2.Add(self.send_file_bt, 0, wx.ALIGN_CENTER, 0)
        self.notebook_1_pane_1.SetSizer(self.grid_sizer_2)
        label_3 = wx.StaticText(self.notebook_1_notebook_status, wx.ID_ANY, "MACHINE STATUS :", style=wx.ALIGN_CENTER)
        label_3.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.LIGHT, 0, "Futura Std"))
        grid_sizer_1.Add(label_3, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        status_input = wx.StaticText(self.notebook_1_notebook_status, wx.ID_ANY, "-", style=wx.ALIGN_CENTER)
        status_input.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.LIGHT, 0, "Futura Std"))
        grid_sizer_1.Add(status_input, 0, wx.EXPAND, 0)
        percent_input = wx.StaticText(self.notebook_1_notebook_status, wx.ID_ANY, "-", style=wx.ALIGN_CENTER)
        percent_input.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.LIGHT, 0, "Futura Std"))
        grid_sizer_1.Add(percent_input, 0, wx.EXPAND, 0)
        counter_input = wx.StaticText(self.notebook_1_notebook_status, wx.ID_ANY, "-", style=wx.ALIGN_CENTER)
        counter_input.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.LIGHT, 0, "Futura Std"))
        grid_sizer_1.Add(counter_input, 0, wx.EXPAND, 0)
        static_line_2 = wx.StaticLine(self.notebook_1_notebook_status, wx.ID_ANY)
        grid_sizer_1.Add(static_line_2, 0, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 0)
        serial_no_input = wx.StaticText(self.notebook_1_notebook_status, wx.ID_ANY, "Serial No : ", style=wx.ALIGN_CENTER)
        serial_no_input.SetMinSize((136, 15))
        serial_no_input.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.LIGHT, 0, "Futura Std"))
        grid_sizer_1.Add(serial_no_input, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        core_version_input = wx.StaticText(self.notebook_1_notebook_status, wx.ID_ANY, "Core Version :", style=wx.ALIGN_CENTER)
        core_version_input.SetMinSize((136, 15))
        core_version_input.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.LIGHT, 0, "Futura Std"))
        grid_sizer_1.Add(core_version_input, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        software_version_input = wx.StaticText(self.notebook_1_notebook_status, wx.ID_ANY, "Software Version :", style=wx.ALIGN_CENTER)
        software_version_input.SetMinSize((136, 15))
        software_version_input.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.LIGHT, 0, "Futura Std"))
        grid_sizer_1.Add(software_version_input, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.notebook_1_notebook_status.SetSizer(grid_sizer_1)
        sizer_4.Add(self.tools_grid_name, 0, wx.ALIGN_CENTER, 0)
        self.notebook_1_notebook_tools.SetSizer(sizer_4)
        self.notebook_1.AddPage(self.notebook_1_pane_1, "CONNECT")
        self.notebook_1.AddPage(self.notebook_1_notebook_status, "STATUS")
        self.notebook_1.AddPage(self.notebook_1_notebook_tools, "TOOLS")
        sizer_1.Add(self.notebook_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade


    def AwesomeWM_Workaround(self, event):
        """ A workaround for the Linux "Awesome" window manager.  """
        self.updateFileLabel()


    def setFilePath(self, file_path, update_layout=True):
        """ Set a new file path, and update the GUI accordingly. """
        self.inputFilePath = file_path
        self.updateFileLabel(update_layout)


    def updateFileLabel(self, update_layout=True):
        """ Update the `self.file_path` label, depending on the `self.inputFilePath` property.

        Args:
            update_layout: indicates if the layout has to be redrawn
        """
        basename = os.path.basename(self.inputFilePath)
        self.file_path.SetLabel('File: {}'.format(basename))
        if update_layout:
            self.grid_sizer_2.Layout()


    def connect(self, event):  # wxGlade: Frame.<event_handler>
        print("Event handler 'connect' not implemented!")
        event.Skip()


    def onOpenFile(self, event):
        """ Create and show the Open FileDialog """
        dlg = wx.FileDialog(
            self,
            message = "Choose a file",
            defaultDir = self.currentDirectory,
            defaultFile = "",
            wildcard = WILDCARDS,
            style = wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR
        )

        if dlg.ShowModal() == wx.ID_OK:
            self.setFilePath(dlg.GetPath())
            dlg.Destroy()

            print("You chose the following file(s):")
            print(self.inputFilePath)


    def send(self, event):
        #if not self.inputFilePath:
        #    print("Choisissez un fichier")
        #else:
        masso.sendFile(self.ip_input.GetValue().encode('utf-8'), self.inputFilePath)



class MassoSenderApp(wx.App):
    def OnInit(self):
        self.frame = Frame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

