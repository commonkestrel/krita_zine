from krita import *

class ZineExtension(Extension):
    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        create = window.createAction("zineCreate", "Create New Zine", "tools/scripts")
        create.triggered.connect(self.new_doc)

        export = window.createAction("zineExport", "Export Zine", "tools/scripts")
        export.triggered.connect(self.export_doc)

    def new_doc(self):
        # Create letter-sized document
        doc = Krita.instance().createDocument(3300, 2550, "Zine", "RGBA", "U8", "", 300.0)
        Krita.instance().setActiveDocument(doc)

        # Add guides
        doc.setGuidesVisible(True)
        doc.setGuidesLocked(True)
        doc.setHorizontalGuides([2550/2])
        doc.setVerticalGuides([3300/4, 3300/2, 3*3300/4])

        window = Krita.instance().activeWindow()
        view = window.addView(doc)
        window.showView(view)

        return doc

    def export_doc(self):
        doc = Krita.instance().activeDocument()
        if doc is None:
            return
        
        root = doc.rootNode()
        layer = doc.createNode("projection_layer", "paintlayer")
        root.addChildNode(layer, None)

        layer.setPixelData(doc.pixelData(0, 0, 3300, 2550//2), 0, 0, 3300, 2550//2)
        layer.scaleNode(QPoint(0, 2550//4), 3300, -2550//2, "bicubic")

        Krita.instance().action("file_export_file").trigger()

        root.removeChildNode(layer)

Krita.instance().addExtension(ZineExtension(Krita.instance()))
