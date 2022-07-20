# Gv3GEWRF 
# Copyright (c) Odycloud.

from PyQt5.QtCore import QObject, pyqtSignal

from Gv3GEWRF.core import Project

class BroadcastSignals(QObject):
    geo_datasets_updated = pyqtSignal()
    met_datasets_updated = pyqtSignal()
    options_updated = pyqtSignal()
    project_updated = pyqtSignal()
    open_project_from_object = pyqtSignal(Project)

Broadcast = BroadcastSignals()
