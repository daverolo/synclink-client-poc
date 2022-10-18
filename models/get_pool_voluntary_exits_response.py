# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_block_request_one_of_message_all_of_body_voluntary_exits_inner import PublishBlockRequestOneOfMessageAllOfBodyVoluntaryExitsInner


class GetPoolVoluntaryExitsResponse(BaseModel):
    """GetPoolVoluntaryExitsResponse - a model defined in OpenAPI

        data: The data of this GetPoolVoluntaryExitsResponse [Optional].
    """

    data: Optional[List[PublishBlockRequestOneOfMessageAllOfBodyVoluntaryExitsInner]] = Field(alias="data", default=None)

GetPoolVoluntaryExitsResponse.update_forward_refs()
