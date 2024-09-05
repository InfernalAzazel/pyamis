from amis.data_display import *
from amis.types import *

class TableRow2(AmisNode):
    """
    行配置属性表

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/table2#%E8%A1%8C%E9%85%8D%E7%BD%AE%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: Optional[Literal['checkbox', 'radio']] = None
    """
    - 指定单选还是多选
    - 默认值：'checkbox'
    """
    fixed: Optional[Literal['left','right']] = None
    """选择列是否固定，只能左侧固定"""
    keyField: Optional[str] = None
    """
    - 对应数据源的 key 值，默认是key，可指定为id、shortId等
    - 默认值：'key'
    """
    disableOn: Optional[str] = None
    """当前行是否可选择条件，要用 表达式"""
    selections: SerializeAsAny[Optional[TableSelections2]] = None
    """自定义筛选菜单，内置all（全选）、invert（反选）、none（取消选择）、odd（选择奇数项）、even（选择偶数项）"""
    selectedRowKeys: Optional[Union[list[int], list[str]]] = None
    """已选择项"""
    selectedRowKeysExpr: Optional[str] = None
    """已选择项正则表达式"""
    columnWidth: Optional[int] = None
    """自定义选择列列宽"""
    rowClick:  Optional[bool] = None
    """单条任意区域选中"""

class TableSelections2(AmisNode):
    """
    展开行配置属性表

    参考： https://aisuda.bce.baidu.com/amis/zh-CN/components/table2#%E5%B1%95%E5%BC%80%E8%A1%8C%E9%85%8D%E7%BD%AE%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    key: Optional[Literal['all','invert', 'none','odd', 'even']] = None
    """
    - 菜单类型，内置全选、反选、取消选择、选择奇数项、选择偶数项
    - 默认值：'all'
    """
    text: Optional[str] = None
    """自定义菜单项文本"""

class TableExpandable2(AmisNode):
    """
    展开行配置属性表

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/table2#%E5%B1%95%E5%BC%80%E8%A1%8C%E9%85%8D%E7%BD%AE%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    expandableOn: Optional[str] = None
    """指定可展开的行，要用 表达式"""
    keyField: Optional[str] = None
    """
    - 对应数据源的 key 值，默认是key，可指定为id、shortId等
    - 默认值：'key'
    """
    disableOn: Optional[str] = None
    """当前行是否可选择条件，要用 表达式"""
    selections: SerializeAsAny[Optional[TableSelections2]] = None
    """自定义筛选菜单，内置all（全选）、invert（反选）、none（取消选择）、odd（选择奇数项）、even（选择偶数项）"""
    selectedRowKeys: Optional[Union[list[int], list[str]]] = None
    """已选择项"""
    selectedRowKeysExpr: Optional[str] = None
    """已选择项正则表达式"""
    columnWidth: Optional[int] = None
    """自定义选择列列宽"""

class TableColumn2(AmisNode):
    """
    列配置属性表

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/table2#%E5%88%97%E9%85%8D%E7%BD%AE%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    type: Optional[str] = None
    """Literal['text','audio','image','link','tpl','mapping','carousel','date', 'progress','status','switch','list','json','operation','tag']"""
    label: Optional[Template] = None
    """标题文本内容"""
    name: Optional[str] = None
    """按名称关联数据"""
    fixed: Optional[Literal['left','right']] = None
    """是否修复当前列"""
    popOver: Optional[Union[bool, dict]] = None
    """弹出框"""
    quickEdit: Optional[Union[bool, dict]] = None
    """快速编辑"""
    copyable: Optional[Union[bool, dict]] = None
    """
    - 是否可复制
    - 默认值：{icon: string, content:string}
    """
    sortable: Optional[bool] = None
    """
    - 是否可排序
    - 默认值：False 
    """
    searchable: SerializeAsAny[Optional[Union[bool, SchemaNode]]] = None
    """
    - 是否快速搜索 boolean|图式
    - 默认值：False 
    """
    width: Optional[Union[int, str]] = None
    """默认值：列宽"""
    remark: Optional[RemarkT] = None
    """提示消息"""






