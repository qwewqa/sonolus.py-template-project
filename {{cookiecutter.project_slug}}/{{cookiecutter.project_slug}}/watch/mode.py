from {{ cookiecutter.project_slug }}.common.buckets import Buckets
from {{ cookiecutter.project_slug }}.common.effect import Effects
from {{ cookiecutter.project_slug }}.common.particle import Particles
from {{ cookiecutter.project_slug }}.common.skin import Skin
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
