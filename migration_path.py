from typing import Optional
from wildlife_tracker.habitat_management.habitat import Habitat


class MigrationPath:
    def __init__(self,
                path_id: int,
                destination: Habitat,
                species: str,
                start_location: Habitat,
                duration: Optional[int] = None) -> None:
        self.path_id = path_id
        self.destination = destination
        self.species = species
        self.start_location = start_location
        self.duration = duration

    def update_migration_path_details(self, **kwargs) -> None:
        pass

    def get_migration_path_details(self) -> dict:
        pass