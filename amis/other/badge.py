from typing import Optional

from amis.types import *

# https://baidu.github.io/amis/zh-CN/components/badge#%E5%B1%9E%E6%80%A7%E8%A1%A8

class Badge(AmisNode):
    """Subscript"""

    mode: str = "dot"  # Corner type, can be dot/text/ribbon
    text: Union[int, str, None] = None  # Corner text, supports strings and numbers, invalid when mode='dot'
    size: Optional[int] = None  # Angular size
    level: Optional[
        str] = None  # The level of the corner label, which can be info/success/warning/danger, after setting the
    # background color of the corner label is different
    overflowCount: Optional[int] = None  # 99 # Set the capped number value
    position: Optional[str] = None  # "top-right" # Corner position, can be top-right/top-left/bottom-right/bottom-left
    offset: Optional[
        int] = None  # The position of the corner label, the priority is greater than the position, when the
    # offset is set, the position is positioned as the top-right reference number[top, left]
    className: Optional[str] = None  # The class name of the outer dom
    animation: Optional[bool] = None  # whether the corner icon displays animation
    style: Optional[dict] = None  # Custom style for corner labels
    visibleOn: Optional[Expression] = None  # Controls the display and hiding of corner labels