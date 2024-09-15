from biodataviz.core.user_settings import UserSettingsView
from biodataviz.core.plotting import PlotterChain
from biodataviz.core.stats import StatsChain

import matplotlib.pyplot as plt

from matplotlib.figure import Figure
from matplotlib.axes import Axes
from ipywidgets import Button
from pandas import DataFrame



class VisualizationController:

    def __init__(self, 
                 user_settings_view: UserSettingsView,
                 plotter_chain: PlotterChain
                ) -> None:
        self._set_input_as_attributes(user_settings_view, plotter_chain)
        self._link_all_widgets_to_functions()


    def _set_input_as_attributes(self, 
                                 user_settings_view: UserSettingsView,
                                 plotter_chain: PlotterChain
                                ) -> None:
        self.user_settings_view = user_settings_view
        self.plotter_chain = plotter_chain


    def _link_all_widgets_to_functions(self) -> None:
        self._setup_all_observers()
        self._setup_button_click_events()


    def _setup_all_observers(self) -> None:
        for user_settings in self.user_settings_view.all_user_settings:
            for individual_widget in user_settings.configurable_widgets.values():
                individual_widget.observe(self._refresh_plot_via_observers)


    def _refresh_plot_via_observers(self, change: dict) -> None:
        if change['name'] == 'value':
            self._refresh_plot()


    def _setup_button_click_events(self) -> None:
        self.user_settings_view.refresh_plot_button.on_click(self._refresh_plot_via_button)
        self.user_settings_view.save_plot_button.on_click(self._save_plot_via_button)


    def _refresh_plot_via_button(self, button_click_event: Button) -> None:
        self._refresh_plot()


    def _get_kwargs_for_plotting(self) -> dict:
        configs = self.user_settings_view.export_all_user_settings()
        kwargs = {'source_data': self.source_data, **configs}
        return kwargs
                  

    def _save_plot_via_button(self, button_click_event: Button) -> None:
        kwargs = self._get_kwargs_for_plotting()
        self.plotter_chain.save_plot(**configs)


    def _refresh_plot(self) -> None:
        kwargs = self._get_kwargs_for_plotting()
        fig, ax = self.plotter_chain.create_plot(**kwargs)
        with self.user_settings_view.plot_output:
            self.user_settings_view.plot_output.clear_output()
            plt.show()
        plt.close(fig)


    def set_source_data(self, source_data: DataFrame) -> None:
        self.source_data = source_data



        


    
        




