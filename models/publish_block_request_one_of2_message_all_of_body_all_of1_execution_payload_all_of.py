# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class PublishBlockRequestOneOf2MessageAllOfBodyAllOf1ExecutionPayloadAllOf(BaseModel):
    """PublishBlockRequestOneOf2MessageAllOfBodyAllOf1ExecutionPayloadAllOf - a model defined in OpenAPI

        parent_hash: The parent_hash of this PublishBlockRequestOneOf2MessageAllOfBodyAllOf1ExecutionPayloadAllOf [Optional].
        fee_recipient: The fee_recipient of this PublishBlockRequestOneOf2MessageAllOfBodyAllOf1ExecutionPayloadAllOf [Optional].
        state_root: The state_root of this PublishBlockRequestOneOf2MessageAllOfBodyAllOf1ExecutionPayloadAllOf [Optional].
        receipts_root: The receipts_root of this PublishBlockRequestOneOf2MessageAllOfBodyAllOf1ExecutionPayloadAllOf [Optional].
        logs_bloom: The logs_bloom of this PublishBlockRequestOneOf2MessageAllOfBodyAllOf1ExecutionPayloadAllOf [Optional].
        prev_randao: The prev_randao of this PublishBlockRequestOneOf2MessageAllOfBodyAllOf1ExecutionPayloadAllOf [Optional].
        block_number: The block_number of this PublishBlockRequestOneOf2MessageAllOfBodyAllOf1ExecutionPayloadAllOf [Optional].
        gas_limit: The gas_limit of this PublishBlockRequestOneOf2MessageAllOfBodyAllOf1ExecutionPayloadAllOf [Optional].
        gas_used: The gas_used of this PublishBlockRequestOneOf2MessageAllOfBodyAllOf1ExecutionPayloadAllOf [Optional].
        timestamp: The timestamp of this PublishBlockRequestOneOf2MessageAllOfBodyAllOf1ExecutionPayloadAllOf [Optional].
        extra_data: The extra_data of this PublishBlockRequestOneOf2MessageAllOfBodyAllOf1ExecutionPayloadAllOf [Optional].
        base_fee_per_gas: The base_fee_per_gas of this PublishBlockRequestOneOf2MessageAllOfBodyAllOf1ExecutionPayloadAllOf [Optional].
        block_hash: The block_hash of this PublishBlockRequestOneOf2MessageAllOfBodyAllOf1ExecutionPayloadAllOf [Optional].
    """

    parent_hash: Optional[str] = Field(alias="parent_hash", default=None)
    fee_recipient: Optional[str] = Field(alias="fee_recipient", default=None)
    state_root: Optional[str] = Field(alias="state_root", default=None)
    receipts_root: Optional[str] = Field(alias="receipts_root", default=None)
    logs_bloom: Optional[str] = Field(alias="logs_bloom", default=None)
    prev_randao: Optional[str] = Field(alias="prev_randao", default=None)
    block_number: Optional[str] = Field(alias="block_number", default=None)
    gas_limit: Optional[str] = Field(alias="gas_limit", default=None)
    gas_used: Optional[str] = Field(alias="gas_used", default=None)
    timestamp: Optional[str] = Field(alias="timestamp", default=None)
    extra_data: Optional[str] = Field(alias="extra_data", default=None)
    base_fee_per_gas: Optional[str] = Field(alias="base_fee_per_gas", default=None)
    block_hash: Optional[str] = Field(alias="block_hash", default=None)

    @validator("parent_hash")
    def parent_hash_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{64}$", value)
        return value

    @validator("fee_recipient")
    def fee_recipient_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{40}$", value)
        return value

    @validator("state_root")
    def state_root_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{64}$", value)
        return value

    @validator("receipts_root")
    def receipts_root_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{64}$", value)
        return value

    @validator("logs_bloom")
    def logs_bloom_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{512}$", value)
        return value

    @validator("prev_randao")
    def prev_randao_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{64}$", value)
        return value

    @validator("extra_data")
    def extra_data_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{0,64}$", value)
        return value

    @validator("block_hash")
    def block_hash_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{64}$", value)
        return value

PublishBlockRequestOneOf2MessageAllOfBodyAllOf1ExecutionPayloadAllOf.update_forward_refs()
