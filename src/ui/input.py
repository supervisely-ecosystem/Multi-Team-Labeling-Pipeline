import os

import supervisely as sly
from supervisely.app.widgets import (
    Card,
    SelectDataset,
    Button,
    Container,
    InputNumber,
    Field,
)

import src.globals as g

# dataset_thumbnail = DatasetThumbnail()
# dataset_thumbnail.hide()

load_button = Button("Load data")
change_dataset_button = Button("Change dataset", icon="zmdi zmdi-lock-open")
change_dataset_button.hide()

# no_dataset_message = Text(
#     "Please, select a dataset before clicking the button.",
#     status="warning",
# )
# no_dataset_message.hide()

# Global variables to access them from other modules.
selected_team = None
selected_workspace = None
selected_project = None
selected_dataset = None

if g.PROJECT_ID:
    # If the app was loaded from a project: showing the dataset selector in compact mode.
    sly.logger.debug("App was loaded from a project.")

    selected_team = g.TEAM_ID
    selected_workspace = g.WORKSPACE_ID
    selected_project = g.PROJECT_ID

    select_dataset = SelectDataset(
        project_id=g.PROJECT_ID,
        compact=True,
        show_label=False,
        allowed_project_types=[sly.ProjectType.IMAGES],
    )
else:
    # If the app was loaded from ecosystem: showing the dataset selector in full mode.
    sly.logger.debug("App was loaded from ecosystem.")

    select_dataset = SelectDataset(allowed_project_types=[sly.ProjectType.IMAGES])

# Inout card with all widgets.
select_project_card = Card(
    "1️⃣ Select project and dataset(s)",
    "Images from the selected dataset(s) will be loaded.",
    content=Container(
        widgets=[
            # dataset_thumbnail,
            select_dataset,
            load_button,
            change_dataset_button,
            # no_dataset_message,
        ]
    ),
)

# Field for choosing the number of teams.
teams_number_input = InputNumber(value=0, min=1, precision=0)
teams_number_field = Field(
    title="Needed number of teams",
    content=teams_number_input,
)

select_team_card = Card(
    "2️⃣ Select the number of teams",
    "These teams will labeling images.",
    content=Container(widgets=[teams_number_field]),
)
