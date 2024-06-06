from ...models import Language
from django.core.management.base import BaseCommand
from pathlib import Path
from typing import Any, Optional

class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        Language.objects.all().delete()
        langs_added=[]
        with open(Path(Path(__file__).parent, "languages.txt"), "r") as file:
            for i in file.readlines():
                i=i.strip().split(",")
                Language(language = i[0], translate_short=i[1], recognition_short=i[2]).save()
                langs_added.append(i[0])
                
        return f"Added languages: {langs_added}"