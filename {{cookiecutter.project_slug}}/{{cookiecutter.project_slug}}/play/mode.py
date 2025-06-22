from sonolus.script.engine import PlayMode

from {{ cookiecutter.project_slug }}.lib.buckets import Buckets
from {{ cookiecutter.project_slug }}.lib.effect import Effects
from {{ cookiecutter.project_slug }}.lib.particle import Particles
from {{ cookiecutter.project_slug }}.lib.skin import Skin

play_mode = PlayMode(
    archetypes=[],
    skin=Skin,
    effects=Effects,
    particles=Particles,
    buckets=Buckets,
)
