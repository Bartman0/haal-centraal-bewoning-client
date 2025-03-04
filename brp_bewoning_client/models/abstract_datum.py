# coding: utf-8

"""
    BRP bewoning

    API voor het raadplegen van de (historische) bewoning van een adres. 

    The version of the OpenAPI document: 2.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from importlib import import_module
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from brp_bewoning_client.models.volledige_datum import VolledigeDatum
    from brp_bewoning_client.models.datum_onbekend import DatumOnbekend
    from brp_bewoning_client.models.jaar_datum import JaarDatum
    from brp_bewoning_client.models.jaar_maand_datum import JaarMaandDatum

class AbstractDatum(BaseModel):
    """
    AbstractDatum
    """ # noqa: E501
    type: StrictStr
    lang_formaat: Annotated[str, Field(strict=True)] = Field(alias="langFormaat")
    __properties: ClassVar[List[str]] = ["type", "langFormaat"]

    @field_validator('lang_formaat')
    def lang_formaat_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-z0-9 ]{1,17}$", value):
            raise ValueError(r"must validate the regular expression /^[a-z0-9 ]{1,17}$/")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'type'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'Datum': 'VolledigeDatum','DatumOnbekend': 'DatumOnbekend','JaarDatum': 'JaarDatum','JaarMaandDatum': 'JaarMaandDatum'
    }

    @classmethod
    def get_discriminator_value(cls, obj: Dict[str, Any]) -> Optional[str]:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Union[VolledigeDatum, DatumOnbekend, JaarDatum, JaarMaandDatum]]:
        """Create an instance of AbstractDatum from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[VolledigeDatum, DatumOnbekend, JaarDatum, JaarMaandDatum]]:
        """Create an instance of AbstractDatum from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'VolledigeDatum':
            return import_module("brp_bewoning_client.models.volledige_datum").VolledigeDatum.from_dict(obj)
        if object_type ==  'DatumOnbekend':
            return import_module("brp_bewoning_client.models.datum_onbekend").DatumOnbekend.from_dict(obj)
        if object_type ==  'JaarDatum':
            return import_module("brp_bewoning_client.models.jaar_datum").JaarDatum.from_dict(obj)
        if object_type ==  'JaarMaandDatum':
            return import_module("brp_bewoning_client.models.jaar_maand_datum").JaarMaandDatum.from_dict(obj)

        raise ValueError("AbstractDatum failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


