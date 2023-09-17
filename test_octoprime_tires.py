import unittest
from tires.octoprime_tires import OctoprimeTires

class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [1.0, 1.0, 1.0, 1.0]
        tires = OctoprimeTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.1, 0.2, 1.0, 1.0]
        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.needs_service())

if __name__ == '__main__':
    unittest.main()