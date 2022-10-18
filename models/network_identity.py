# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.get_network_identity_response_data_metadata import GetNetworkIdentityResponseDataMetadata


class NetworkIdentity(BaseModel):
    """NetworkIdentity - a model defined in OpenAPI

        peer_id: The peer_id of this NetworkIdentity [Optional].
        enr: The enr of this NetworkIdentity [Optional].
        p2p_addresses: The p2p_addresses of this NetworkIdentity [Optional].
        discovery_addresses: The discovery_addresses of this NetworkIdentity [Optional].
        metadata: The metadata of this NetworkIdentity [Optional].
    """

    peer_id: Optional[str] = Field(alias="peer_id", default=None)
    enr: Optional[str] = Field(alias="enr", default=None)
    p2p_addresses: Optional[List[str]] = Field(alias="p2p_addresses", default=None)
    discovery_addresses: Optional[List[str]] = Field(alias="discovery_addresses", default=None)
    metadata: Optional[GetNetworkIdentityResponseDataMetadata] = Field(alias="metadata", default=None)

NetworkIdentity.update_forward_refs()
