from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QSizePolicy
from source.utils.LogManager import LogManager

logger = LogManager.get_logger()

def toggle_segundo_layout(self):
    is_checked = self.segundo_layout_action.isChecked()

    if is_checked:
        # Expand window width if currently narrower than 1200px to fit both layouts side-by-side
        if self.width() < 1200:
            self.resize(1200, max(self.height(), 750))

        self.segundo_layout_column = QVBoxLayout()

        first_quadrant_2 = self.create_first_quadrant_2()
        second_quadrant_2 = self.create_second_quadrant_2()
        main_layout_1_2 = QHBoxLayout()
        main_layout_1_2.addLayout(first_quadrant_2)
        main_layout_1_2.addLayout(second_quadrant_2)

        self.main_layout_1_widget_2 = self.create_widget_with_layout(main_layout_1_2)
        self.main_layout_1_widget_2.setMinimumHeight(152)
        self.main_layout_1_widget_2.setMaximumHeight(304)
        self.segundo_layout_column.addWidget(self.main_layout_1_widget_2)

        third_quadrant_2 = QVBoxLayout()
        self.create_method_checkboxes_2(third_quadrant_2)
        main_layout_2_2 = QHBoxLayout()
        main_layout_2_2.addLayout(third_quadrant_2)
        self.segundo_layout_column.addWidget(self.create_widget_with_layout(main_layout_2_2))

        scroll_area_2_widget = self.create_scroll_area_2()
        self.segundo_layout_column.addWidget(scroll_area_2_widget)

        self.segundo_layout_widget = QWidget()
        self.segundo_layout_widget.setLayout(self.segundo_layout_column)
        self.segundo_layout_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        if self.columns_widget.layout():
            self.columns_widget.layout().addWidget(self.segundo_layout_widget, 1)

        self.adjust_scroll_area()
        self.adapt_layout_orientation()

    else:
        for method in list(self.current_layouts_2.keys()):
            layout_to_remove = self.current_layouts_2.pop(method)
            self.remove_layout_widgets(layout_to_remove)
            self.method_layouts_container_2.removeItem(layout_to_remove)
            layout_to_remove.deleteLater()

        if hasattr(self, 'segundo_layout_widget') and self.segundo_layout_widget is not None:
            if self.columns_widget.layout():
                self.columns_widget.layout().removeWidget(self.segundo_layout_widget)
            self.segundo_layout_widget.setParent(None)
            self.segundo_layout_widget.deleteLater()
            self.segundo_layout_widget = None

        if hasattr(self, 'checkboxes_2'):
            self.checkboxes_2.clear()

        self.main_buttons_2.clear()
        self.methods_group_2 = None

        self.adjust_scroll_area()
        self.adapt_layout_orientation()
