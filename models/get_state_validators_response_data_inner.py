# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_state_validators_response_data_inner_validator import GetStateValidatorsResponseDataInnerValidator


class GetStateValidatorsResponseDataInner(BaseModel):
    """GetStateValidatorsResponseDataInner - a model defined in OpenAPI

        index: The index of this GetStateValidatorsResponseDataInner [Optional].
        balance: The balance of this GetStateValidatorsResponseDataInner [Optional].
        status: The status of this GetStateValidatorsResponseDataInner [Optional].
        validator: The validator of this GetStateValidatorsResponseDataInner [Optional].
    """

    index: Optional[str] = Field(alias="index", default=None)
    balance: Optional[str] = Field(alias="balance", default=None)
    status: Optional[str] = Field(alias="status", default=None)
    validator: Optional[GetStateValidatorsResponseDataInnerValidator] = Field(alias="validator", default=None)

GetStateValidatorsResponseDataInner.update_forward_refs()
