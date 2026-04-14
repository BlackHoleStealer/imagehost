from app.routes.upload import upload_route
from app.routes.view import view_route
from app.routes.raw import raw_route
from app.routes.index import index_route

def register_routes(app):
    app.add_url_rule("/upload", view_func=upload_route, methods=["POST"])
    app.add_url_rule("/view", view_func=view_route)
    app.add_url_rule("/i/<file_id>", view_func=raw_route)
    app.add_url_rule("/", view_func=index_route)