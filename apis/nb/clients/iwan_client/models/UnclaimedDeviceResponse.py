#!/usr/bin/env python
#pylint: skip-file
"""
Manually generated by Nuno
"""

class UnclaimedDeviceResponse(object):
    """NOTE: Manually generated by Nuno until the API supports swagger."""


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            'version': 'str',
            'response': 'list[UnprovisionedSite]'
        }

        self.attributeMap = {
            'version': 'version',
            'response': 'response'
        }

        self.version = None # str
        self.response = None # list[UnprovisionedSite]