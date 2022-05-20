import src.candle_col_name as ccn
import unittest
import logging


class CandleColNameTestCase(unittest.TestCase):
    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

    def test_def_values(self):
      self.assertEqual('low',ccn.LOW)
      self.assertEqual('high',ccn.HIGH)
      self.assertEqual('open',ccn.OPEN)
      self.assertEqual('high',ccn.HIGH)

    def test_rename_values(self):
      ccn.LOW = "low1"
      ccn.HIGH = "high1"
      ccn.OPEN = "open1"
      ccn.CLOSE = "close1"
      self.assertEqual('low1',ccn.LOW)
      self.assertEqual('high1',ccn.HIGH)
      self.assertEqual('open1',ccn.OPEN)
      self.assertEqual('high1',ccn.HIGH)