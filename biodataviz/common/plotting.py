from biodataviz.core.plotting import PlotConfigurator

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes


class FigureConfigurator(PlotConfigurator):

    def configure_plot(self, fig: Figure, ax: Axes, **kwargs) -> tuple[Figure, Axes]:
        fig.set_figwidth(kwargs['figure_width_in_cm'] * 0.393701)
        fig.set_figheight(kwargs['figure_height_in_cm'] * 0.393701)
        fig.set_facecolor(kwargs['figure_face_color'])
        ax.spines[['right', 'top']].set_visible(False)
        return fig, ax


class XYAxisConfigurator(PlotConfigurator):

    def configure_plot(self, fig: Figure, ax: Axes, **kwargs) -> tuple[Figure, Axes]:
        ax.set_ylabel(kwargs['y_axis_label_text'])
        ax.set_xlabel(kwargs['x_axis_label_text'])
        return fig, ax