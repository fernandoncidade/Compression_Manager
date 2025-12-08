from source.utils.LogManager import LogManager

logger = LogManager.get_logger()

def remove_layout_widgets(self, layout):
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)

            else:
                self.remove_layout_widgets(item.layout())
