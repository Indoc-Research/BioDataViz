from biodataviz.core.user_settings import UserSettingsView, UserSettings
from biodataviz.common.user_settings import FigureSettings, XYAxisSettings

import ipywidgets as w


class StripplotSettings(UserSettings):

    @property
    def accordion_title(self) -> str:
        return 'Marker configurations'
        

    def _build_vbox_with_user_settings_widgets(self) -> w.VBox:
        self.user_settings_marker_size = w.BoundedFloatText(description = 'Marker size:', value = 8.0, min = 0.1, max = 100.0, step = 0.1)
        self.user_settings_marker_color = w.Dropdown(description = 'Marker color:', options = ['magenta', 'cyan', 'yellow'], value = 'magenta')
        v_box = w.VBox([self.user_settings_marker_size, self.user_settings_marker_color])
        return v_box



class StripplotSettingsView(UserSettingsView):

    @property
    def _all_user_settings_to_create(self) -> list[UserSettings]:
        return [FigureSettings, XYAxisSettings, StripplotSettings]