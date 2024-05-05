from PugglePuzzles.seed import Seeder
from sudokus.models import Sudoku

seeder = Seeder()

seeder.add_entity(Sudoku, 10, {
    'created_at': lambda x: seeder.faker.date_time_this_year(before_now=True, after_now=False),
})

inserted_pks = seeder.execute()
