from pydantic import SerializeAsAny
from amis.function.action import Action
from amis.types import *


class ButtonToolbar(AmisNode):
    """
    Button-Toolbar 按钮工具栏

    默认按钮会独占一行，如果想让多个按钮并排方式，可以使用 button-toolbar 组件包裹起来，另外还有能用 button-group 来在展现上更紧凑。
    """

    type: str = "button-toolbar"
    """指定为 ButtonToolbar 组件"""
    buttons: SerializeAsAny[List[Action]]
    """按钮组"""