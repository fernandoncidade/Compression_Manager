from utils.LogManager import LogManager

logger = LogManager.get_logger()

def adjust_scroll_area(self):
    num_layouts = len(self.current_layouts)
    max_layouts = min(num_layouts, 4)
    self.scroll_area.setMinimumHeight(347 + max_layouts * 10)
    self.main_layout_1_widget.setMaximumHeight(304 - max_layouts * 20)
