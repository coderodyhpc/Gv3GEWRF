# Gv3GEWRF Plugin
# Copyright (c) 2022 Odycloud.

from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtCore import pyqtSignal

from qgis.gui import QgisInterface

from Gv3GEWRF.plugin.ui.helpers import WhiteScroll
from Gv3GEWRF.plugin.ui.widget_process import Process


class DownloadTab(QTabWidget):
    def __init__(self, iface) -> None:
        super().__init__()

        self.general_tab = GeneralWidget()
        gfs = WhiteScroll(self.general_tab)
#        nam = WhiteScroll(self.domain_tab)
#        other = WhiteScroll(self.run_tab)

        self.addTab(gfs, 'GFS')
#        self.addTab(nam, 'NAM')
#        self.addTab(other, 'Other')
        
#        self.addTab(WhiteScroll(self.general_tab), 'General')
#        self.addTab(WhiteScroll(self.domain_tab), 'Domain')
#        self.addTab(WhiteScroll(self.datasets_tab), 'Data')
#        self.addTab(WhiteScroll(self.run_tab), 'Run')

#        self.tabs = [self.general_tab, self.domain_tab, self.datasets_tab, self.run_tab]
