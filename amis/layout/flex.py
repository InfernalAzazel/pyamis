from typing import Optional

from pydantic import SerializeAsAny

from amis.types import *


class Flex(AmisNode):
    """布局"""

    type: str = "flex"
    """指定为 Flex 渲染器"""
    className: Optional[str] = None
    """css 类名"""
    justify: Optional[str] = None
    '''"start", "flex-start", "center", "end", "flex-end", "space-around", "space-between", "space-evenly"'''
    alignItems: Optional[str] = None
    '''对齐,选填: "stretch", "start", "flex-start", "flex-end", "end", "center", "baseline"'''
    style: Optional[dict] = None
    """自定义样式"""
    items: SerializeAsAny[Optional[List[SchemaNode]]] = None
    """组件列表"""
