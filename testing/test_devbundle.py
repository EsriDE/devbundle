from devbundle.content import DevBundle
from devbundle.software import ArcGISEnterprise

import unittest
from unittest import TestCase


class BundleTestCase(TestCase):

    def setUp(self) -> None:
        self._bundle = DevBundle()

    def test_included_software(self):
        # Validate using the number of software
        software = self._bundle.software
        self.assertLess(5, len(software), 'The bundle must contain more than 5 products!')

        # Validate using the instance type
        has_type = False
        for software in software:
            if isinstance(software, ArcGISEnterprise):
                has_type = True
                break
            
        self.assertTrue(has_type, 'ArcGIS Enterprise must be part of the ArcGIS Developer Bundle!')
        
        # Validate using the product name
        self.assertTrue('ArcGIS Enterprise' in self._bundle.software_names, 'ArcGIS Enterprise must be part of the ArcGIS Developer Bundle!')


if __name__ == '__main__':
    unittest.main()