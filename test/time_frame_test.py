from src.time_frame import TimeFrame
import unittest
import logging


class TimeFrameTestCase(unittest.TestCase):
    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

    def test_parse_from_str(self):
        # Array
        expectedTf = TimeFrame.m1

        # Act

        # Assert
        self.assertEqual(expectedTf, TimeFrame.parse("m1"))
        self.assertEqual(expectedTf, TimeFrame.parse("M1"))
        self.assertEqual(expectedTf, TimeFrame.parse("minute1"))
        self.assertEqual(expectedTf, TimeFrame.parse("minUte1"))

    def test_parse_from_str_def_func(self):
        # Array
        expectedTf = TimeFrame.m1

        # Act

        # Assert
        self.assertEqual(expectedTf, TimeFrame["m1"])
        self.assertEqual(expectedTf, TimeFrame["MINUTE1"])

    def test_WHEN_compare_THEN_correct(self):
        # Array
        tf1 = TimeFrame.HOUR4
        tf2 = TimeFrame.DAY

        # Act
        
        # Assert
        self.assertTrue(tf1 < tf2)

    def test_WHEN_convert_to_THEN_print_also_converting(self):
        # Array
    
        # Act
    
        # Assert
        self.assertEqual(f"{TimeFrame.DAY}", f"{TimeFrame.D.to_full()}")
        self.assertEqual(f"{TimeFrame.D}", f"{TimeFrame.DAY.to_short()}")