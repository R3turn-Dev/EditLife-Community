from ..web import SingleWebPage
from flask import session, render_template


class Root(SingleWebPage):
    def __init__(self, path):
        super().__init__(
            name="/index.html",
            route="/",
            description="Root 홈(메인페이지)",
            template_folder=path
        )

        @self.route('/')
        def root(*args, **kwargs):
            return repr(session.items())
