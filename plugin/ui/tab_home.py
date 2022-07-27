# Gv3GEWRF 
# Copyright (c) Odycloud.

from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap

######from Gv3GEWRF.plugin.constants import Gv3GEWRF_LOGO_PATH

class HomeTab(QWidget):
    """Class for creating the Home tab"""
    def __init__(self) -> None:
        super().__init__()
        vbox = QVBoxLayout()
        title = """
                    <html>
                        <h1>Gv3GEWRF</h1>
                        <br>
                    </html>
                """
        text = """
                    <html>
                        <br>
                        <p>What do I want to write?</p>
                  </html>
               """

        label_title = QLabel(title)
        label_text = QLabel(text)
        label_text.setWordWrap(True)
        label_text.setOpenExternalLinks(True)
        label_pixmap = QLabel()
        pixmap = QPixmap('/home/ubuntu/.local/share/QGIS/QGIS3/profiles/default/python/plugins/Gv3GEWRF/plugin/resources/QGIS_logo64.png')
        label_pixmap.setPixmap(pixmap)
        label_pixmap.setAlignment(Qt.AlignCenter)
        vbox.addWidget(label_title)
        vbox.addWidget(label_pixmap)
        vbox.addWidget(label_text)
        vbox.addStretch()
        self.setLayout(vbox)
