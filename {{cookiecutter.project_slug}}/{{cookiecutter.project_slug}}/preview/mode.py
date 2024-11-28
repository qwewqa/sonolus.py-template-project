from {{ cookiecutter.project_slug }}.common.skin import Skin
from sonolus.script.engine import PreviewMode

preview_mode = PreviewMode(
    archetypes=[],
    skin=Skin,
)
