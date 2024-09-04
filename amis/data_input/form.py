from amis.constants import *
from amis.data_display import *
from amis.function import Action
from amis.types import *


class Form(AmisNode):
    """Form"""

    class Messages(AmisNode):
        fetchSuccess: Optional[str] = None  # Prompt when fetch is successful
        fetchFailed: Optional[str] = None  # Prompt when fetch fails
        saveSuccess: Optional[str] = None  # Prompt when saving is successful
        saveFailed: Optional[str] = None  # Prompt when saving fails

    type: str = "form"
    """指定 Form 渲染器"""
    name: Optional[str] = None  # After setting a name, it is convenient for other components to communicate with it
    mode: Optional[DisplayModeEnum] = None  # Form display mode, can be: normal, horizontal or inline
    horizontal: Optional["Horizontal"] = None  # Useful when mode is horizontal,
    # Used to control label {"left": "col-sm-2", "right": "col-sm-10", "offset": "col-sm-offset-2"}
    title: Optional[Optional[str]] = None  # Title of the Form
    submitText: Optional[
        Optional[str]] = None  # "Submit" # Default submit button name, if it is set to empty, the default
    # button can be removed.
    className: Optional[str] = None  # The class name of the outer Dom
    body: SerializeAsAny[Optional[List[Union["FormItem", SchemaNode]]]] = None  # Form item collection
    actions: SerializeAsAny[Optional[List["Action"]]] = None  # Form submit button, the member is Action
    actionsClassName: Optional[str] = None  # class name of actions
    messages: SerializeAsAny[
        Optional[Messages]
    ] = None  # The message prompts to be overridden. The default message reads the message returned
    # by the API, but it can be overridden here.
    wrapWithPanel: Optional[
        bool] = None  # whether to wrap the Form with panel, if set to false, actions will be invalid.
    panelClassName: Optional[str] = None  # The class name of the outer panel
    api: Optional[API] = None  # The api that Form uses to save data.
    initApi: Optional[API] = None  # The api that Form uses to get initial data.
    rules: Optional[list] = None  # Form combination validation rules Array<{rule:string;message:string}>
    interval: Optional[int] = None  # refresh time (minimum 3000)
    silentPolling: Optional[
        bool] = None  # False # whether to show the loading animation when the configuration is refreshed
    stopAutoRefreshWhen: Optional[str] = None  # Configure the condition for stopping refresh by expression
    initAsyncApi: Optional[
        API] = None  # The api that Form uses to obtain initial data, which is different from initApi,
    # will keep polling and request this interface until the returned finished attribute is true.
    initFetch: Optional[
        bool] = None  # After initApi or initAsyncApi is set, the request will be sent by default, and if it is
    # set to false, the interface will not be requested at the beginning
    initFetchOn: Optional[str] = None  # Use expression to configure
    initFinishedField: Optional[
        Optional[str]] = None  # After setting initAsyncApi, by default, the data.finished of the
    # returned data will be used to judge whether it is completed.
    # Can also be set to other xxx, it will be obtained from data.xxx
    initCheckInterval: Optional[int] = None  # After setting initAsyncApi, the default pull interval
    asyncApi: Optional[
        API] = None  # After setting this property, after the form is submitted and sent to save the interface,
    # it will continue to poll and request the interface, and it will not end until the returned finished property is
    # true.
    checkInterval: Optional[
        int] = None  # The time interval for polling requests, the default is 3 seconds. Setting asyncApi
    # is valid
    finishedField: Optional[
        Optional[str]] = None  # Set this property if the field name that decides to end is not finished,
    # such as is_success
    submitOnChange: Optional[bool] = None  # Form modification is submitted
    submitOnInit: Optional[bool] = None  # Submit once initially
    resetAfterSubmit: Optional[bool] = None  # whether to reset the form after submitting
    primaryField: Optional[
        str] = None  # Set the primary key id. When set, it will only carry this data when checking whether
    # the form is completed (asyncApi).
    target: Optional[
        str] = None  # The default form submission itself will save the data by sending the api, but you can also
    # set the name value of another form, or another CRUD model name value. If the target target is a Form,
    # the target Form will trigger initApi again, and the api can get the current form data. If the target is a CRUD
    # model, the target model will re-trigger the search with the current Form data as the parameter. When the target
    # is window, the data of the current form will be attached to the page address.
    redirect: Optional[
        str] = None  # After setting this attribute, after the Form is saved successfully, it will automatically
    # jump to the specified page. Support relative addresses, and absolute addresses (relative to the group).
    reload: Optional[
        str] = None  # Refresh the target object after the operation. Please fill in the name value set by the
    # target component. If it is filled in window, the current page will be refreshed as a whole.
    autoFocus: Optional[bool] = None  # whether to auto focus.
    canAccessSuperData: Optional[
        bool] = None  # Specify whether the upper layer data can be automatically obtained and mapped
    # to the form item
    persistData: Optional[
        str] = None  # Specify a unique key to configure whether to enable local caching for the current form
    clearPersistDataAfterSubmit: Optional[
        bool] = None  # Specify whether to clear the local cache after the form is submitted
    # successfully
    preventEnterSubmit: Optional[bool] = None  # Disable EnterSubmit form submission
    trimValues: Optional[bool] = None  # trim each value of the current form item
    promptPageLeave: Optional[
        bool] = None  # The form has not been saved, whether to confirm with a pop-up box before leaving
    # the page.
    columnCount: Optional[int] = None  # The form item is displayed as several columns
    debug: Optional[bool] = None
    inheritData: Optional[
        bool] = None  # true # The default form is to create its own data field in the form of a data link,
    # and only the data in this data field will be sent when the form is submitted. If you want to share the
    # upper layer data field, you can set this attribute to false, so that the data in the upper layer data field
    # does not need to be sent in the form with hidden fields or explicit mapping.
    static: Optional[bool] = None  # false # 2.4.0. The entire form is displayed statically.
    # For details, please refer to the:https://aisuda.bce.baidu.com/amis/examples/form/switchDisplay.
    staticClassName: Optional[str] = None  # 2.4.0. The name of the class used when the form is statically displayed
    labelAlign: Optional[Literal["right", "left"]] = None  # "right"  # 表单项标签对齐方式，默认右对齐，
    # 仅在 mode为horizontal 时生效
    labelWidth: Union[int, str, None] = None  # 表单项标签自定义宽度
    persistDataKeys: Optional[List[str]] = None  # 指指定只有哪些 key 缓存
    closeDialogOnSubmit: Optional[bool] = None  # 提交的时候是否关闭弹窗


