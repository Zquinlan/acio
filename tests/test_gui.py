from acio_gui import*
from PyQt5 import QtCore


def test_gui(qtbot):
    widget = mainWindow()
    qtbot.addWidget(widget)
    assert widget.mkFramework.text() == "Acio Website"