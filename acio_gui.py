## AC.IO GUI

#import dependencies
import wx as wx

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title="Academia to .io")
        panel = wx.Panel(self)

        repo_search = wx.FLP_CHANGE_DIR(panel)


        self.Show()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()

# Run this to generate the bundled app: pyinstaller --onefile --windowed myscript.p