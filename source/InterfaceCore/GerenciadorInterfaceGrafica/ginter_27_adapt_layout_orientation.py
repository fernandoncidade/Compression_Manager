from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget
from source.utils.LogManager import LogManager

logger = LogManager.get_logger()


def adapt_layout_orientation(self):
    if not hasattr(self, 'columns_widget') or not hasattr(self, 'primeiro_layout_widget'):
        return

    is_segundo_active = (
        hasattr(self, 'segundo_layout_action') and 
        self.segundo_layout_action.isChecked() and 
        getattr(self, 'segundo_layout_widget', None) is not None
    )

    win_w = self.width()
    win_h = self.height()

    # Layout 2 MUST be placed side-by-side to the RIGHT of Layout 1 by default (QHBoxLayout).
    # Only switch to vertical stack if window is explicitly in extreme vertical portrait mode (win_h > 1.5 * win_w).
    if is_segundo_active:
        is_portrait = (win_h > 1.5 * win_w)
    else:
        is_portrait = False

    target_layout_cls = QVBoxLayout if is_portrait else QHBoxLayout
    current_layout = self.columns_widget.layout()

    if isinstance(current_layout, target_layout_cls):
        return

    # Extract widgets from existing layout safely
    current_layout.removeWidget(self.primeiro_layout_widget)
    if is_segundo_active and getattr(self, 'segundo_layout_widget', None):
        current_layout.removeWidget(self.segundo_layout_widget)

    # Delete existing layout
    QWidget().setLayout(current_layout)

    # Re-create layout with new orientation (QHBoxLayout places Layout 2 directly to the right of Layout 1)
    new_layout = target_layout_cls(self.columns_widget)
    new_layout.setContentsMargins(0, 0, 0, 0)
    new_layout.setSpacing(10)
    new_layout.addWidget(self.primeiro_layout_widget, 1)

    if is_segundo_active and getattr(self, 'segundo_layout_widget', None):
        new_layout.addWidget(self.segundo_layout_widget, 1)

    self.columns_widget.setLayout(new_layout)