class Horizontal(AmisNode):
    left: Optional[int] = None
    """左侧标签的宽度比例"""
    right: Optional[int] = None
    """右侧控制器的宽度比"""
    offset: Optional[int] = None
    """未设置标签时，右侧控制器的偏移量"""

class FormItem(AmisNode):
    """Form item common"""

    class AutoFill(BaseAmisModel):
        showSuggestion: Optional[bool] = None  # true refers to input, false automatically fills
        api: Optional[
            API
        ] = None  # Automatically populate the interface/filter the CRUD request configuration with reference to entry
        silent: Optional[bool] = None  # Whether to display a data format error message. The default value is true
        fillMappinng: SerializeAsAny[
            Optional[SchemaNode]
        ] = None  # Auto-fill/reference input data mapping configuration, key-value pair form,
        # value support variable acquisition and expression
        trigger: Optional[str] = None  # ShowSuggestion to true, the reference input support way of trigger,
        # currently supports change "value change" | focus "form focus"
        mode: Optional[str] = None  # When showSuggestion is true, refer to the popOver mode: dialog, drawer, popOver
        labelField: Optional[
            str] = None  # When showSuggestion is true, set the popup dialog,drawer,popOver picker's labelField
        position: Optional[
            str] = None  # If showSuggestion is true, set the popOver location as shown in the input mode Popover
        size: Optional[str] = None  # If showSuggestion is true, set the value as shown in dialog mode
        columns: SerializeAsAny[
            Optional[List["TableColumn"]]
        ] = None  # When showSuggestion is true, the data display column configuration
        filter: SerializeAsAny[Optional[SchemaNode]] = None  # When showSuggestion is true, data query filter condition

    type: str = "input-text"  # Specify the form item type
    className: Optional[str] = None  # The outermost class name of the form
    inputClassName: Optional[str] = None  # Form controller class name
    labelClassName: Optional[str] = None  # class name of label
    name: Optional[str] = None  # Field name, specifying the key when the form item is submitted
    label: Union[bool, Template, None] = None  # form item label template or false
    labelAlign: Optional[
        str] = None  # "right" # Form item label alignment, default right alignment, only effective when mode is
    labelRemark: Optional[RemarkT] = None  # Form item label description
    description: Optional[Template] = None  # Form item description
    placeholder: Optional[str] = None  # Form item description
    inline: Optional[bool] = None  # whether it is inline mode
    submitOnChange: Optional[bool] = None  # whether to submit the current form when the value of the form item changes.
    disabled: Optional[bool] = None  # whether the current form item is disabled
    disabledOn: Optional[Expression] = None  # The condition for whether the current form item is disabled
    visible: Optional[bool] = None  # whether the current form item is disabled or not
    visibleOn: Optional[Expression] = None  # The condition for whether the current form item is disabled
    required: Optional[bool] = None  # whether it is required.
    requiredOn: Optional[Expression] = None  # Use an expression to configure whether the current form item is required.
    validations: SerializeAsAny[
        Optional[Union["Validation", Expression]]
    ] = None  # Validation of the form item value format, multiple settings
    # are supported, and multiple rules are separated by commas.
    validateApi: Optional[API] = None  # Form validation interface
    copyable: Union[bool, dict, None] = None  # whether to copy boolean or {icon: string, content:string}
    autoFill: Optional[AutoFill] = None  # Data entry configuration, automatic filling or reference entry
    static: Optional[bool] = None  # 2.4.0 Whether the current form item is static display,
    staticOn: Optional[Expression] = None  # 2.4.0 The condition for whether the current form item is static display
    # the current support static display of the form item
    staticClassName: Optional[str] = None  # 2.4.0 The class name for static display
    staticLabelClassName: Optional[str] = None  # 2.4.0 The class name of the Label for static display
    staticInputClassName: Optional[str] = None  # 2.4.0 The class name of value when static display
    staticSchema: Union[str, list, None] = None  # SchemaNode




