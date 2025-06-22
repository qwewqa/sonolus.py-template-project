from sonolus.script.bucket import Bucket, bucket, bucket_sprite, buckets
from sonolus.script.text import StandardText

from {{ cookiecutter.project_slug }}.lib.skin import Skin


@buckets
class Buckets:
    note: Bucket = bucket(
        sprites=[
            bucket_sprite(
                sprite=Skin.note,
                x=0,
                y=0,
                w=2,
                h=2,
            )
        ],
        unit=StandardText.MILLISECOND_UNIT,
    )
