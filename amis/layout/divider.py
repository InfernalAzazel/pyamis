from typing import Optional

from amis.types import *


class Divider(AmisNode):
    """分割线组件"""

    type: str = "divider"
    """"divider" 指定为 分割线 渲染器"""
    className: Optional[str] = None
    """	外层 Dom 的类名"""
    lineStyle: Optional[str] = None
    """分割线的样式，支持dashed和solid"""
    direction: str = "horizontal"
    """分割线的方向，支持horizontal和vertical，版本:3.5.0"""
    color: Optional[str] = None
    """分割线的颜色，版本:3.5.0"""
    rotate: Optional[int] = None
    """分割线的旋转角度，版本:3.5.0"""
    title: Optional[SchemaNode] = None
    """分割线的标题，版本:3.5.0"""
    titleClassName: Optional[str] = None
    """分割线的标题类名，版本:3.5.0"""
    titlePosition: Optional[str] = 'center'
    """分割线的标题位置，支持left、center和right，版本:3.5.0"""
