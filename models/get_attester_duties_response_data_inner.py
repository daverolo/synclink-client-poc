# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GetAttesterDutiesResponseDataInner(BaseModel):
    """GetAttesterDutiesResponseDataInner - a model defined in OpenAPI

        pubkey: The pubkey of this GetAttesterDutiesResponseDataInner [Optional].
        validator_index: The validator_index of this GetAttesterDutiesResponseDataInner [Optional].
        committee_index: The committee_index of this GetAttesterDutiesResponseDataInner [Optional].
        committee_length: The committee_length of this GetAttesterDutiesResponseDataInner [Optional].
        committees_at_slot: The committees_at_slot of this GetAttesterDutiesResponseDataInner [Optional].
        validator_committee_index: The validator_committee_index of this GetAttesterDutiesResponseDataInner [Optional].
        slot: The slot of this GetAttesterDutiesResponseDataInner [Optional].
    """

    pubkey: Optional[str] = Field(alias="pubkey", default=None)
    validator_index: Optional[str] = Field(alias="validator_index", default=None)
    committee_index: Optional[str] = Field(alias="committee_index", default=None)
    committee_length: Optional[str] = Field(alias="committee_length", default=None)
    committees_at_slot: Optional[str] = Field(alias="committees_at_slot", default=None)
    validator_committee_index: Optional[str] = Field(alias="validator_committee_index", default=None)
    slot: Optional[str] = Field(alias="slot", default=None)

    @validator("pubkey")
    def pubkey_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{96}$", value)
        return value

GetAttesterDutiesResponseDataInner.update_forward_refs()
