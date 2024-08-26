from typing import Optional
from amis.types import *

# https://aisuda.bce.baidu.com/amis/zh-CN/components/remark#%E5%B1%9E%E6%80%A7%E8%A1%A8

RemarkT = Union[str, "Remark"]


class Remark(AmisNode):
    """mark"""

    type: str = "remark"
    className: Optional[str] = None
    """外层 CSS 类名"""
    content: Optional[str] = None
    """提示文本"""
    placement: Optional[str] = None
    """弹出位置"""
    trigger: Optional[str] = None
    """触发条件, 默认: ['hover', 'focus']"""
    icon: Optional[str] = None
    """图标: fa fa-question-circle"""
    shape: Optional[str] = None
    """	图标形状"""
