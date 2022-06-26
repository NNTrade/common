import unittest
import logging
from src.data_pack import DataPack
from datetime import datetime
import pandas as pd

from test.test_tools import compare_df


class DataPack_TestCase(unittest.TestCase):

    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    def test_WHEN_create_instance_with_dif_index_THEN_get_error(self):
        # Array
        x_data_df = pd.DataFrame(
            {"A": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "B": [
                11, 21, 31, 41, 51, 61, 71, 81, 91, 11]},
            index=[datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3), datetime(2020, 1, 4), datetime(2020, 1, 5), datetime(2020, 1, 6), datetime(2020, 1, 7), datetime(2020, 1, 8), datetime(2020, 1, 9), datetime(2020, 1, 10)])
        y_data_df = pd.DataFrame(
            {"AA": [11, 12, 13, 14, 15, 16, 17, 18, 19, 110], "BB": [
                111, 121, 131, 141, 151, 161, 171, 181, 191, 111]},
            index=[datetime(2019, 12, 30), datetime(2020, 1, 2), datetime(2020, 1, 3), datetime(2020, 1, 4), datetime(2020, 1, 5), datetime(2020, 1, 6), datetime(2020, 1, 7), datetime(2020, 1, 8), datetime(2020, 1, 9), datetime(2020, 1, 10)])

        # Act

        # Assert
        with self.assertRaises(Exception):
            DataPack(x_data_df, y_data_df)

    def test_WHEN_create_instance_with_dif_count_of_index_THEN_get_error(self):
        # Array
        x_data_df = pd.DataFrame(
            {"A": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "B": [
                11, 21, 31, 41, 51, 61, 71, 81, 91, 11]},
            index=[datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3), datetime(2020, 1, 4), datetime(2020, 1, 5), datetime(2020, 1, 6), datetime(2020, 1, 7), datetime(2020, 1, 8), datetime(2020, 1, 9), datetime(2020, 1, 10)])
        y_data_df = pd.DataFrame(
            {"AA": [12, 13, 14, 15, 16, 17, 18, 19, 110], "BB": [
                121, 131, 141, 151, 161, 171, 181, 191, 111]},
            index=[datetime(2020, 1, 2), datetime(2020, 1, 3), datetime(2020, 1, 4), datetime(2020, 1, 5), datetime(2020, 1, 6), datetime(2020, 1, 7), datetime(2020, 1, 8), datetime(2020, 1, 9), datetime(2020, 1, 10)])

        # Act

        # Assert
        with self.assertRaises(Exception):
            DataPack(x_data_df, y_data_df)

    def test_WHEN_join_THEN_get_correct_data(self):
        # Array
        x1_df = pd.DataFrame({"A": [1, 2, 3], "B": [11, 22, 33]}, index=[
                             datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3)])
        y1_df = pd.DataFrame({"AA": [0.1, 0.2, 0.3], "BA": [0.11, 0.22, 0.33]}, index=[
                             datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3)])

        x2_df = pd.DataFrame({"A": [11, 12, 13], "B": [111, 122, 133]}, index=[
                             datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3)])
        y2_df = pd.DataFrame({"AA": [0.11, 0.12, 0.13], "BA": [0.111, 0.122, 0.133]}, index=[
                             datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3)])

        dp1 = DataPack(x1_df, y1_df)
        dp2 = DataPack(x2_df, y2_df)

        expected_x_df = pd.DataFrame({"A": [1, 2, 3, 11, 12, 13], "B": [11, 22, 33, 111, 122, 133]}, index=[datetime(
            2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3), datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3)])
        expected_y_df = pd.DataFrame({"AA": [0.1, 0.2, 0.3, 0.11, 0.12, 0.13], "BA": [0.11, 0.22, 0.33, 0.111, 0.122, 0.133]}, index=[
                                     datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3), datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3)])

        # Act
        asserted_dp = DataPack.join([dp1, dp2])

        # Assert
        compare_df(self, expected_x_df, asserted_dp.input_df)
        compare_df(self, expected_y_df, asserted_dp.output_df)

    def test_WHEN_join_dif_X_columns_THEN_get_error(self):
        # Array
        x1_df = pd.DataFrame({"A": [1, 2, 3], "B": [11, 22, 33]}, index=[
                             datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3)])
        y1_df = pd.DataFrame({"AA": [0.1, 0.2, 0.3], "BA": [0.11, 0.22, 0.33]}, index=[
                             datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3)])

        x2_df = pd.DataFrame({"A": [11, 12, 13], "Ba": [111, 122, 133]}, index=[
                             datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3)])
        y2_df = pd.DataFrame({"AA": [0.11, 0.12, 0.13], "BA": [0.111, 0.122, 0.133]}, index=[
                             datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3)])

        dp1 = DataPack(x1_df, y1_df)
        dp2 = DataPack(x2_df, y2_df)

        # Act

        # Assert
        with self.assertRaises(Exception):
            asserted_dp = DataPack.join([dp1, dp2])

    def test_WHEN_join_dif_Y_columns_THEN_get_error(self):
        # Array
        x1_df = pd.DataFrame({"A": [1, 2, 3], "B": [11, 22, 33]}, index=[
                             datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3)])
        y1_df = pd.DataFrame({"AA": [0.1, 0.2, 0.3], "Bt": [0.11, 0.22, 0.33]}, index=[
                             datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3)])

        x2_df = pd.DataFrame({"A": [11, 12, 13], "Ba": [111, 122, 133]}, index=[
                             datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3)])
        y2_df = pd.DataFrame({"AA": [0.11, 0.12, 0.13], "BA": [0.111, 0.122, 0.133]}, index=[
                             datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3)])

        dp1 = DataPack(x1_df, y1_df)
        dp2 = DataPack(x2_df, y2_df)

        # Act

        # Assert
        with self.assertRaises(Exception):
            asserted_dp = DataPack.join([dp1, dp2])
