from cocciep.db import db
from datetime import datetime
import enum

class EnumSubjects(enum.Enum):
  MATH = "math",
  PORTUGUESE = "portugues",
  HISTORY = "history"
  GEOGRAPHY = "geography"
  ENGLISH = "english"
  TECHNICAL_DRAWING = "technical drawing"
  PHYSICAL_EDUCATION = "physical education"
  BIOLOGY = "biology"
  PHYSICS = "physics"
  CHEMISTRY = "chemistry"
  SPANISH = "spanish"
  SCIENCES = "sciences"
  ARTS = "arts"
