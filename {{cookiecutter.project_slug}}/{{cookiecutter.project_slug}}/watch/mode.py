from {{ cookiecutter.project_slug }}.lib.buckets import Buckets
from {{ cookiecutter.project_slug }}.lib.effect import Effects
from {{ cookiecutter.project_slug }}.lib.particle import Particles
from {{ cookiecutter.project_slug }}.lib.skin import Skin
from {{ cookiecutter.project_slug }}.watch.update_spawn import update_spawn
from sonolus.script.engine import WatchMode

watch_mode = WatchMode(
    archetypes=[],
    skin=Skin,
    effects=Effects,
    particles=Particles,
    buckets=Buckets,
    update_spawn=update_spawn,
)
