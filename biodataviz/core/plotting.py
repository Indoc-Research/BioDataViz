import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

from abc import ABC, abstractmethod



class PlotConfigurator(ABC):

    @abstractmethod
    def configure_plot(self, fig: Figure, ax: Axes, **kwargs) -> tuple[Figure, Axes]:
        pass



class PlotterChain(ABC):

    @property
    @abstractmethod
    def _all_plot_configurators_to_create(self) -> list[PlotConfigurator]:
        # Add all plot configurator objects here as a list
        pass


    def __init__(self) -> None:
        self._instantiate_all_plot_configurators()


    def _instantiate_all_plot_configurators(self) -> None:
        if hasattr(self, 'all_plot_configurators') == False:
            all_plot_configurators = [plot_configurator() for plot_configurator in self._all_plot_configurators_to_create]
            setattr(self, 'all_plot_configurators', all_plot_configurators)

    
    def create_plot(self, **kwargs) -> tuple[Figure, Axes]:
        fig, ax = plt.subplots()
        for plot_handler in self.all_plot_configurators:
            fig, ax = plot_handler.configure_plot(fig, ax, **kwargs)
        return fig, ax
    
    
    def save_plot(self, **kwargs) -> None:
        fig, ax = self.create_plot(**kwargs)
        fig.tight_layout()
        fig.savefig(kwargs['figure_filename'], dpi = kwargs['figure_dpi'])
        plt.close(fig)