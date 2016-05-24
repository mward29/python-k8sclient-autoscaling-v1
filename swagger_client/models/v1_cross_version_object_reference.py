# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class V1CrossVersionObjectReference(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        V1CrossVersionObjectReference - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'kind': 'str',
            'name': 'str',
            'api_version': 'str'
        }

        self.attribute_map = {
            'kind': 'kind',
            'name': 'name',
            'api_version': 'apiVersion'
        }

        self._kind = None
        self._name = None
        self._api_version = None

    @property
    def kind(self):
        """
        Gets the kind of this V1CrossVersionObjectReference.
        Kind of the referent; More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds\"

        :return: The kind of this V1CrossVersionObjectReference.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1CrossVersionObjectReference.
        Kind of the referent; More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds\"

        :param kind: The kind of this V1CrossVersionObjectReference.
        :type: str
        """
        self._kind = kind

    @property
    def name(self):
        """
        Gets the name of this V1CrossVersionObjectReference.
        Name of the referent; More info: http://releases.k8s.io/HEAD/docs/user-guide/identifiers.md#names

        :return: The name of this V1CrossVersionObjectReference.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1CrossVersionObjectReference.
        Name of the referent; More info: http://releases.k8s.io/HEAD/docs/user-guide/identifiers.md#names

        :param name: The name of this V1CrossVersionObjectReference.
        :type: str
        """
        self._name = name

    @property
    def api_version(self):
        """
        Gets the api_version of this V1CrossVersionObjectReference.
        API version of the referent

        :return: The api_version of this V1CrossVersionObjectReference.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1CrossVersionObjectReference.
        API version of the referent

        :param api_version: The api_version of this V1CrossVersionObjectReference.
        :type: str
        """
        self._api_version = api_version

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

