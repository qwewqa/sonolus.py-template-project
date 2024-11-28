from sonolus.script.engine import PlayMode

from {{ cookiecutter.project_slug }}.common.buckets import Buckets
from {{ cookiecutter.project_slug }}.common.effect import Effects
from {{ cookiecutter.project_slug }}.common.particle import Particles
from {{ cookiecutter.project_slug }}.common.skin import Skin

play_mode = PlayMode(
    archetypes=[],
    skin=Skin,
    effects=Effects,
    particles=Particles,
    buckets=Buckets,
)
