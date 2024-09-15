from biodataviz.core.stats import StatsComputationStep, StatsChain
from biodataviz.common.stats import ParametricCheck

import numpy as np
import pandas as pd
import pingouin as pg

class TwoGroupsNoRepeatedMeasuresCompStep(StatsComputationStep):

    def compute_stats(self, 
                      source_data: pd.DataFrame, 
                      current_results: dict,
                      **kwargs
                     ) -> dict:
        if current_results['parametric_test_ok'] == True:
            current_results['final_results'] = self._compute_ttest(source_data, **kwargs)
        else:
            current_results['final_results'] = self._compute_mwu(source_data, **kwargs)
        return current_results


    def _compute_ttest(self, source_data: pd.DataFrame, **kwargs) -> pd.DataFrame:
        data_group_a, data_group_b = self._extract_data_per_group(source_data, **kwargs)
        df_ttest = pg.ttest(data_group_a, data_group_b)
        return df_ttest


    def _compute_mwu(self, source_data: pd.DataFrame, **kwargs) -> pd.DataFrame:
        data_group_a, data_group_b = self._extract_data_per_group(source_data, **kwargs)
        df_mwu = pg.mwu(data_group_a, data_group_b)
        return df_mwu
        

    def _extract_data_per_group(self, source_data: pd.DataFrame, **kwargs) -> tuple[np.ndarray, np.ndarray]:
        group_col_name = kwargs['group_column_name']
        dv_col_name = kwargs['dependent_variable_column_name']
        id_group_a, id_group_b = source_data[group_col_name].unique()
        data_group_a = source_data.query(f'{group_col_name} == "{id_group_a}"')[dv_col_name].values
        data_group_b = source_data.query(f'{group_col_name} == "{id_group_b}"')[dv_col_name].values
        return data_group_a, data_group_b



class TwoGroupsNoRepeatedMeasuresStatsChain(StatsChain):

    @property
    def _all_comp_steps_to_create(self) -> list[StatsComputationStep]:  
        return [ParametricCheck, TwoGroupsNoRepeatedMeasuresCompStep]