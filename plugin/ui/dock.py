# Gv3GEWRF 
# Copyright (c) Odycloud.

from PyQt5.QtWidgets import QDockWidget, QTabWidget

from qgis.gui import QgisInterface

from Gv3GEWRF.plugin.ui.tab_home import HomeTab
from Gv3GEWRF.plugin.ui.tab_download import DownloadTab
from Gv3GEWRF.plugin.ui.tab_datasets import DatasetsTab
from Gv3GEWRF.plugin.ui.tab_simulation import SimulationTab
from Gv3GEWRF.plugin.ui.widget_view import ViewWidget
from Gv3GEWRF.plugin.ui.helpers import WhiteScroll

class MainDock(QDockWidget):
    """Set up the principle side dock"""
    def __init__(self, iface: QgisInterface, dock_widget: QDockWidget) -> None:
        super().__init__('GIS4WRF')

        tabs = QTabWidget()
        tabs.addTab(WhiteScroll(HomeTab()), 'Home')
        tabs.addTab(DatasetsTab(iface), "Download")
        self.download_tab = DownloadTab(iface)
        tabs.addTab(DatasetsTab(iface), "Datasets")
        self.simulation_tab = SimulationTab(iface)
        tabs.addTab(self.simulation_tab, "Simulation")
        self.view_tab = ViewWidget(iface, dock_widget)
        tabs.addTab(self.view_tab, "View")
        self.setWidget(tabs)
        self.tabs = tabs

###        self.simulation_tab.view_wrf_nc_file.connect(self.view_wrf_nc_file)

    def open_view_tab(self):
        self.tabs.setCurrentIndex(3)

    def view_wrf_nc_file(self, path: str) -> None:
        self.view_tab.add_dataset(path)
        self.open_view_tab()
