# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GetStateValidatorsResponseDataInnerValidator(BaseModel):
    """GetStateValidatorsResponseDataInnerValidator - a model defined in OpenAPI

        pubkey: The pubkey of this GetStateValidatorsResponseDataInnerValidator [Optional].
        withdrawal_credentials: The withdrawal_credentials of this GetStateValidatorsResponseDataInnerValidator [Optional].
        effective_balance: The effective_balance of this GetStateValidatorsResponseDataInnerValidator [Optional].
        slashed: The slashed of this GetStateValidatorsResponseDataInnerValidator [Optional].
        activation_eligibility_epoch: The activation_eligibility_epoch of this GetStateValidatorsResponseDataInnerValidator [Optional].
        activation_epoch: The activation_epoch of this GetStateValidatorsResponseDataInnerValidator [Optional].
        exit_epoch: The exit_epoch of this GetStateValidatorsResponseDataInnerValidator [Optional].
        withdrawable_epoch: The withdrawable_epoch of this GetStateValidatorsResponseDataInnerValidator [Optional].
    """

    pubkey: Optional[str] = Field(alias="pubkey", default=None)
    withdrawal_credentials: Optional[str] = Field(alias="withdrawal_credentials", default=None)
    effective_balance: Optional[str] = Field(alias="effective_balance", default=None)
    slashed: Optional[bool] = Field(alias="slashed", default=None)
    activation_eligibility_epoch: Optional[str] = Field(alias="activation_eligibility_epoch", default=None)
    activation_epoch: Optional[str] = Field(alias="activation_epoch", default=None)
    exit_epoch: Optional[str] = Field(alias="exit_epoch", default=None)
    withdrawable_epoch: Optional[str] = Field(alias="withdrawable_epoch", default=None)

    @validator("pubkey")
    def pubkey_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{96}$", value)
        return value

GetStateValidatorsResponseDataInnerValidator.update_forward_refs()
