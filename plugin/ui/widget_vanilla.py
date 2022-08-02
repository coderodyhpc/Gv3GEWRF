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
    Pass
    
