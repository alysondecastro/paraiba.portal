# -*- coding: utf-8 -*-
import unittest2 as unittest
from paraiba.portal.testing import PARAIBA_PORTAL_INTEGRATION_TESTING

class TestSetup(unittest.TestCase):
    
    layer = PARAIBA_PORTAL_INTEGRATION_TESTING
    
    def test_portal_title(self):
        portal = self.layer['portal']
        self.assertEqual(
            "Secretaria de Comunicação",
            portal.getProperty('title')
        )

    def test_portal_description(self):
        portal = self.layer['portal']
        self.assertEqual(
            "Portal do Governo do Estado da Paraíba",
            portal.getProperty('description')
        )
