# coding: utf-8

"""
    Yanshee RESTful API

     ## Overview Yanshee RESTful APIs are generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. By using the [OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) from a remote server. The API service uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.  To provide the API service, Yanshee RESTful APIs are integrated into apollo package, it is a part of Yanshee-ROS framework. Yanshee RESTful APIs provided two language versions: - [English version](https://app.swaggerhub.com/apis-docs/UBTEDU/apollo_en/1.0.0) - [Chinese version](https://app.swaggerhub.com/apis-docs/UBTEDU/apollo_cn/1.0.0)  ## Requirements. Python 2.7 or 3.4+  ## Getting Started Please follow the [installation procedure](#installation--usage) and then run the following:  ``` from __future__ import print_function import time import openadk from openadk.rest import ApiException from pprint import pprint  # create an instance of the API class configuration = openadk.Configuration() configuration.host = 'http://192.168.1.100:9090/v1' api_instance = openadk.DevicesApi(openadk.ApiClient(configuration)) try:  # Get system's battery information  api_response = api_instance.get_devices_battery()  pprint(api_response) except ApiException as e:  print(\"Exception when calling DevicesApi->get_devices_battery: %s\" % e)  ```   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: swenggroup@ubtrobot.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class VisionsStream(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'resolution': 'str'
    }

    attribute_map = {
        'resolution': 'resolution'
    }

    def __init__(self, resolution=None):  # noqa: E501
        """VisionsStream - a model defined in Swagger"""  # noqa: E501

        self._resolution = None
        self.discriminator = None

        if resolution is not None:
            self.resolution = resolution

    @property
    def resolution(self):
        """Gets the resolution of this VisionsStream.  # noqa: E501

         The stream's resolution. The default resolution is 640x480, the max resolution is 640x480.   # noqa: E501

        :return: The resolution of this VisionsStream.  # noqa: E501
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this VisionsStream.

         The stream's resolution. The default resolution is 640x480, the max resolution is 640x480.   # noqa: E501

        :param resolution: The resolution of this VisionsStream.  # noqa: E501
        :type: str
        """

        self._resolution = resolution

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(VisionsStream, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VisionsStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
