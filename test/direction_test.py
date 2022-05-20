import src.direction as dir
import unittest
import logging


class DirectionTestCase(unittest.TestCase):
    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

    def test_parse(self):
      self.assertEqual(dir.direction.from_str("long"), dir.direction.Long)
      self.assertEqual(dir.direction.from_str("Long"), dir.direction.Long)
      self.assertEqual(dir.direction.from_str("LONG"), dir.direction.Long)
      self.assertEqual(dir.direction.from_str("LoNg"), dir.direction.Long)
      self.assertEqual(dir.direction.from_str("short"), dir.direction.Short)
      self.assertEqual(dir.direction.from_str("Short"), dir.direction.Short)
      self.assertEqual(dir.direction.from_str("SHORT"), dir.direction.Short)
      self.assertEqual(dir.direction.from_str("shOrt"), dir.direction.Short)
