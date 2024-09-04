

[简体中文](./README_zh-CN.md) | [English](./README.md)

# 介绍

<h2 align="center">pyamis</h2>
<p align="center">
    <em>amis 是一个低代码前端框架，它使用 JSON 配置来生成页面，可以减少页面开发工作量，极大提升效率</em><br/>
    <em>pyamis 是基于百度开源的 amis 进行 python 封装</em>
</p>

------
> 目前在测试阶段请勿用于生产环境

`pyamis` 是一个高性能、高效的框架，基于 `jinja2`、`amis` 和 `Python 3.7+`，并利用标准的 Python 类型提示。
开发它的初衷是完善应用生态，快速生成 Web 应用的可视化看板。它遵循 `Apache 2.0` 协议，免费且开源。我非常希望得到大家的赞助和支持，以便更好地长期运营和维护这个项目。

## 配合 fastapi
- 代码
```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from amis.function import App

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_root():
    amis_app = App()
    amis_app.type = 'page'
    amis_app.body = {
        'type': 'form',
        'mode': 'horizontal',
        'api': '/saveForm',
        'body': [
            {
                'label': 'Name',
                'type': 'input-text',
                'name': 'name'
            },
            {
                'label': 'Email',
                'type': 'input-email',
                'name': 'email'
            }
        ]
    }

    return HTMLResponse(content=amis_app.render())
```
- 运行

```python
uvicorn examples.fastapi:app --reload --port 3000
```

## 许可

- 根据 `Apache 2.0` 协议，`pyamis` 是免费开源的，可用于商业用途。请在界面上清晰显示 `pyamis` 的版权信息。