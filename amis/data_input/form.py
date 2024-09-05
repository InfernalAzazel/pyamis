from amis.constants import *
from amis.data_display import *
from amis.function import Action
from amis.types import *

class Form(AmisNode):
    """
    Form 表单

    表单是 amis 中核心组件之一，主要作用是提交或者展示表单数据。

    参考: https://aisuda.bce.baidu.com/amis/zh-CN/components/form/index#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class Messages(AmisNode):
        fetchSuccess: Optional[str] = None
        """获取成功时提示"""
        fetchFailed: Optional[str] = None
        """获取失败时提示"""
        saveSuccess: Optional[str] = None
        """保存成功时提示"""
        saveFailed: Optional[str] = None
        """保存失败时提示"""

    type: str = "form"
    """指定 Form 渲染器"""
    name: Optional[str] = None
    """设置一个名字后，方便其他组件与其通信"""
    mode: Optional[DisplayModeEnum] = None
    """表单展示方式，可以是：normal、horizontal 或者 inline"""
    horizontal: Optional["Horizontal"] = None
    """
    - 当 mode 为 horizontal 时有用，用来控制 label 的展示占比
    - 默认值: '{"left":2, "right":10, "justify": false}'"""
    labelAlign: Optional[Literal["right", "left"]] = None
    """ 
    - 表单项标签对齐方式，默认右对齐，仅在 mode为horizontal 时生效
    - 默认值: right
    """
    labelWidth: Union[int, str, None] = None
    """表单项标签自定义宽度"""
    title: Optional[Optional[str]] = None
    """
    - Form 的标题 
    - 默认值'表单'"""
    submitText: Optional[Optional[str]] = None
    """
    - 默认的提交按钮名称，如果设置成空，则可以把默认按钮去掉
    - 默认值：'提交'
    """
    className: Optional[str] = None
    """外部 Dom 的类名"""
    body: SerializeAsAny[Optional[List[Union["FormItem", SchemaNode]]]] = None
    """Form 表单项集合"""
    actions: SerializeAsAny[Optional[List["Action"]]] = None
    """Form 提交按钮，成员为 Action"""
    messages: SerializeAsAny[Optional[Messages]] = None
    """消息提示覆写，默认消息读取的是 API 返回的消息，但是在此可以覆写它"""
    wrapWithPanel: Optional[bool] = None
    """
    - 是否让 Form 用 panel 包起来，设置为 false 后，actions 将无效
    - 默认值：true
    """
    panelClassName: Optional[str] = None
    """外层 panel 的类名"""
    api: Optional[API] = None
    """Form 用来保存数据的 api"""
    initApi: Optional[API] = None
    """Form 用来获取初始数据的 api"""
    rules: Optional[list] = None
    """表单组合校验规则"""
    interval: Optional[int] = None
    """
    - 刷新时间(最低 3000)
    - 默认值：3000
    """
    silentPolling: Optional[bool] = None
    """
    - 配置刷新时是否显示加载动画
    - 默认值：false
    """
    stopAutoRefreshWhen: Optional[str] = None
    """
    通过表达式 来配置停止刷新的条件
    """
    initAsyncApi: Optional[API] = None
    """Form 用来获取初始数据的 api,与 initApi 不同的是，会一直轮询请求该接口，直到返回 finished 属性为 true 才 结束"""
    initFetch: Optional[bool] = None
    """
    - 设置了 initApi 或者 initAsyncApi 后，默认会开始就发请求，设置为 false 后就不会起始就请求接口
    - 默认值：true
    """
    initFetchOn: Optional[str] = None
    """用表达式来配置"""
    initFinishedField: Optional[Optional[str]] = None
    """
    - 设置了 initAsyncApi 后，默认会从返回数据的 data.finished 来判断是否完成，也可以设置成其他的 xxx，就会从 data.xxx 中获取
    - 默认值：'finished'
    """
    initCheckInterval: Optional[int] = None
    """
    - 设置了 initAsyncApi 以后，默认拉取的时间间隔
    - 默认值：3000
    """
    asyncApi: Optional[API] = None
    """设置此属性后，表单提交发送保存接口后，还会继续轮询请求该接口，直到返回 finished 属性为 true 才 结束"""
    checkInterval: Optional[int] = None
    """
    - 轮询请求的时间间隔，默认为 3 秒。设置 asyncApi 才有效
    默认值：3000
    """
    finishedField: Optional[Optional[str]] = None
    """
    - 如果决定结束的字段名不是 finished 请设置此属性，比如 is_success
    - 默认值：'finished'
    """
    submitOnChange: Optional[bool] = None
    """
    - 表单修改即提交
    - 默认值：false
    """
    submitOnInit: Optional[bool] = None
    """
    - 初始就提交一次
    - 默认值：false
    """
    resetAfterSubmit: Optional[bool] = None
    """
    - 提交后是否重置表单
    - 默认值：false
    """
    primaryField: Optional[str] = None
    """
    - 设置主键 id, 当设置后，检测表单是否完成时（asyncApi），只会携带此数据
    - 默认值：'id'
    """
    target: Optional[str] = None
    """
    - 默认表单提交自己会通过发送 api 保存数据，但是也可以设定另外一个 form 的 name 值，或者另外一个 CRUD 模型的 name 值。 
    - 如果 target 目标是一个 Form ，则目标 Form 会重新触发 initApi，api 可以拿到当前 form 数据。
    - 如果目标是一个 CRUD 模型，则目标模型会重新触发搜索，参数为当前 Form 数据。
    - 当目标是 window 时，会把当前表单的数据附带到页面地址上。
    """
    redirect: Optional[str] = None
    """设置此属性后，Form 保存成功后，自动跳转到指定页面。支持相对地址，和绝对地址（相对于组内的)"""
    reload: Optional[str] = None
    """操作完后刷新目标对象。请填写目标组件设置的 name 值，如果填写为 window 则让当前页面整体刷新。"""
    autoFocus: Optional[bool] = None
    """
    - 是否自动聚焦
    - 默认值：false
    """
    canAccessSuperData: Optional[bool] = None
    """
    - 指定是否可以自动获取上层的数据并映射到表单项上
    - 默认值：true
    """
    persistData: Optional[str] = None
    """指定一个唯一的 key，来配置当前表单是否开启本地缓存"""
    persistDataKeys: Optional[List[str]] = None
    """指指定只有哪些 key 缓存"""
    clearPersistDataAfterSubmit: Optional[bool] = None
    """
    - 指定表单提交成功后是否清除本地缓存
    - 默认值：true
    """
    preventEnterSubmit: Optional[bool] = None
    """
    - 禁用回车提交表单
    - 默认值：false
    """
    trimValues: Optional[bool] = None
    """
    - trim 当前表单项的每一个值
    - 默认值：false
    """
    promptPageLeave: Optional[bool] = None
    """
    - form 还没保存，即将离开页面前是否弹框确认。
    - 默认值：false
    """
    columnCount: Optional[int] = None
    """
    - 表单项显示为几列
    - 默认值：0
    """
    inheritData: Optional[bool] = None
    """
    - 默认表单是采用数据链的形式创建个自己的数据域
    - 表单提交的时候只会发送自己这个数据域的数据
    - 如果希望共用上层数据域可以设置这个属性为 false
    - 这样上层数据域的数据不需要在表单中用隐藏域或者显式映射才能发送了
    """
    static: Optional[bool] = None
    """
    - 2.4.0 整个表单静态方式展示
    - 详情请查看示例页: https://aisuda.bce.baidu.com/amis/examples/form/switchDisplay
    """
    staticClassName: Optional[str] = None
    """2.4.0 表单静态展示时使用的类名"""
    closeDialogOnSubmit: Optional[bool] = None
    """提交的时候是否关闭弹窗。当 form 里面有且只有一个弹窗的时候，本身提交会触发弹窗关闭，此属性可以关闭此行为"""
    debug: Optional[bool] = None

class Horizontal(AmisNode):
    left: Optional[int] = None
    """左侧标签的宽度比例"""
    right: Optional[int] = None
    """右侧控制器的宽度比"""
    justify: Optional[bool] = None

class FormItem(AmisNode):
    """
    FormItem 普通表单项

    表单项 是组成一个表单的基本单位，它具有的一些特性会帮助我们更好地实现表单操作。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/formitem#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """



    class AutoFill(BaseAmisModel):

        showSuggestion: Optional[bool] = None
        """true 为参照录入，false 自动填充"""
        api: Optional[API] = None
        """自动填充接口/参照录入筛选 CRUD 请求配置"""
        silent: Optional[bool] = None
        """是否展示数据格式错误提示，默认为 true"""
        fillMappinng: SerializeAsAny[Optional[SchemaNode]] = None
        """自动填充/参照录入数据映射配置，键值对形式，值支持变量获取及表达式"""
        trigger: Optional[str] = None
        """showSuggestion 为 true 时，参照录入支持的触发方式，目前支持 change「值变化」｜ focus 「表单项聚焦」"""
        mode: Optional[str] = None
        """showSuggestion 为 true 时，参照弹出方式 dialog, drawer, popOver"""
        labelField: Optional[str] = None
        """showSuggestion 为 true 时，设置弹出 dialog,drawer,popOver 中 picker 的 labelField"""
        position: Optional[str] = None
        """showSuggestion 为 true 时，参照录入 mode 为 popOver 时，可配置弹出位置"""
        size: Optional[str] = None
        """showSuggestion 为 true 时，参照录入 mode 为 dialog 时，可设置大小"""
        columns: SerializeAsAny[Optional[List["TableColumn"]]] = None
        """showSuggestion 为 true 时，数据展示列配置"""
        filter: SerializeAsAny[Optional[SchemaNode]] = None
        """showSuggestion 为 true 时，数据查询过滤条件"""

    class StaticSchema(SchemaNode):
        limit: Optional[int] = None
        """
        - 2.4.0 select、checkboxes 等选择类组件多选时展示态展示的数量
        - 默认值：10
        """

    type: str = "input-text"
    """指定表单项类型"""
    className: Optional[str] = None
    """表单最外层类名"""
    inputClassName: Optional[str] = None
    """表单控制器类名"""
    labelClassName: Optional[str] = None
    """label 的类名"""
    name: Optional[str] = None
    """字段名，指定该表单项提交时的 key"""
    value: Optional[str] = None
    """表单默认值"""
    label: Union[bool, Template, None] = None
    """表单项标签"""
    labelAlign: Optional[str] = None
    """
    - 表单项标签对齐方式，默认右对齐，仅在 mode为horizontal 时生效
    - 默认值：'right'
    """
    labelRemark: Optional[RemarkT] = None
    """表单项标签描述"""
    description: Optional[Template] = None
    """表单项描述"""
    placeholder: Optional[str] = None
    """表单项描述"""
    inline: Optional[bool] = None
    """是否为 内联 模式"""
    strictMode: Optional[bool] = None
    """通过配置 false 可以及时获取所有表单里面的数据，否则可能会有不同步"""
    submitOnChange: Optional[bool] = None
    """是否该表单项值发生变化时就提交当前表单。"""
    disabled: Optional[bool] = None
    """当前表单项是否是禁用状态"""
    disabledOn: Optional[Expression] = None
    """当前表单项是否禁用的条件"""
    visible: Optional[bool] = None
    """当前表单项是否禁用的条件"""
    visibleOn: Optional[Expression] = None
    """当前表单项是否禁用的条件"""
    required: Optional[bool] = None
    """是否为必填"""
    requiredOn: Optional[Expression] = None
    """通过表达式来配置当前表单项是否为必填"""
    validations: SerializeAsAny[Optional[Union["Validation", Expression]]] = None
    """表单项值格式验证，支持设置多个，多个规则用英文逗号隔开"""
    validateApi: Optional[API] = None
    """表单校验接口"""
    autoFill: Optional[AutoFill] = None
    """数据录入配置，自动填充或者参照录入"""
    static: Optional[bool] = None
    """2.4.0 当前表单项是否是静态展示，目前支持静支持静态展示的表单项"""
    staticClassName: Optional[str] = None
    """2.4.0 静态展示时的类名"""
    staticLabelClassName: Optional[str] = None
    """2.4.0 静态展示时的 Label 的类名"""
    staticInputClassName: Optional[str] = None
    """2.4.0 静态展示时的 value 的类名"""
    staticSchema: SerializeAsAny[Optional[StaticSchema]] = None
    """2.4.0 自定义静态展示方式"""


