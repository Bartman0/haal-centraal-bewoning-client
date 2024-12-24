# coding: utf-8

"""
    BRP bewoning

    API voor het raadplegen van de (historische) bewoning van een adres. 

    The version of the OpenAPI document: 2.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from brp_bewoning_client.models.jaar_maand_datum import JaarMaandDatum

class TestJaarMaandDatum(unittest.TestCase):
    """JaarMaandDatum unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JaarMaandDatum:
        """Test JaarMaandDatum
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JaarMaandDatum`
        """
        model = JaarMaandDatum()
        if include_optional:
            return JaarMaandDatum(
                jaar = 1,
                maand = 1
            )
        else:
            return JaarMaandDatum(
                jaar = 1,
                maand = 1,
        )
        """

    def testJaarMaandDatum(self):
        """Test JaarMaandDatum"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
