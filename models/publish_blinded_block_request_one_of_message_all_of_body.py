# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.publish_blinded_block_request_one_of_message_all_of_body_all_of_execution_payload_header import PublishBlindedBlockRequestOneOfMessageAllOfBodyAllOfExecutionPayloadHeader
from models.publish_block_request_one_of1_message_all_of_body_sync_aggregate import PublishBlockRequestOneOf1MessageAllOfBodySyncAggregate
from models.publish_block_request_one_of_message_all_of_body_attestations_inner import PublishBlockRequestOneOfMessageAllOfBodyAttestationsInner
from models.publish_block_request_one_of_message_all_of_body_attester_slashings_inner import PublishBlockRequestOneOfMessageAllOfBodyAttesterSlashingsInner
from models.publish_block_request_one_of_message_all_of_body_deposits_inner import PublishBlockRequestOneOfMessageAllOfBodyDepositsInner
from models.publish_block_request_one_of_message_all_of_body_eth1_data import PublishBlockRequestOneOfMessageAllOfBodyEth1Data
from models.publish_block_request_one_of_message_all_of_body_proposer_slashings_inner import PublishBlockRequestOneOfMessageAllOfBodyProposerSlashingsInner
from models.publish_block_request_one_of_message_all_of_body_voluntary_exits_inner import PublishBlockRequestOneOfMessageAllOfBodyVoluntaryExitsInner


class PublishBlindedBlockRequestOneOfMessageAllOfBody(BaseModel):
    """PublishBlindedBlockRequestOneOfMessageAllOfBody - a model defined in OpenAPI

        randao_reveal: The randao_reveal of this PublishBlindedBlockRequestOneOfMessageAllOfBody [Optional].
        eth1_data: The eth1_data of this PublishBlindedBlockRequestOneOfMessageAllOfBody [Optional].
        graffiti: The graffiti of this PublishBlindedBlockRequestOneOfMessageAllOfBody [Optional].
        proposer_slashings: The proposer_slashings of this PublishBlindedBlockRequestOneOfMessageAllOfBody [Optional].
        attester_slashings: The attester_slashings of this PublishBlindedBlockRequestOneOfMessageAllOfBody [Optional].
        attestations: The attestations of this PublishBlindedBlockRequestOneOfMessageAllOfBody [Optional].
        deposits: The deposits of this PublishBlindedBlockRequestOneOfMessageAllOfBody [Optional].
        voluntary_exits: The voluntary_exits of this PublishBlindedBlockRequestOneOfMessageAllOfBody [Optional].
        sync_aggregate: The sync_aggregate of this PublishBlindedBlockRequestOneOfMessageAllOfBody [Optional].
        execution_payload_header: The execution_payload_header of this PublishBlindedBlockRequestOneOfMessageAllOfBody [Optional].
    """

    randao_reveal: Optional[str] = Field(alias="randao_reveal", default=None)
    eth1_data: Optional[PublishBlockRequestOneOfMessageAllOfBodyEth1Data] = Field(alias="eth1_data", default=None)
    graffiti: Optional[str] = Field(alias="graffiti", default=None)
    proposer_slashings: Optional[List[PublishBlockRequestOneOfMessageAllOfBodyProposerSlashingsInner]] = Field(alias="proposer_slashings", default=None)
    attester_slashings: Optional[List[PublishBlockRequestOneOfMessageAllOfBodyAttesterSlashingsInner]] = Field(alias="attester_slashings", default=None)
    attestations: Optional[List[PublishBlockRequestOneOfMessageAllOfBodyAttestationsInner]] = Field(alias="attestations", default=None)
    deposits: Optional[List[PublishBlockRequestOneOfMessageAllOfBodyDepositsInner]] = Field(alias="deposits", default=None)
    voluntary_exits: Optional[List[PublishBlockRequestOneOfMessageAllOfBodyVoluntaryExitsInner]] = Field(alias="voluntary_exits", default=None)
    sync_aggregate: Optional[PublishBlockRequestOneOf1MessageAllOfBodySyncAggregate] = Field(alias="sync_aggregate", default=None)
    execution_payload_header: Optional[PublishBlindedBlockRequestOneOfMessageAllOfBodyAllOfExecutionPayloadHeader] = Field(alias="execution_payload_header", default=None)

    @validator("graffiti")
    def graffiti_pattern(cls, value):
        assert value is not None and re.match(r"^0x[a-fA-F0-9]{64}$", value)
        return value

PublishBlindedBlockRequestOneOfMessageAllOfBody.update_forward_refs()