from abc import ABC, abstractmethod
from pandas import DataFrame


class StatsComputationStep(ABC):

    @abstractmethod
    def compute_stats(self, 
                      source_data: DataFrame, 
                      current_results: dict,
                      **kwargs
                     ) -> dict:
        pass



class StatsChain(ABC):

    @property
    @abstractmethod
    def _all_comp_steps_to_create(self) -> list[StatsComputationStep]:  
        # Create a list here of all specific StatsComputationStep classes
        pass

    def __init__(self) -> None:
        self._instantiate_all_comp_steps()


    def _instantiate_all_comp_steps(self) -> None:
        if hasattr(self, 'all_comp_steps') == False:
            all_comp_steps = [comp_step() for comp_step in self._all_comp_steps_to_create]
            setattr(self, 'all_comp_steps', all_comp_steps)


    def compute_stats(self, source_data: DataFrame, **kwargs) -> dict:
        results = {}
        for comp_step in self.all_comp_steps:
            results = comp_step.compute_stats(source_data, results, **kwargs)
        return results


    

    
