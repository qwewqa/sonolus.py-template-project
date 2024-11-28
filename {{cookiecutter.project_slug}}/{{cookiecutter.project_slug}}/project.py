from sonolus.script.engine import Engine, EngineData
from sonolus.script.project import Project

from {{ cookiecutter.project_slug }}.common.options import Options
from {{ cookiecutter.project_slug }}.common.ui import ui_config
from {{ cookiecutter.project_slug }}.level import level
from {{ cookiecutter.project_slug }}.play.mode import play_mode
from {{ cookiecutter.project_slug }}.preview.mode import preview_mode
from {{ cookiecutter.project_slug }}.tutorial.mode import tutorial_mode
from {{ cookiecutter.project_slug }}.watch.mode import watch_mode

engine = Engine(
    name="{{ cookiecutter.project_slug }}",
    title="{{ cookiecutter.project_name }}",
    skin="pixel",
    particle="pixel",
    background="vanilla",
    data=EngineData(
        ui=ui_config,
        options=Options,
        play=play_mode,
        watch=watch_mode,
        preview=preview_mode,
        tutorial=tutorial_mode,
    ),
)

project = Project(
    engine=engine,
    levels=[level],
)
