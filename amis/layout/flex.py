from typing import Optional
from pydantic import SerializeAsAny
from amis.types import *


# https://aisuda.bce.baidu.com/amis/zh-CN/components/flex#%E5%B1%9E%E6%80%A7%E8%A1%A8
class Flex(AmisNode):
    """
    Flex 布局

    Flex 布局是基于 CSS Flex 实现的布局效果，
    它比 Grid 和 HBox 对子节点位置的可控性更强，
    比用 CSS 类的方式更易用，并且默认使用水平垂直居中的对齐。
    """

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