class Validation(BaseAmisModel):
    isEmail: Optional[bool] = None  # Must be Email.
    isUrl: Optional[bool] = None  # Must be a Url.
    isNumeric: Optional[bool] = None  # Must be a number.
    isAlpha: Optional[bool] = None  # Must be an alpha.
    isAlphanumeric: Optional[bool] = None  # Must be a letter or a number.
    isInt: Optional[bool] = None  # Must be an integer.
    isFloat: Optional[bool] = None  # Must be a float.
    isLength: Optional[int] = None  # whether the length is exactly equal to the set value.
    minLength: Optional[int] = None  # Minimum length.
    maxLength: Optional[int] = None  # Maximum length.
    maximum: Optional[int] = None  # Maximum value.
    minimum: Optional[int] = None  # Minimum value.
    equals: Optional[str] = None  # The current value must be exactly equal to xxx.
    equalsField: Optional[str] = None  # The current value must be the same as the xxx variable value.
    isJson: Optional[bool] = None  # Is it a valid Json string.
    isUrlPath: Optional[bool] = None  # is the url path.
    isPhoneNumber: Optional[bool] = None  # Is it a legal phone number
    isTelNumber: Optional[bool] = None  # Is it a valid phone number
    isZipcode: Optional[bool] = None  # whether it is a zip code
    isId: Optional[bool] = None  # whether it is an ID number, no verification is done
    matchRegexp: Optional[str] = None  # Must hit a certain regexp. /foo/