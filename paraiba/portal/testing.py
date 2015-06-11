# -*- coding: utf-8 -*-
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

from zope.configuration import xmlconfig

class ParaibaPortal(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import paraiba.portal
        xmlconfig.file('configure.zcml',
                paraiba.portal,
                context=configurationContext
            )
    def setUpPloneSite(self, portal):
        applyProfile(portal, 'paraiba.portal:default')

PARAIBA_PORTAL_FIXTURE = ParaibaPortal()
PARAIBA_PORTAL_INTEGRATION_TESTING = IntegrationTesting(
        bases=(PARAIBA_PORTAL_FIXTURE,),
        name="Paraiba:Integration"
)