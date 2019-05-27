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
from openadk import Name, VisionsDeleteTags, VisionsGetRequest, VisionsPhoto
from openadk.api.visions_api import VisionsApi  # noqa: E501
from openadk.rest import ApiException
from pprint import pprint
import time

from openadk.models.visions_put_tags import VisionsPutTags
from openadk.models.visions_stream import VisionsStream
from openadk.models.visions_task import VisionsTask


class TestVisionsApi(unittest.TestCase):
    """VisionsApi unit test stubs"""

    def setUp(self):
        self.configuration = openadk.Configuration()
        self.configuration.host = 'http://10.10.63.105:9090/v1'
        self.api_instance = VisionsApi(openadk.ApiClient(self.configuration))  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_vision_photo(self):
        """Test case for delete_vision_photo

        Delete a photo based the name  # noqa: E501
        """
        # 删除存在的照片
        body = VisionsPhoto(resolution="1280x800")
        ret = self.api_instance.post_vision_photo(body=body)  # 返回VisionsPhotoResponse对象
        self.assertEqual(ret.code, 0, ret)
        name = ret.data.name
        body = Name(name=name)
        ret = self.api_instance.delete_vision_photo(body=body)
        self.assertEqual(ret.code, 0, ret)

        # 删除不存在（已删除）的照片
        body = Name(name=name)
        ret = self.api_instance.delete_vision_photo(body=body)
        self.assertEqual(ret.code, 0, ret)

    def test_delete_vision_photo_samples(self):
        """Test case for delete_vision_photo_samples

        Delete the uploaded sample  # noqa: E501
        """
        # 删除存在的样本
        photo_dir = 'files/'
        body = VisionsPhoto(resolution="1280x800")
        ret = self.api_instance.post_vision_photo(body=body)  # 返回VisionsPhotoResponse对象
        self.assertEqual(ret.code, 0, ret)
        photo_name = ret.data.name
        photo_path = photo_dir + photo_name

        ret = self.api_instance.get_visions_photos(body=photo_name, _preload_content=False)
        self.assertEqual(ret.status, 200, ret)
        with open(photo_path, 'wb') as fwrite:
            fwrite.write(ret.data)  # 照片的二进制数据在response的data域里

        ret = self.api_instance.post_visions_photo_samples(file=photo_path)
        self.assertEqual(ret.code, 0, ret)

        body = Name(name=photo_name)
        ret = self.api_instance.delete_vision_photo_samples(body=body)
        self.assertEqual(ret.code, 0, ret)

        # 删除不存在（已删除）的样本
        body = Name(name=photo_name)
        ret = self.api_instance.delete_vision_photo_samples(body=body)
        self.assertEqual(ret.code, 0, ret)

    def test_delete_visions_streams(self):
        """Test case for delete_visions_streams

        Turn off the web stream for the camera  # noqa: E501
        """
        ret = self.api_instance.delete_visions_streams()
        self.assertEqual(ret.code, 0, ret)

    def test_delete_visions_tags(self):
        """Test case for delete_visions_tags

        Delete a sample's tag based the tag name  # noqa: E501
        """
        # 删除存在的样本标签
        photo_dir = 'files/'
        body = VisionsPhoto(resolution="1280x800")
        ret = self.api_instance.post_vision_photo(body=body)  # 返回VisionsPhotoResponse对象
        self.assertEqual(ret.code, 0, ret)
        photo_name = ret.data.name
        photo_path = photo_dir + photo_name

        ret = self.api_instance.get_visions_photos(body=photo_name, _preload_content=False)
        self.assertEqual(ret.status, 200, ret)
        with open(photo_path, 'wb') as fwrite:
            fwrite.write(ret.data)  # 照片的二进制数据在response的data域里

        ret = self.api_instance.post_visions_photo_samples(file=photo_path)
        self.assertEqual(ret.code, 0, ret)

        tags = str(int(time.time()))
        body = VisionsPutTags(tags=tags, resources=[photo_name])
        ret = self.api_instance.put_visions_tags(body=body)
        self.assertEqual(ret.code, 0, ret)

        body = VisionsDeleteTags(tags=tags)
        ret = self.api_instance.delete_visions_tags(body=body)
        self.assertEqual(ret.code, 0, ret)

        # 删除不存在（已删除）的样本标签
        body = VisionsDeleteTags(tags=tags)
        ret = self.api_instance.delete_visions_tags(body=body)
        self.assertEqual(ret.code, 0, ret)

    def test_get_photo_samples(self):
        """Test case for get_photo_samples

        Get all the uploaded photo samples  # noqa: E501
        """
        photo_dir = 'files/'
        # 拍一张照片
        body = VisionsPhoto(resolution="1280x800")
        ret = self.api_instance.post_vision_photo(body=body)    # 返回VisionsPhotoResponse对象
        self.assertEqual(ret.code, 0, ret)
        photo_name = ret.data.name
        photo_path = photo_dir + photo_name

        # 获取指定照片
        ret = self.api_instance.get_visions_photos(body=photo_name, _preload_content=False)
        self.assertEqual(ret.status, 200, ret)
        with open(photo_path, 'wb') as fwrite:
            fwrite.write(ret.data)  # 照片的二进制数据在response的data域里

        # 上传样本
        ret = self.api_instance.post_visions_photo_samples(file=photo_path)
        self.assertEqual(ret.code, 0, ret)

        # 获取上传样本列表
        ret = self.api_instance.get_photo_samples()  # 返回VisionsPhotoListResponse对象
        self.assertEqual(ret.code, 0, ret)
        found = False
        for name in ret.data:
            if name.name == photo_name:
                found = True
                break
        self.assertEqual(found, True, ret)

    def test_get_vision(self):
        """Test case for get_vision

        Get compute vision result  # noqa: E501
        """
        type_list = ['tracking', 'recognition', 'gender', 'age_group', 'quantity']

        for type in type_list:
            ret = self.api_instance.get_vision(option='face', type=type)  # 返回VisionsGetResponse对象
            self.assertEqual(ret.code, 0, ret)
            self.assertEqual(ret.type, type, ret)
            self.assertEqual(ret.status, 'idle', ret)

        ret = self.api_instance.get_vision(option='color', type='color_detect')
        self.assertEqual(ret.code, 0, ret)
        self.assertEqual(ret.type, 'color_detect', ret)
        self.assertEqual(ret.status, 'idle', ret)

    def test_get_visions_photos(self):
        """Test case for get_visions_photos

        Get a specific photo based the name  # noqa: E501
        """
        photo_dir = 'files/'
        # 拍一张照片
        body = VisionsPhoto(resolution="1280x800")
        ret = self.api_instance.post_vision_photo(body=body)  # 返回VisionsPhotoResponse对象
        self.assertEqual(ret.code, 0, ret)
        photo_name = ret.data.name
        photo_path = photo_dir + photo_name

        # 获取指定照片
        ret = self.api_instance.get_visions_photos(body=photo_name, _preload_content=False)
        self.assertEqual(ret.status, 200, ret)
        with open(photo_path, 'wb') as fwrite:
            fwrite.write(ret.data)  # 照片的二进制数据在response的data域里
        with open(photo_path, 'rb') as fread:
            self.assertNotEqual(fread.read(), b'', ret)

    def test_get_visions_photos_lists(self):
        """Test case for get_visions_photos_lists

        Get the photo's list  # noqa: E501
        """
        # 拍一张照片
        body = VisionsPhoto(resolution="1280x800")
        ret = self.api_instance.post_vision_photo(body=body)  # 返回VisionsPhotoResponse对象
        self.assertEqual(ret.code, 0, ret)
        photo_name = ret.data.name

        # 获取拍照列表
        ret = self.api_instance.get_visions_photos_lists()  # 返回VisionsPhotoListResponse对象
        self.assertEqual(ret.code, 0, ret)
        found = False
        for name in ret.data:
            if name.name == photo_name:
                found = True
                break
        self.assertEqual(found, True, ret)

    def test_get_visions_tags(self):
        """Test case for get_visions_tags

        Get all the tag list  # noqa: E501
        """
        photo_dir = 'files/'
        # 拍一张照片
        body = VisionsPhoto(resolution="1280x800")
        ret = self.api_instance.post_vision_photo(body=body)  # 返回VisionsPhotoResponse对象
        self.assertEqual(ret.code, 0, ret)
        photo_name = ret.data.name
        photo_path = photo_dir + photo_name

        # 获取指定照片
        ret = self.api_instance.get_visions_photos(body=photo_name, _preload_content=False)
        self.assertEqual(ret.status, 200, ret)
        with open(photo_path, 'wb') as fwrite:
            fwrite.write(ret.data)  # 照片的二进制数据在response的data域里

        # 上传样本
        ret = self.api_instance.post_visions_photo_samples(file=photo_path)
        self.assertEqual(ret.code, 0, ret)

        # 设置样本标签
        body = VisionsPutTags(tags=str(int(time.time())), resources=[photo_name])
        ret = self.api_instance.put_visions_tags(body=body)
        self.assertEqual(ret.code, 0, ret)

        # 获取已设置标签列表
        ret = self.api_instance.get_visions_tags()  # 返回VisionsTagsResponse对象
        self.assertEqual(ret.code, 0, ret)
        found = False
        for tag in ret.data:
            if tag.tags == body.tags and tag.resources == body.resources:
                found = True
                break
        self.assertEqual(found, True, ret)

    def test_post_vision_photo(self):
        """Test case for post_vision_photo

        Take a photo  # noqa: E501
        """
        body = VisionsPhoto(resolution="1280x800")
        ret = self.api_instance.post_vision_photo(body=body)  # 返回VisionsPhotoResponse对象
        self.assertEqual(ret.code, 0, ret)
        self.assertEqual(ret.data.name.endswith('jpg'), True, ret)

    def test_post_visions_photo_samples(self):
        """Test case for post_visions_photo_samples

        Upload photo sample  # noqa: E501
        """
        photo_dir = 'files/'
        # 拍一张照片
        body = VisionsPhoto(resolution="1280x800")
        ret = self.api_instance.post_vision_photo(body=body)  # 返回VisionsPhotoResponse对象
        self.assertEqual(ret.code, 0, ret)
        photo_name = ret.data.name
        photo_path = photo_dir + photo_name

        # 获取指定照片
        ret = self.api_instance.get_visions_photos(body=photo_name, _preload_content=False)
        self.assertEqual(ret.status, 200, ret)
        with open(photo_path, 'wb') as fwrite:
            fwrite.write(ret.data)  # 照片的二进制数据在response的data域里

        # 上传样本
        ret = self.api_instance.post_visions_photo_samples(file=photo_path)
        self.assertEqual(ret.code, 0, ret)

    def test_post_visions_streams(self):
        """Test case for post_visions_streams

        Turn on the web stream for the camera  # noqa: E501
        """
        body = VisionsStream(resolution="1280x800")
        ret = self.api_instance.post_visions_streams(body=body)
        self.assertEqual(ret.code, 0, ret)
        time.sleep(3.0)
        ret = self.api_instance.delete_visions_streams()
        self.assertEqual(ret.code, 0, ret)

    def test_put_visions(self):
        """Test case for put_visions

        Start or stop a compute vision task  # noqa: E501
        """
        operation_list = ['start', 'stop']
        type_list = ['tracking', 'recognition', 'gender', 'age_group', 'quantity']
        for type in type_list:
            for operation in operation_list:
                body = VisionsTask(type=type, operation=operation, option='face', timestamp=int(time.time()))
                ret = self.api_instance.put_visions(body=body)
                self.assertEqual(ret.code, 0, ret)
                time.sleep(1.0)

        for operation in operation_list:
            body = VisionsTask(type='color_detect', operation=operation, option='color', timestamp=int(time.time()))
            ret = self.api_instance.put_visions(body=body)
            self.assertEqual(ret.code, 0, ret)
            time.sleep(1.0)

    def test_put_visions_tags(self):
        """Test case for put_visions_tags

        Set the sample's tag  # noqa: E501
        """
        photo_dir = 'files/'
        # 拍一张照片
        body = VisionsPhoto(resolution="1280x800")
        ret = self.api_instance.post_vision_photo(body=body)  # 返回VisionsPhotoResponse对象
        self.assertEqual(ret.code, 0, ret)
        photo_name = ret.data.name
        photo_path = photo_dir + photo_name

        # 获取指定照片
        ret = self.api_instance.get_visions_photos(body=photo_name, _preload_content=False)
        self.assertEqual(ret.status, 200, ret)
        with open(photo_path, 'wb') as fwrite:
            fwrite.write(ret.data)  # 照片的二进制数据在response的data域里

        # 上传样本
        ret = self.api_instance.post_visions_photo_samples(file=photo_path)
        self.assertEqual(ret.code, 0, ret)

        # 设置样本标签
        body = VisionsPutTags(tags=str(int(time.time())), resources=[photo_name])
        ret = self.api_instance.put_visions_tags(body=body)
        self.assertEqual(ret.code, 0, ret)


if __name__ == '__main__':
    unittest.main()
