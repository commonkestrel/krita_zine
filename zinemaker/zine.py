from krita import *
import zipfile
from math import pi

HELPER_LAYER = "Zine Help Layer commonkestrel_krita_zine_helper"
HEIGHT = 2550
WIDTH = 3300

class ZineExtension(Extension):
    def __init__(self, parent):
        self.help_layers = []
        super().__init__(parent)

    def setup(self):
        path = Krita.getAppDataLocation() + "/pykrita/zinemaker/overlay.zip"
        with zipfile.ZipFile(path, 'r') as zip:
            self.overlay = QByteArray(zip.read("overlay"))

    def createActions(self, window):
        create = window.createAction("zineCreate", "Create New Zine", "tools/scripts")
        create.triggered.connect(self.new_doc)

        export = window.createAction("zineExport", "Export Zine", "tools/scripts")
        export.triggered.connect(self.export_doc)

    def new_doc(self):
        # Create letter-sized document
        doc = Krita.instance().createDocument(WIDTH, HEIGHT, "Zine", "RGBA", "U8", "", 300.0)
        Krita.instance().setActiveDocument(doc)

        # Add guides
        doc.setGuidesVisible(True)
        doc.setGuidesLocked(True)
        doc.setHorizontalGuides([HEIGHT/2])
        doc.setVerticalGuides([WIDTH/4, WIDTH/2, 3*WIDTH/4])

        window = Krita.instance().activeWindow()
        view = window.addView(doc)
        window.showView(view)

        layer = doc.createNode(HELPER_LAYER, "paintlayer")
        layer.setPixelData(self.overlay, 0, 0, WIDTH, HEIGHT)

        root = doc.rootNode()
        root.addChildNode(layer, None)

        self.help_layers.append(layer)

    def export_doc(self):
        doc = Krita.instance().activeDocument()
        if doc is None:
            return
        
        height = doc.height()
        width = doc.width()
        
        root = doc.rootNode()
        helpers = root.findChildNodes(HELPER_LAYER)
        nodes = list(map(hide_visible, helpers))

        layer = doc.createNode("projection_layer", "paintlayer")
        root.addChildNode(layer, None)

        layer.setPixelData(doc.pixelData(0, 0, width, height//2), 0, 0, width, height//2)
        layer.rotateNode(pi)

        Krita.instance().action("file_export_file").trigger()

        for node in nodes:
            node[0].setVisible(node[1])
        root.removeChildNode(layer)

def hide_visible(node: Node):
    visible = node.visible()
    node.setVisible(False)
    return (node, visible)
    
Krita.instance().addExtension(ZineExtension(Krita.instance()))
