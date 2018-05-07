from ..web import SingleWebPage
from flask import session, request, render_template, send_from_directory


class Root():
    def __init__(self, path):
        self.parent = SingleWebPage(
            name="/",
            url_prefix="",
            description="Root 홈(메인페이지)",
            template_folder=path
        )
        print(self.parent.bp.static_folder)

        @self.parent.bp.route('/')
        def root(*args, **kwargs):
            return render_template("/root/index.html", request=request)

        @self.parent.bp.route("/<any(css, img, js, media):folder>/<path:filename>")
        def test(folder, filename):
            return send_from_directory(path + "/root/", folder + "/" + filename)