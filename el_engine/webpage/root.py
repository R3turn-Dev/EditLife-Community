from ..web import SingleWebPage
from flask import session, request, render_template, send_from_directory
from ..db import engine, profile, engineSelect


class Root:
    def __init__(self, path):
        self.parent = SingleWebPage(
            name="/",
            url_prefix="",
            description="Root 홈(메인페이지)",
            template_folder=path
        )
        self.mobile_platform = ['android', 'iphone', 'blackberry']
        self.db = engineSelect(engine)(**profile)

        print(self.parent.bp.static_folder)

        @self.parent.bp.route('/')
        def root(*args, **kwargs):
            _, member_count = self.db.getMemberCount()
            _, boards = self.db.geBoards(selects="name")
            _, most_comments = self.db.getArticles(selects="title, board, no, (SELECT COUNT(*) FROM comments WHERE article=articles.no)", board="커뮤니티", sort="(SELECT COUNT(*) FROM comments WHERE article=articles.no) DESC")

            is_mobile = request.user_agent.platform in self.mobile_platform
            return render_template("root/main.html", request=request, is_mobile=is_mobile, board= {
                "members": member_count,
                "boards": boards,
                "main_frame": {
                    "boards": [
                        ["커뮤니티", "bleu_de_france"],
                        ["편집툴 Tip", "brink-pink"]
                    ],
                    "articles": {
                        "커뮤니티": self.db.getArticles(selects="title, no, (SELECT COUNT(*) FROM comments WHERE article=articles.no)", board="커뮤니티", sort="(SELECT COUNT(*) FROM comments WHERE article=articles.no) DESC LIMIT 5")[1],
                        "편집툴 Tip": self.db.getArticles(selects="title, board, no, (SELECT COUNT(*) FROM comments WHERE article=articles.no)", board="편집툴 Tip", sort="(SELECT COUNT(*) FROM comments WHERE article=articles.no) DESC LIMIT 5")[1]
                    }
                },
                "most_comments": most_comments
            })

        @self.parent.bp.route("/<any(css, img, js, media):folder>/<path:filename>")
        def test(folder, filename):
            return send_from_directory(path + "/root/", folder + "/" + filename)