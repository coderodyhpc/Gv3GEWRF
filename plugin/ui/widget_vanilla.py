# Gv3GEWRF 
# Copyright (c) Odycloud.

from typing import Optional, Tuple, List, Callable, Union, Iterable, Any
from io import StringIO
import os

from PyQt5.QtCore import (
    QMetaObject, Qt, QLocale, pyqtSlot, pyqtSignal, QModelIndex, QThread
)
from PyQt5.QtGui import (
    QDoubleValidator, QIntValidator, QPalette, QTextOption, QSyntaxHighlighter,
    QTextCharFormat, QColor, QFont
)
from PyQt5.QtWidgets import (
    QWidget, QTabWidget, QPushButton, QLayout, QVBoxLayout, QDialog, QGridLayout, QGroupBox, QSpinBox,
    QLabel, QHBoxLayout, QComboBox, QScrollArea, QFileDialog, QRadioButton, QLineEdit, QTableWidget,
    QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QHeaderView, QPlainTextEdit, QSizePolicy,
    QMessageBox, QSizePolicy
)

from qgis.gui import QgisInterface

from Gv3GEWRF.core import Project, get_namelist_schema, UserError, WRFDistributionError, WPSDistributionError

from Gv3GEWRF.plugin.constants import PLUGIN_NAME
from Gv3GEWRF.plugin.options import get_options
from Gv3GEWRF.plugin.ui.helpers import MessageBar
from Gv3GEWRF.plugin.ui.thread import ProgramThread
from Gv3GEWRF.plugin.ui.dialog_nml_editor import NmlEditorDialog

class VanillaWidget(QWidget):
    tab_active = pyqtSignal()
    view_wrf_nc_file = pyqtSignal(str)

    def __init__(self, iface: QgisInterface) -> None:
        super().__init__()
#        pass

        self.iface = iface
        self.options = get_options()
        self.msg_bar = MessageBar(iface)
#        self.wps_box, [open_namelist_wps, prepare_only_wps, run_geogrid, run_ungrib, run_metgrid, open_output_wps] = \
#            self.create_gbox_with_btns('WPS', [
#                'Open Configuration',
#                'Prepare only',
#                ['Run Geogrid', 'Run Ungrib', 'Run Metgrid'],
#                'Visualize Output'
#            ])

        self.wps_box, [run_geogrid, run_ungrib, run_metgrid, open_output_wps] = \
            self.create_gbox_with_btns('WPS Preprocessor', [
                'Run Geogrid', 
                'Run Ungrib', 
                'Run Metgrid',
                'Visualize Output'
            ])

        
        vbox = QVBoxLayout()
        vbox.addWidget(self.wps_box)        

        self.setLayout(vbox)
 
        open_namelist_wps.clicked.connect(self.on_open_namelist_wps_clicked)
#        prepare_only_wps.clicked.connect(self.on_prepare_only_wps_clicked)
#        run_geogrid.clicked.connect(self.on_run_geogrid_clicked)
#        run_ungrib.clicked.connect(self.on_run_ungrib_clicked)
#        run_metgrid.clicked.connect(self.on_run_metgrid_clicked)
#        open_output_wps.clicked.connect(self.on_open_output_wps_clicked)

    def create_gbox_with_btns(self, gbox_name: str, btn_names: List[Union[str,List[str]]]) \
            -> Tuple[QGroupBox, List[QPushButton]]:
        vbox = QVBoxLayout()
        btns = []
        for name_or_list in btn_names:
            if isinstance(name_or_list, str):
                name = name_or_list
                btn = QPushButton(name)
                btns.append(btn)
                vbox.addWidget(btn)
            else:
                hbox = QHBoxLayout()
                for name in name_or_list:
                    btn = QPushButton(name)
                    btns.append(btn)
                    hbox.addWidget(btn)
                vbox.addLayout(hbox)
        gbox = QGroupBox(gbox_name)
        gbox.setLayout(vbox)
        return gbox, btns        

    def on_open_namelist_wps_clicked(self) -> None:
        self.project.update_wps_namelist()
        self.open_editor_dialog(self.project.wps_namelist_path,
                                get_namelist_schema('wps'))
        