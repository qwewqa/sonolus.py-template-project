from {{ cookiecutter.project_slug }}.lib.skin import Skin
from sonolus.script.engine import PreviewMode

preview_mode = PreviewMode(
    archetypes=[],
    skin=Skin,
)
