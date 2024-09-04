
[English](./README.md) | [简体中文](./README_zh-CN.md)


## introduction

<h2 align="center"> pyamis </h2>
<p align="center">
    <em>amis is a low-code front-end framework that uses JSON configuration to generate pages, which can reduce the workload of page development and greatly improve efficiency</em><br/>
    <em>pyamis is based on Baidu's open-source AMIS for Python encapsulation</em>
</p>

------
> Do not use in a production environment at this time during the testing phase

`pyamis` is a high-performance, efficient framework based on `jinja2`, `amis`, and `Python 3.7+`, and leverages standard Python type hints.
It was originally developed to improve the application ecosystem and quickly generate visual kanban boards for web applications. It follows the `Apache 2.0` license, is free and open source. I would very much like to have your sponsorship and support in order to better operate and maintain this project in the long term.

## works with fastapi
- code
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
- run

```python
uvicorn examples.fastapi:app --reload --port 3000
```

## license

- According to the `Apache 2.0` license, `pyamis` is free and open source and can be used commercially. Please clearly display the copyright information of `pyamis` on the interface.