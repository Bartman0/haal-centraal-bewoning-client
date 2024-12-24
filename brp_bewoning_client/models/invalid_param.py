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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class InvalidParam(BaseModel):
    """
    Details over fouten in opgegeven parameters
    """ # noqa: E501
    type: Optional[StrictStr] = None
    name: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Naam van de parameter")
    code: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Systeemcode die het type fout aangeeft")
    reason: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Beschrijving van de fout op de parameterwaarde")
    __properties: ClassVar[List[str]] = ["type", "name", "code", "reason"]

    @field_validator('name')
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9\._]{1,30}$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\._]{1,30}$/")
        return value

    @field_validator('code')
    def code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9]{1,25}$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9]{1,25}$/")
        return value

    @field_validator('reason')
    def reason_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9\., ]{1,80}$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\., ]{1,80}$/")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of InvalidParam from a JSON string"""
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
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InvalidParam from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "name": obj.get("name"),
            "code": obj.get("code"),
            "reason": obj.get("reason")
        })
        return _obj


