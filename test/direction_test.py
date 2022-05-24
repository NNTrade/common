from src.direction import direction
import unittest
import logging


class DirectionTestCase(unittest.TestCase):
    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

    def test_parse(self):
      self.assertEqual(direction.parse("long"), direction.Long)
      self.assertEqual(direction.parse("Long"), direction.Long)
      self.assertEqual(direction.parse("LONG"), direction.Long)
      self.assertEqual(direction.parse("LoNg"), direction.Long)
      self.assertEqual(direction.parse("short"), direction.Short)
      self.assertEqual(direction.parse("Short"), direction.Short)
      self.assertEqual(direction.parse("SHORT"), direction.Short)
      self.assertEqual(direction.parse("shOrt"), direction.Short)
