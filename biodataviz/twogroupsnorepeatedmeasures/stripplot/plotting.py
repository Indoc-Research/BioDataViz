from biodataviz.core.plotting import PlotterChain, PlotConfigurator
from biodataviz.common.plotting import FigureConfigurator, XYAxisConfigurator

from matplotlib.figure import Figure
from matplotlib.axes import Axes

import seaborn as sns


class StripplotConfigurator(PlotConfigurator):

    def configure_plot(self, fig: Figure, ax: Axes, **kwargs) -> tuple[Figure, Axes]:
        df = kwargs['source_data']
        sns.stripplot(data = df, x = 'group', y = 'measure', 
                      color = kwargs['marker_color'], size = kwargs['marker_size'], 
                      legend = False, ax = ax)
        return fig, ax



class StripplotChain(PlotterChain):

    @property
    def _all_plot_configurators_to_create(self) -> list[PlotConfigurator]:
        return [FigureConfigurator, StripplotConfigurator, XYAxisConfigurator]