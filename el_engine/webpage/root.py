from ..web import SingleWebPage
from flask import session, render_template


class Root():
    def __init__(self, path):
        self.parent = SingleWebPage(
            name="/index.html",
            url_prefix="/",
            description="Root 홈(메인페이지)",
            template_folder=path
        )

        @self.parent.bp.route('/')
        def root(*args, **kwargs):
            return repr(session.items())
