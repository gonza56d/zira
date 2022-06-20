from zira.api.app import create_app
from zira.containers import Container


container = Container()
container.wire(modules=['zira.api.views'])
app = create_app()
