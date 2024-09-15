from biodataviz.core.user_settings import UserSettings

import ipywidgets as w



class FigureSettings(UserSettings):

    @property
    def accordion_title(self) -> str:
        return 'General Figure settings'


    def _build_vbox_with_user_settings_widgets(self) -> w.VBox:
        self.user_settings_figure_width_in_cm = w.FloatSlider(description = 'Figure width [cm]:', value = 16)
        self.user_settings_figure_height_in_cm = w.FloatSlider(description = 'Figure height [cm]:', value = 9)
        self.user_settings_figure_face_color = w.Dropdown(description = 'Background color:', 
                                                          options = ['white', 'black', 'transparent'],
                                                          value = 'white')
        self.user_settings_figure_filename = w.Text(description = 'Filename:', value = 'plot.png', 
                                                    placeholder = 'Please include the filetype extension, e.g.: plot.png')
        self.user_settings_figure_dpi = w.IntSlider(description = 'DPI:', value = 300, min = 150, max = 1400, step = 20)
        v_box = w.VBox([w.HBox([self.user_settings_figure_width_in_cm, self.user_settings_figure_height_in_cm]),
                        self.user_settings_figure_face_color,
                        w.HBox([self.user_settings_figure_filename, self.user_settings_figure_dpi])])
        return v_box
        


class XYAxisSettings(UserSettings):

    @property
    def accordion_title(self) -> str:
        return 'X and Y axis configurations'
        

    def _build_vbox_with_user_settings_widgets(self):
        self.user_settings_y_axis_label_text = w.Text(description = 'Y-Axis label:', value = 'Y')
        self.user_settings_x_axis_label_text = w.Text(description = 'X-Axis label:', value = 'X')
        v_box = w.VBox([self.user_settings_y_axis_label_text, self.user_settings_x_axis_label_text])
        return v_box