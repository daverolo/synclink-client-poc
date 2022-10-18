# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_block_headers_response_data_inner_header import GetBlockHeadersResponseDataInnerHeader


class GetBlockHeadersResponseDataInner(BaseModel):
    """GetBlockHeadersResponseDataInner - a model defined in OpenAPI

        root: The root of this GetBlockHeadersResponseDataInner [Optional].
        canonical: The canonical of this GetBlockHeadersResponseDataInner [Optional].
        header: The header of this GetBlockHeadersResponseDataInner [Optional].
    """

    root: Optional[str] = Field(alias="root", default=None)
    canonical: Optional[bool] = Field(alias="canonical", default=None)
    header: Optional[GetBlockHeadersResponseDataInnerHeader] = Field(alias="header", default=None)

    @validator("root")
    def root_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{64}$", value)
        return value

GetBlockHeadersResponseDataInner.update_forward_refs()
