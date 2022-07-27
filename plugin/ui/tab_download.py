# Gv3GEWRF Plugin
# Copyright (c) 2022 Odycloud.

from PyQt5.QtWidgets import QTabWidget


from Gv3GEWRF.plugin.ui.helpers import WhiteScroll
from Gv3GEWRF.plugin.ui.widget_process import Process


class DownloadTab(QTabWidget):
    def __init__(self, iface) -> None:
        super().__init__('Accelerated download of meteorological data')

        gfs = WhiteScroll(Process(iface))
        nam = WhiteScroll(Process(iface))
        other = WhiteScroll(Process(iface))

        self.addTab(gfs, 'GFS')
        self.addTab(nam, 'NAM')
        self.addTab(other, 'Other')
