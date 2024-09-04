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
