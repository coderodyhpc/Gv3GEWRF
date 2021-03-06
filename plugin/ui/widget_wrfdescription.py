# Gv3GEWRF 
# Copyright (c) Odycloud.

from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (
    QWidget, QTabWidget, QPushButton, QLayout, QVBoxLayout, QDialog, QGridLayout, QGroupBox, QSpinBox,
    QLabel, QHBoxLayout, QComboBox, QScrollArea, QFileDialog, QRadioButton, QLineEdit, QTableWidget,
    QTableWidgetItem, QTreeWidget, QTreeWidgetItem
)
from PyQt5.QtGui import QPixmap,QFont

#from PyQt5.QtCore import *
#from PyQt5.QtWidgets import *
#from PyQt5.QtGui import *

from Gv3GEWRF.core import Project
from Gv3GEWRF.plugin.options import get_options
###from Gv3GEWRF.plugin.constants import Gv3GEWRF_LOGO_PATH

class WRFDescriptionWidget(QWidget):
    create_project = pyqtSignal(str)
    open_project = pyqtSignal(str)
    close_project = pyqtSignal()
    tab_active = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()

        self.options = get_options()

        btn_new = QPushButton("Create Project",
            clicked=self.on_create_project_button_clicked)
        btn_new.setFont(QFont('Exo 2'))

        btn_existing = QPushButton("Open Project",
            clicked=self.on_open_project_button_clicked)

        self.current_project_label = QLabel()

        vbox = QVBoxLayout()
        title = """
                    <html>
                        <h2>Graphic Environment on Graviton3 for WRF</h2>
                        <h3>WRF Simulations</h3>
                        <br>
                    </html>
                """
        text = """
                    <html>
                        <br>
                        <p>These are the different options to run WRF.</p>
                        <ul>
                        <li>Build the input file from the preprocessor tab</li>
                        <li>If the meteorological data is already available, you can run real and wrf. </li>
                        <li>If the boundary and initial files are already available, you can run wrf</li>
                        </ul> 
                  </html>
               """
        text2 = """
                    <html>
                        <br>
                        <p>These are the different options to run WRF 2.</p>
                        <ul>
                        <li>Build the input file from the preprocessor tab</li>
                        <li>If the meteorological data is already available, you can run real and wrf. </li>
                        <li>If the boundary and initial files are already available, you can run wrf</li>
                        </ul> 
                  </html>
               """

        label_title = QLabel(title)
        label_text = QLabel(text)
        label_text2 = QLabel(text2)
        label_title.setFont(QFont('Exo'))
        label_text.setFont(QFont('Exo 2'))
        label_text2.setFont(QFont('Exo-2'))
        label_text.setWordWrap(True)
        label_text.setOpenExternalLinks(True)
        label_text2.setWordWrap(True)
        label_text2.setOpenExternalLinks(True)
#        label_pixmap = QLabel()
#        pixmap = QPixmap('/home/ubuntu/.local/share/QGIS/QGIS3/profiles/default/python/plugins/Gv3GEWRF/plugin/resources/icon512.png')
#        label_pixmap.setPixmap(pixmap)
#        label_pixmap.setAlignment(Qt.AlignCenter)
        vbox.addWidget(label_title)
#        vbox.addWidget(label_pixmap)
        vbox.addWidget(label_text)
        vbox.addWidget(label_text2)
        vbox.addStretch()

        vbox.addWidget(btn_new)
        vbox.addWidget(btn_existing)
        vbox.addWidget(self.current_project_label)
        self.setLayout(vbox)

    @property
    def project(self) -> Project:
        return self._project

    @project.setter
    def project(self, val: Project) -> None:
        ''' Sets the currently active project. See tab_simulation. '''
        self._project = val
        self.update_project_path_label()

    def on_create_project_button_clicked(self):
        folder = QFileDialog.getExistingDirectory(
            caption='Select new project folder', directory=self.options.projects_dir)
        if not folder:
            return
        self.create_project.emit(folder)

    def on_open_project_button_clicked(self):
        folder = QFileDialog.getExistingDirectory(
            caption='Select existing project folder', directory=self.options.projects_dir)
        if not folder:
            return
        self.open_project.emit(folder)

    def update_project_path_label(self) -> None:
        path = self.project.path
        if path is None:
            path = 'N/A'
        self.current_project_label.setText('Project path: ' + path)
