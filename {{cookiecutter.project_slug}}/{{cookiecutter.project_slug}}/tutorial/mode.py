from sonolus.script.engine import TutorialMode

from {{ cookiecutter.project_slug }}.common.effect import Effects
from {{ cookiecutter.project_slug }}.common.particle import Particles
from {{ cookiecutter.project_slug }}.common.skin import Skin
from {{ cookiecutter.project_slug }}.tutorial.init import preprocess
from {{ cookiecutter.project_slug }}.tutorial.instructions import InstructionIcons, Instructions
from {{ cookiecutter.project_slug }}.tutorial.navigate import navigate
from {{ cookiecutter.project_slug }}.tutorial.update import update

tutorial_mode = TutorialMode(
    skin=Skin,
    effects=Effects,
    particles=Particles,
    instructions=Instructions,
    instruction_icons=InstructionIcons,
    preprocess=preprocess,
    navigate=navigate,
    update=update,
)
