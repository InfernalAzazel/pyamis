from typing import Optional
from amis.types import *


class Container(AmisNode):
    """容器组件"""

    type: str = 'container'
    """指定为 container 渲染器"""
    className: Optional[str] = None
    """外层 Dom 的类名"""
    bodyClassName: Optional[str] = None
    """容器内容区的类名"""
    wrapperComponent: Optional[str] = 'div'
    """容器标签名"""
    style: Optional[str] = None
    """自定义样式"""
    body: Optional[SchemaNode] = None
    """容器内容"""