class Validation(BaseAmisModel):
    """
    表单项值发生变化即校验

    默认校验是当进行行为操作时，对表单项进行校验，如果你想每次表单项的值发生变化的时候就校验，请配置 "validateOnChange": true

    参考: https://aisuda.bce.baidu.com/amis/zh-CN/components/form/formitem#%E6%94%AF%E6%8C%81%E7%9A%84%E6%A0%BC%E5%BC%8F%E6%A0%A1%E9%AA%8C
    """
    isEmail: Optional[bool] = None
    """必须是 电子邮件"""
    isUrl: Optional[bool] = None
    """必须是 Url"""
    isNumeric: Optional[bool] = None
    """必须是 数值"""
    isAlpha: Optional[bool] = None
    """必须是 字母"""
    isAlphanumeric: Optional[bool] = None
    """必须是 字母或者数字"""
    isInt: Optional[bool] = None
    """必须是 整形"""
    isFloat: Optional[bool] = None
    """必须是 浮点形"""
    isLength: Optional[int] = None
    """是否长度正好等于设定值"""
    minLength: Optional[int] = None
    """最小长度"""
    maxLength: Optional[int] = None
    """最大长度"""
    maximum: Optional[int] = None
    """最大值"""
    minimum: Optional[int] = None
    """最小值"""
    equals: Optional[str] = None
    """当前值必须完全等于 xxx"""
    equalsField: Optional[str] = None
    """当前值必须与 xxx 变量值一致"""
    isJson: Optional[bool] = None
    """是否是合法的 Json 字符串"""
    isUrlPath: Optional[bool] = None
    """是 url 路径"""
    isPhoneNumber: Optional[bool] = None
    """是否为合法的手机号码"""
    isTelNumber: Optional[bool] = None
    """是否为合法的电话号码"""
    isZipcode: Optional[bool] = None
    """是否为邮编号码"""
    isId: Optional[bool] = None
    """是否为身份证号码，支持 18 位和 15 位验证，单个验证请使用 isId18 / isId15"""
    matchRegexp: Optional[str] = None
    """
    - 必须命中某个正则
    - matchRegexp${n}:/foo/ 这样的需要手动加入字段
    """
    isDateTimeSame: Optional[bool] = None
    """日期和目标日期相同，支持指定粒度，默认到毫秒 millisecond"""
    isDateTimeBefore: Optional[bool] = None
    """日期早于目标日期，支持指定粒度，默认到毫秒 millisecond"""
    isDateTimeAfter: Optional[bool] = None
    """日期晚于目标日期，支持指定粒度，默认到毫秒 millisecond"""
    isDateTimeSameOrBefore: Optional[bool] = None
    """日期早于目标日期或和目标日期相同，支持指定粒度，默认到毫秒 millisecond"""
    isDateTimeSameOrAfter: Optional[bool] = None
    """日期晚于目标日期或和目标日期相同，支持指定粒度，默认到毫秒 millisecond"""
    isDateTimeBetween: Optional[bool] = None
    """日期处于目标日期范围，支持指定粒度和区间的开闭形式，默认到毫秒 millisecond，左右开区间'()'"""
    isTimeSame: Optional[bool] = None
    """时间和目标时间相同，支持指定粒度，默认到毫秒 millisecond"""
    isTimeBefore: Optional[bool] = None
    """时间早于目标时间，支持指定粒度，默认到毫秒 millisecond"""
    isTimeAfter: Optional[bool] = None
    """时间晚于目标时间，支持指定粒度，默认到毫秒 millisecond"""
    isTimeSameOrBefore: Optional[bool] = None
    """时间早于目标时间或和目标时间相同，支持指定粒度，默认到毫秒 millisecond"""
    isTimeSameOrAfter: Optional[bool] = None
    """时间晚于目标时间或和目标时间相同，支持指定粒度，默认到毫秒 millisecond"""
    isTimeBetween: Optional[bool] = None
    """时间处于目标时间范围，支持指定粒度和区间的开闭形式，默认到毫秒 millisecond，左右开区间'()'"""
    isVariableName: Optional[bool] = None
    """是否为合法的变量名，默认规则为 /^[a-zA-Z_]+[a-zA-Z0-9]*$/ 可以自己指定如 {isVariableName: /^a.*$/}"""