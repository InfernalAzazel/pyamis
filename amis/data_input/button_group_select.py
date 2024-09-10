from typing import Optional

from amis.data_input import FormItem
from amis.types import *


class ButtonGroupSelect(FormItem):
    """Button group select"""

    type: str = "button-group-select"
    """指定为 button-group-select 渲染器"""
    vertical: Optional[bool] = None
    """
    - 是否使用垂直模式
    - 默认值：false
    """
    tiled: Optional[bool] = None
    """
    - 是否使用平铺模式
    - 默认值：false
    """
    btnLevel: LevelEnum = LevelEnum.default  # button style
    btnActiveLevel: LevelEnum = LevelEnum.default  # Check button style
    options: Optional[OptionsNode] = None  # option group
    source: Optional[API] = None  # dynamic group
    multiple: Optional[bool] = None  # Default False, multiple choice
    labelField: Optional[str] = None  # Default "label"
    valueField: Optional[str] = None  # Default "value"
    joinValues: Optional[bool] = None  # Default True
    extractValue: Optional[bool] = None  # Default False
    autoFill: Optional[dict] = None  # autofill