from sonolus.script.level import Level, LevelData

level = Level(
    name="{{ cookiecutter.project_slug }}_level",
    title="{{ cookiecutter.project_name }} Level",
    bgm=None,
    data=LevelData(
        bgm_offset=0,
        entities=[],
    ),
)


def load_levels():
    yield level
