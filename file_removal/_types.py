from typing import List
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Config(object):
    """
    This class is a TypedDict that is used to store the configuration
    of the program.
    """
    root_dir: str
    file_ext: List[str]
