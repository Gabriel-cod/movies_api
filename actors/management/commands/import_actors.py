from django.core.management.base import BaseCommand
from actors.models import Actor


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            "file_path",
            type=str,
            help="CSV file path containing the actors to register. The CSV file must have the first line with \"name,birthday,nationality\" syntax."
        )

    def handle(self, *args, **options):
        file_path = options["file_path"]
        try:
            with open(file_path, "r", encoding='utf-8') as file:
                print('Importing actors...')
                reader = file.readlines()
                reader.remove(reader[0])
                print('Registering actors...')
                exist_count = registered = 0
                for line in reader:
                    name, birthday, nationality = line.strip().split(",")
                    if Actor.objects.filter(name=name).exists():
                        exist_count += 1
                        continue
                    Actor.objects.create(name=name, birthday=birthday, nationality=nationality)
                    registered += 1
                print(f'Writing objects: {(registered / len(reader)) * 100:.0f}% [{registered}/{len(reader)}] actors registered.')
                print(f'[{exist_count}] actors already exist in the database.')
        except FileNotFoundError:
            print("File not found.")
