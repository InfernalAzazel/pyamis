from typing import Optional
from amis.types import *

# https://baidu.github.io/amis/zh-CN/components/iframe#%E5%B1%9E%E6%80%A7%E8%A1%A8

class Iframe(AmisNode):
    """
    Iframe

    内嵌外部站点，可用 iframe 来实现。
    """

    type: str = "iframe"
    """指定为 iFrame 渲染器"""
    className: Optional[str] = None
    """iFrame 的类名"""
    frameBorder: Optional[list] = None
    """frameBorder"""
    style: Optional[dict] = None
    """样式对象"""
    src: Optional[str] = None
    """iframe 地址"""
    allow: Optional[str] = None
    """	allow 配置"""
    sandbox: Optional[str] = None
    """sandbox 配置"""
    referrerpolicy: Optional[str] = None
    """referrerpolicy 配置"""
    height: Union[int, str] = '100%'
    """iframe 高度"""
    width: Union[int, str] = '100%'
    """iframe 宽度"""