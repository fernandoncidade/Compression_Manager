from utils.LogManager import LogManager

logger = LogManager.get_logger()

def rebuild_method_layouts(self):
    for method in list(self.current_layouts.keys()):
        layout_to_remove = self.current_layouts.pop(method)
        self.remove_layout_widgets(layout_to_remove)
        self.method_layouts_container.removeItem(layout_to_remove)
        layout_to_remove.deleteLater()

    for method, checkbox in self.checkboxes.items():
        if checkbox.isChecked():
            new_layout = self.compression_method_layouts[method]()
            self.current_layouts[method] = new_layout
            self.method_layouts_container.addLayout(new_layout)

    self.adjust_scroll_area()
