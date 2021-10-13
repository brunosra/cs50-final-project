from cocciep.db import db
from datetime import datetime
import enum
class EnumBimester(enum.Enum):
  first = 1,
  second = 2,
  third = 3,
  fourth = 4,
  final = 5,
  recuperation = 6

"""
Seed the enum type:
  1
  2
  3
  4
"""