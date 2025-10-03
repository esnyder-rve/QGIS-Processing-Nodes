from typing import List, Dict, Self, Tuple

from PyQt5.QtWidgets import QMenu, QTreeWidget, QTreeWidgetItem
from PyQt5.QtCore import Qt

from Singleton import Singleton

from QpnAlgDbContext import QpnDbContext
from QpnAlgorithm import QpnAlgorithm
from TempQgisAlgsRegistry import TEMP_QgsAlgsRegistry
# from QpnAlgorithm import QpnAlgorithm
from QpnAlgorithmWrapper import QpnAlgorithmWrapper


class QpnAlgorithmsDB(metaclass=Singleton):
    # [Context] = {Provider:
    #               {Group:
    #                 {id: (name, description)}}}
    _algDbTree : List[Dict[str, Dict[str, Tuple[str, str]]]] = []

    # [id] = QpnAlgorithmWrapper
    _algDbList : Dict[str, QpnAlgorithmWrapper] = {}

    # List of algorithms that either don't make sense in a processing model context, or
    # algorithms that need a custom QPN wrapper.
    _blacklist_algs : List[str] = [
            'native:aggregate',   # FIXME: aggregates input param
            'native:httprequest', # FIXME: authcfg input param
            'native:reprojectlayer', # FIXME: coordinateoperation input param
            'pdal:reproject', # FIXME: coordinateoperation input param
            'gdal:importvectorintopostgisdatabaseavailableconnections', # FIXME: databaseschema input param, databasetable input param, providerconnection input param
            'native:importintopostgis', # FIXME: databaseschema input param, databasetable input param, providerconnection input param
            'native:postgisexecutesql', # FIXME: providerconnection input param
            'native:spatialiteexecutesqlregistered', # FIXME: providerconnection input param
            'qgis:postgisexecuteandloadsql', # FIXME: providerconnection input param
            'native:dxfexport', # FIXME: dxflayers input param, maptheme input param
            'native:refactorfields', # FIXME: fields_mapping input param
            'qgis:idwinterpolation', # FIXME: idw_interpolation_data input param
            'qgis:tininterpolation', # FIXME: idw_interpolation_data input param
            'native:atlaslayouttoimage', # FIXME: layout input param
            'native:atlaslayouttomultiplepdf', # FIXME: layout input param
            'native:atlaslayouttopdf', # FIXME: layout input param
            'native:printlayoutmapextenttolayer', # FIXME: layout input param, layoutitem input param
            'native:printlayouttoimage', # FIXME: layout input param
            'native:printlayouttopdf', # FIXME: layout input param
            'native:extractlabels', # FIXME: maptheme input param
            'native:rasterize', # FIXME: maptheme input param
            'native:exportmeshedges', # FIXME: meshdatasetgroups input param, meshdatasettime input param
            'native:exportmeshfaces', # FIXME: meshdatasetgroups input param, meshdatasettime input param
            'native:exportmeshongrid', # FIXME: meshdatasetgroups input param, meshdatasettime input param
            'native:exportmeshvertices', # FIXME: meshdatasetgroups input param, meshdatasettime input param
            'native:meshcontours', # FIXME: meshdatasetgroups input param, meshdatasettime input param
            'native:meshexportcrosssection', # FIXME: meshdatasetgroups input param, meshdatasettime input param
            'native:meshexporttimeseries', # FIXME: meshdatasetgroups input param, meshdatasettime input param
            'native:meshrasterize', # FIXME: meshdatasetgroups input param, meshdatasettime input param
            'qgis:rastercalculator', # FIXME: raster_calc_expression input param, cannot find this alg in GUI
            'qgis:relief', # FIXME: relief_colors input param
            'native:tinmeshcreation', # FIXME: tininputlayers input param
            # QGIS Modeler Exclusive
            # These will either be re-implemented by QPN, or aren't necessary
            'native:calculateexpression',
            'native:condition',
            'native:createdirectory',
            'native:filter',
            'native:filterlayersbytype',
            'native:loadlayer',
            'native:raiseexception',
            'native:raisemessage',
            'native:raisewarning',
            'native:renamelayer',
            'native:savelog',
            'native:setprojectvariable',
            'native:stringconcatenation',
            # QPN wrappers:
            # 'native:rasterlayerstatistics' # Implemented by qpn:rasterlayerstatistics
            ]

    def __init__(self):
        self.refreshDB()


    def instance(self) -> Self:
        """Get the instance of the algorithms db"""
        return self


    def refreshDB(self):
        """Refresh the algorithm db from the various sources"""
        self._algDbTree.clear()
        for context in QpnDbContext:
            currentContextDB = {}
            for alg in self.getAlgsList(context):
                # Skip over algs in the blacklist
                # These either need custom wrappers or aren't suited for models
                if alg.algId in self._blacklist_algs:
                    continue

                # Add it to the single, giant list of algs
                self._algDbList[alg.algId] = alg

                # Go through, and add it to the tree
                currentProvider = 'QGIS' if alg.provider in ['QGIS (3D)', 'QGIS (native c++)', 'QGIS (PDAL)', 'QGIS'] else alg.provider
                if currentProvider in currentContextDB:
                    if alg.group in currentContextDB[currentProvider]:
                        currentContextDB[currentProvider][alg.group][alg.algId] = (alg.name, alg.description)
                    else:
                        currentContextDB[currentProvider][alg.group] = {alg.algId: (alg.name, alg.description)}
                else:
                    currentContextDB[currentProvider] = {alg.group: {alg.algId: (alg.name, alg.description)}}
            self._algDbTree.append(currentContextDB)


    def getAlgsList(self, context: QpnDbContext = QpnDbContext.BASE) -> List[QpnAlgorithmWrapper]:
        """Get the list of algorithms available to the desired context"""
        algsList : List[QpnAlgorithmWrapper] = []
        if context == QpnDbContext.BASE:
            # Load algs from QGIS
            # algsList.append(QgsApplication().processingRegistry().algorithms())
            algsList += [QpnAlgorithmWrapper(x) for x in TEMP_QgsAlgsRegistry().instance().algorithms()]

            from algs.QpnAlgRegistry import QpnAlgRegistry
            algsList += [QpnAlgorithmWrapper(x) for x in QpnAlgRegistry().instance().algorithms()]

            from algs.PdalAlgsRegistry import PdalAlgRegistry
            algsList += [QpnAlgorithmWrapper(x) for x in PdalAlgRegistry().instance().algorithms()]

        elif context == QpnDbContext.PDAL_PIPELINE:
            pass

        return algsList


    def getAlgorithm(self, algID: str) -> QpnAlgorithmWrapper:
        """Get an algorithm by its QGIS ID (i.e. 'native:buffer')"""
        return self._algDbList[algID]


    def getAlgorithmToolbox(self, context: QpnDbContext = QpnDbContext.BASE) -> QTreeWidget:
        """Get the desired algorithm context tools as a QTreeWidget"""
        toolbox = QTreeWidget()
        toolbox.setColumnCount(2)
        toolbox.setColumnHidden(1, True)
        toolbox.setHeaderHidden(True)

        for provider in self._algDbTree[context.value]:
            currentProvider = QTreeWidgetItem(toolbox)
            currentProvider.setText(0, provider)

            for group in self._algDbTree[context.value][provider]:
                currentGroup = QTreeWidgetItem(currentProvider)
                currentGroup.setText(0, group)

                for algorithm in self._algDbTree[context.value][provider][group]:
                    currentAlg = QTreeWidgetItem(currentGroup)
                    currentAlg.setText(0, self._algDbTree[context.value][provider][group][algorithm][0])
                    currentAlg.setText(1, algorithm)

                    currentGroup.addChild(currentAlg)

                currentGroup.sortChildren(0, Qt.AscendingOrder)
                currentProvider.addChild(currentGroup)
            currentProvider.sortChildren(0, Qt.AscendingOrder)
            toolbox.addTopLevelItem(currentProvider)
        return toolbox


    def getAlgorithmMenu(self, context: QpnDbContext = QpnDbContext.BASE) -> QMenu:
        """Get the desired algorithm context tools as a QMenu (NOT IMPLEMENTED)"""
        menu = QMenu(parent=None)
        for provider, groups in self._algDbTree[context]:
            currentProvider = QMenu(provider)
            for group, algorithms in groups:
                currentGroup = QMenu(group)
                for algorithm in algorithms:
                    currentAlg = QMenu(algorithm.name())
                    currentGroup.addAction(currentAlg[0])
                currentProvider.addMenu(currentGroup)
            menu.addMenu(currentProvider)
        return menu
