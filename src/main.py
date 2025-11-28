import supervisely as sly

from supervisely.app.widgets import Container

import src.globals as g
import src.ui.input as input

images_container = Container()

layout = Container(
    widgets=[input.select_project_card, input.select_team_card], direction="horizontal"
)

app = sly.Application(layout=layout, static_dir=g.STATIC_DIR)
