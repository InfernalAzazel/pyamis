from pathlib import Path
from jinja2 import Environment, FileSystemLoader


def render(
        self,
        template_path: str = "",
        locale: str = "zh_CN",
        cdn: str = "https://unpkg.com",
        pkg: str = "amis@1.10.2",
        site_title: str = "Amis",
        site_icon: str = "",
        theme: str = "cxd",
):
    """Render html template"""
    env = Environment(loader=FileSystemLoader(Path(__file__).parent / 'templates'))
    template_path = template_path or self.__default_template_path__

    return env.get_template(template_path).render(
        {
            "AmisSchemaJson": self.json(),
            "locale": locale.replace("_", "-"),  # Fix #50
            "cdn": cdn,
            "pkg": pkg,
            "site_title": site_title,
            "site_icon": site_icon,
            "theme": theme,
        }
    )