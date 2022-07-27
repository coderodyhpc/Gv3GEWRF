# Gv3GEWRF Plugin
# Copyright (c) 2022 Odycloud.

from PyQt5.QtWidgets import QTabWidget


from Gv3GEWRF.plugin.ui.helpers import WhiteScroll
from Gv3GEWRF.plugin.ui.widget_geo import GeoToolsDownloadManager
from Gv3GEWRF.plugin.ui.widget_met import MetToolsDownloadManager
from Gv3GEWRF.plugin.ui.widget_process import Process


class DatasetsTab(QTabWidget):
    def __init__(self, iface) -> None:
        super().__init__()

        geo = WhiteScroll(GeoToolsDownloadManager(iface))
        met = WhiteScroll(MetToolsDownloadManager(iface))
        process = WhiteScroll(Process(iface))

        self.addTab(geo, 'Geo')
        self.addTab(met, 'Met')
        self.addTab(process, 'Process')
