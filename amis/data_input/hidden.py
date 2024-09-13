from typing import Optional
from amis.types import *


class Hidden(AmisNode):
    """"
    Hidden 隐藏字段

    参考： https://aisuda.bce.baidu.com/amis/zh-CN/components/form/hidden
    """
    type: Optional[str] = 'hidden'
    name: Optional[str]= None
    """对应字段名称"""
    value: Optional[int] = None
    """默认值"""