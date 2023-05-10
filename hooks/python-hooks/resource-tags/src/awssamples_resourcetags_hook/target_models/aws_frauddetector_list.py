# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass

from cloudformation_cli_python_lib.interface import BaseModel
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

import sys
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class AwsFrauddetectorList(BaseModel):
    Arn: Optional[str]
    Name: Optional[str]
    Description: Optional[str]
    VariableType: Optional[str]
    CreatedTime: Optional[str]
    LastUpdatedTime: Optional[str]
    Tags: Optional[Any]
    Elements: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsFrauddetectorList"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsFrauddetectorList"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            VariableType=json_data.get("VariableType"),
            CreatedTime=json_data.get("CreatedTime"),
            LastUpdatedTime=json_data.get("LastUpdatedTime"),
            Tags=json_data.get("Tags"),
            Elements=json_data.get("Elements"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsFrauddetectorList = AwsFrauddetectorList


@dataclass
class Tag(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


