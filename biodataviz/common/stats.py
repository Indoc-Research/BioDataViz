from biodataviz.core.stats import StatsComputationStep

import pandas as pd
import pingouin as pg


class ParametricCheck(StatsComputationStep):

    def compute_stats(self, 
                      source_data: pd.DataFrame, 
                      current_results: dict,
                      **kwargs
                     ) -> dict:
        current_results['normal_distribution'] = self._check_normal_distribution(source_data, **kwargs)
        current_results['homoscedasticity'] = self._check_homoscedasticity(source_data, **kwargs)
        current_results['parametric_test_ok'] = self._check_if_parametric_test_can_be_used(current_results)
        return current_results


    def _check_normal_distribution(self, source_data: pd.DataFrame, **kwargs) -> pd.DataFrame:
        df_normality_results = pg.normality(data = source_data,
                                            dv = kwargs['dependent_variable_column_name'],
                                            group = kwargs['group_column_name'])
        return df_normality_results


    def _check_homoscedasticity(self, source_data: pd.DataFrame, **kwargs) -> pd.DataFrame:
        df_homoscedasticity_results = pg.homoscedasticity(data = source_data,
                                                          dv = kwargs['dependent_variable_column_name'],
                                                          group = kwargs['group_column_name'])
        return df_homoscedasticity_results


    def _check_if_parametric_test_can_be_used(self, current_results: dict) -> bool:
        if (current_results['normal_distribution']['normal'].all() == True) & (current_results['homoscedasticity']['equal_var'].iloc[0] == True):
            parametric_test_ok = True
        else:
            parametric_test_ok = False
        return parametric_test_ok



    
                                                          