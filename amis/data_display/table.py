from pydantic import SerializeAsAny
from amis.data_display import *
from amis.function import Action
from amis.types import *


class Table(AmisNode):
    """sheet"""

    type: str = "table"  # Specify as table renderer
    title: Optional[Optional[str]] = None  # title
    source: Optional[str] = None  # "${items}" # Data source, bind the current environment variable
    affixHeader: Optional[bool] = None  # True # whether to fix the header
    columnsTogglable: Union[bool, str, None] = None  # "auto" # Display column display switch, automatic: it is
    # automatically turned on when the number of columns is greater than or equal to 5
    placeholder: Optional[str] = None  # "No data" # Text prompt when there is no data
    className: Optional[str] = None  # "panel-default" # Outer CSS class name
    tableClassName: Optional[str] = None  # "table-db table-striped" # table CSS class name
    headerClassName: Optional[str] = None  # "Action.md-table-header" # Top outer CSS class name
    footerClassName: Optional[str] = None  # "Action.md-table-footer" # Bottom outer CSS class name
    toolbarClassName: Optional[str] = None  # "Action.md-table-toolbar" # Toolbar CSS class name
    columns: SerializeAsAny[Optional[List[Union["TableColumn", SchemaNode]]]] = None  # Used to set column information
    combineNum: Optional[int] = None  # Automatically combine cells
    itemActions: SerializeAsAny[Optional[List[Action]]] = None  # Floating row action button group
    itemCheckableOn: Optional[
        Expression] = None  # Configure the condition for whether the current row can be checked, use an
    # expression
    itemDraggableOn: Optional[
        Expression] = None  # To configure whether the current row can be dragged or not, use an expression
    checkOnItemClick: Optional[bool] = None  # False # whether clicking on the data row can check the current row
    rowClassName: Optional[str] = None  # Add CSS class name to row
    rowClassNameExpr: Optional[Template] = None  # Add CSS class name to row via template
    prefixRow: Optional[list] = None  # top summary row
    affixRow: Optional[list] = None  # Bottom summary row
    itemBadge: SerializeAsAny[Optional["Badge"]] = None  # Row badge configuration
    autoFillHeight: Optional[bool] = None  # Content area adaptive height
    footable: Union[bool, dict, None] = None  # When there are too many columns, the content cannot be fully displayed.
    # Some information can be displayed at the bottom, allowing users to expand to view the details. The
    # configuration is very simple, just turn on the footable attribute, and add a breakpoint attribute to the column
    # you want to display at the bottom as *.
    resizable: Optional[bool] = None  # 列宽度是否支持调整
    selectable: Optional[bool] = None  # 支持勾选
    multiple: Optional[bool] = None  # 勾选 icon 是否为多选样式checkbox， 默认为radio


class TableColumn(AmisNode):
    """Column configuration"""

    type: Optional[str] = None  # Literal['text','audio','image','link','tpl','mapping','carousel','date',
    # 'progress','status','switch','list','json','operation','tag']
    label: Optional[Template] = None  # header text content
    name: Optional[str] = None  # Associate data by name
    tpl: Optional[Template] = None  # Template
    fixed: Optional[str] = None  # whether to fix the current column left|right|none
    popOver: Union[bool, dict, None] = None  # popover
    quickEdit: Union[bool, dict, None] = None  # quick edit
    copyable: Union[bool, dict, None] = None  # whether to copy boolean or {icon: string, content:string}
    sortable: Optional[bool] = None  # False # whether it is sortable
    searchable: SerializeAsAny[
        Optional[Union[bool, SchemaNode]]] = None  # False # whether to quickly search boolean|Schema
    width: Union[int, str, None] = None  # column width
    remark: Optional[RemarkT] = None  # prompt message
    breakpoint: Optional[
        str] = None  # *,ls. When there are too many columns, the content cannot be displayed completely,
    # some information can be displayed at the bottom, and users can expand to view the details
    filterable: Union[bool, Dict[str, Any], None] = None  # filter configuration
    toggled: Optional[
        bool] = None  # whether to expand by default, in the column configuration, you can configure toggled to
    # false to not display this column by default
    backgroundScale: Optional[int] = None  # Can be used to automatically assign color scales based on data control
