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
class AwsEcsCapacityprovider(BaseModel):
    AutoScalingGroupProvider: Optional["_AutoScalingGroupProvider"]
    Tags: Optional[Any]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEcsCapacityprovider"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEcsCapacityprovider"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AutoScalingGroupProvider=AutoScalingGroupProvider._deserialize(json_data.get("AutoScalingGroupProvider")),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEcsCapacityprovider = AwsEcsCapacityprovider


@dataclass
class AutoScalingGroupProvider(BaseModel):
    ManagedScaling: Optional["_ManagedScaling"]
    AutoScalingGroupArn: Optional[str]
    ManagedTerminationProtection: Optional[str]
    ManagedDraining: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutoScalingGroupProvider"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoScalingGroupProvider"]:
        if not json_data:
            return None
        return cls(
            ManagedScaling=ManagedScaling._deserialize(json_data.get("ManagedScaling")),
            AutoScalingGroupArn=json_data.get("AutoScalingGroupArn"),
            ManagedTerminationProtection=json_data.get("ManagedTerminationProtection"),
            ManagedDraining=json_data.get("ManagedDraining"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoScalingGroupProvider = AutoScalingGroupProvider


@dataclass
class ManagedScaling(BaseModel):
    Status: Optional[str]
    MinimumScalingStepSize: Optional[int]
    InstanceWarmupPeriod: Optional[int]
    TargetCapacity: Optional[int]
    MaximumScalingStepSize: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ManagedScaling"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagedScaling"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
            MinimumScalingStepSize=json_data.get("MinimumScalingStepSize"),
            InstanceWarmupPeriod=json_data.get("InstanceWarmupPeriod"),
            TargetCapacity=json_data.get("TargetCapacity"),
            MaximumScalingStepSize=json_data.get("MaximumScalingStepSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagedScaling = ManagedScaling


@dataclass
class Tag(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


