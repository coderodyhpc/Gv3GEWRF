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
                        <h2>WRF Simulations</h2>
                        <br>
                    </html>
                """
        text = """
                    <html>
                        <br>
                        <p>Performing WRF simulations requires opening a project and following one of the following procedures:</p>
                        <ul>
                            <li>Full procedure that includes downloading the meteorological data, generating the domain(s), \
                            preprocessing the data (i.e. running geogrid, ungrib, and metgrid), \
                            generating the initial and boundary conditions files, and running WRF. </li>
                            <li>If the meteorological files are already available in the project subdirectory (in addition to \
                            the namelist.input file, you can directly click on the simulation tab and run real and wrf executables.
                            </li>
                            <li>If the iniital and boundary conditions files are located at the project subdirectory,
                             you can directly click on executing wrf from the simulation tab.
                            </li>
                        </ul> 
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
