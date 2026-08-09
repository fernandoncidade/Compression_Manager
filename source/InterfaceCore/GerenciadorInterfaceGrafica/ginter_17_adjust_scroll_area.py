from source.utils.LogManager import LogManager

logger = LogManager.get_logger()

def adjust_scroll_area(self):
    num_layouts = len(self.current_layouts)
    max_layouts = min(num_layouts, 4)
    self.scroll_area.setMinimumHeight(347 + max_layouts * 10)
    self.main_layout_1_widget.setMaximumHeight(304 - max_layouts * 20)

    if hasattr(self, 'scroll_area_2') and self.scroll_area_2 is not None:
        num_layouts_2 = len(self.current_layouts_2)
        max_layouts_2 = min(num_layouts_2, 4)
        self.scroll_area_2.setMinimumHeight(347 + max_layouts_2 * 10)
        if hasattr(self, 'main_layout_1_widget_2') and self.main_layout_1_widget_2 is not None:
            self.main_layout_1_widget_2.setMaximumHeight(304 - max_layouts_2 * 20)
