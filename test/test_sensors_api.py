# coding: utf-8

"""
    Yanshee RESTful API

     ## Overview Yanshee RESTful APIs are generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. By using the [OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) from a remote server. The API service uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.  To provide the API service, Yanshee RESTful APIs are integrated into apollo package, it is a part of Yanshee-ROS framework. Yanshee RESTful APIs provided two language versions: - [English version](https://app.swaggerhub.com/apis-docs/UBTEDU/apollo_en/1.0.0) - [Chinese version](https://app.swaggerhub.com/apis-docs/UBTEDU/apollo_cn/1.0.0)  ## Requirements. Python 2.7 or 3.4+  ## Getting Started Please follow the [installation procedure](#installation--usage) and then run the following:  ``` from __future__ import print_function import time import openadk from openadk.rest import ApiException from pprint import pprint  # create an instance of the API class configuration = openadk.Configuration() configuration.host = 'http://192.168.1.100:9090/v1' api_instance = openadk.DevicesApi(openadk.ApiClient(configuration)) try:  # Get system's battery information  api_response = api_instance.get_devices_battery()  pprint(api_response) except ApiException as e:  print(\"Exception when calling DevicesApi->get_devices_battery: %s\" % e)  ```   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: swenggroup@ubtrobot.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import openadk
from openadk.api.sensors_api import SensorsApi  # noqa: E501
from openadk.rest import ApiException

from openadk.models.sensors_operation_request import SensorsOperationRequest
from openadk.models.sensors_parameter import SensorsParameter


class TestSensorsApi(unittest.TestCase):
    """SensorsApi unit test stubs"""

    def setUp(self):
        self.configuration = openadk.Configuration()
        self.configuration.host = 'http://10.10.63.105:9090/v1'
        self.api_instance = SensorsApi(openadk.ApiClient(self.configuration))  # noqa: E501

    def tearDown(self):
        pass

    def test_get_sensors_environment(self):
        """Test case for get_sensors_environment

        Get enviornment sensor's value  # noqa: E501
        """
        ret = self.api_instance.get_sensors_environment()   # 返回SensorsEnvironmentValueResponse对象
        self.assertEqual(ret.code, 0, ret)
        self.assertEqual(len(ret.data.environment), 0, ret)

    def test_get_sensors_gyro(self):
        """Test case for get_sensors_gyro

        Get gyroscope sensor's value  # noqa: E501
        """
        ret = self.api_instance.get_sensors_gyro()  # 返回SensorsGyroValueResponse对象
        self.assertEqual(ret.code, 0, ret)
        self.assertEqual(len(ret.data.gyro), 1, ret)

    def test_get_sensors_infrared(self):
        """Test case for get_sensors_infrared

        Get infrared sensor's value  # noqa: E501
        """
        ret = self.api_instance.get_sensors_infrared()  # 返回SensorsInfraredValueResponse对象
        self.assertEqual(ret.code, 0, ret)
        self.assertEqual(len(ret.data.infrared), 0, ret)

    def test_get_sensors_list(self):
        """Test case for get_sensors_list

        Get all sensors' list  # noqa: E501
        """
        ret = self.api_instance.get_sensors_list()  # 返回SensorsListResponse对象
        self.assertEqual(ret.code, 0, ret)
        self.assertEqual(len(ret.data.sensors), 1, ret)

    def test_get_sensors_pressure(self):
        """Test case for get_sensors_pressure

        Get pressure sensor's value  # noqa: E501
        """
        ret = self.api_instance.get_sensors_pressure()  # 返回SensorsPressureValueResponse对象
        self.assertEqual(ret.code, 0, ret)
        self.assertEqual(len(ret.data.pressure), 0, ret)

    def test_get_sensors_touch(self):
        """Test case for get_sensors_touch

        Get touch sensor's value  # noqa: E501
        """
        ret = self.api_instance.get_sensors_touch()  # 返回SensorsTouchValueResponse对象
        self.assertEqual(ret.code, 0, ret)
        self.assertEqual(len(ret.data.touch), 0, ret)

    def test_get_sensors_ultrasonic(self):
        """Test case for get_sensors_ultrasonic

        Get ultrasonic sensor's value  # noqa: E501
        """
        ret = self.api_instance.get_sensors_ultrasonic()    # 返回SensorsUltrasonicValueResponse对象
        self.assertEqual(ret.code, 0, ret)
        self.assertEqual(len(ret.data.ultrasonic), 0, ret)

    def test_put_sensors(self):
        """Test case for put_sensors

        Calibrate sensor or change sensor's I2C address  # noqa: E501
        """
        ret = self.api_instance.get_sensors_gyro()
        self.assertEqual(ret.code, 0, ret)
        gyro_id = ret.data.gyro[0].id

        sensor = SensorsParameter(type='gyro', id=gyro_id, value=0)
        body = SensorsOperationRequest(operation='calibrate', sensor=sensor)
        ret = self.api_instance.put_sensors(body=body)
        self.assertEqual(ret.code, 0, ret)


if __name__ == '__main__':
    unittest.main()
