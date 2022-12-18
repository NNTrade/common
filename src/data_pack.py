from __future__ import annotations
from argparse import ArgumentError
from typing import List
import pandas as pd


class DataPack:
    @staticmethod
    def __compare_columns(columns1: List[str], columns2: List[str]) -> bool:
        if len(columns1) != len(columns2):
            return False
        for c in columns1:
            if c not in columns2:
                return False
        return True

    @staticmethod
    def join(data_packs: List[DataPack]) -> DataPack:
        x_df_arr = []
        y_df_arr = []
        base_x_columns = None
        base_y_columns = None
        for dp in data_packs:
            if base_x_columns is None:
                base_x_columns = dp.input_df.columns
            elif not DataPack.__compare_columns(base_x_columns, dp.input_df.columns):
                raise ArgumentError(data_packs,
                                    message=f"Columns doesn't equals in input data")
            if base_y_columns is None:
                base_y_columns = dp.output_df.columns
            elif not DataPack.__compare_columns(base_y_columns, dp.output_df.columns):
                raise ArgumentError(data_packs,
                                    message=f"Columns doesn't equals in output data")

            x_df_arr.append(dp.input_df.copy(True))
            y_df_arr.append(dp.output_df.copy(True))

        return DataPack(pd.concat(x_df_arr), pd.concat(y_df_arr))

    def __init__(self, input_df: pd.DataFrame, output_df: pd.DataFrame) -> None:
        if len(input_df.index) != len(output_df.index):
            raise ArgumentError(input_df,
                                message=f"Count of index in X df != Y df ({len(input_df.index)} != {len(output_df.index)}")
        for idx, idx_val in enumerate(input_df.index):
            if idx_val != output_df.index[idx]:
                raise ArgumentError(
                    input_df, message=f"Value of indexes, not equal in X df and Y df")
        self.input_df = input_df
        self.output_df = output_df
