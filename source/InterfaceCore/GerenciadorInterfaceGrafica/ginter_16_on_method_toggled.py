from utils.LogManager import LogManager

logger = LogManager.get_logger()

def on_method_toggled(self):
    for method, checkbox in self.checkboxes.items():
        if checkbox.isChecked() and method not in self.current_layouts:
            new_layout = self.compression_method_layouts[method]()
            self.current_layouts[method] = new_layout
            self.method_layouts_container.addLayout(new_layout)

        elif not checkbox.isChecked() and method in self.current_layouts:
            layout_to_remove = self.current_layouts.pop(method)
            self.remove_layout_widgets(layout_to_remove)
            self.method_layouts_container.removeItem(layout_to_remove)
            layout_to_remove.deleteLater()

    self.adjust_scroll_area()
