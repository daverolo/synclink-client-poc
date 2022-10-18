# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GetDepositContractResponseData(BaseModel):
    """GetDepositContractResponseData - a model defined in OpenAPI

        chain_id: The chain_id of this GetDepositContractResponseData [Optional].
        address: The address of this GetDepositContractResponseData [Optional].
    """

    chain_id: Optional[str] = Field(alias="chain_id", default=None)
    address: Optional[str] = Field(alias="address", default=None)

GetDepositContractResponseData.update_forward_refs()
