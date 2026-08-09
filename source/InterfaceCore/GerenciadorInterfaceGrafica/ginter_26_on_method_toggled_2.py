from source.utils.LogManager import LogManager

logger = LogManager.get_logger()

def on_method_toggled_2(self):
    for method, checkbox in self.checkboxes_2.items():
        if checkbox.isChecked() and method not in self.current_layouts_2:
            new_layout = self.compression_method_layouts_2[method]()
            self.current_layouts_2[method] = new_layout
            self.method_layouts_container_2.addLayout(new_layout)

        elif not checkbox.isChecked() and method in self.current_layouts_2:
            layout_to_remove = self.current_layouts_2.pop(method)
            self.remove_layout_widgets(layout_to_remove)
            self.method_layouts_container_2.removeItem(layout_to_remove)
            layout_to_remove.deleteLater()

    self.adjust_scroll_area()
