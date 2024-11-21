from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from collections import Counter
from lib.utils import generate_positive_sample

class PlantSetBase(BaseModel):
  set_name: str
  planting_date: datetime
  average_flowering_day: int
  standard_deviation_flowering_day: int
  total_plants: int
  average_flowers_per_plant: int
  standard_deviation_flowers_per_plant: int

class PlantSet(PlantSetBase):
  flowers_per_plant: List = []
  flowering_days: List = []
  flattened_flowering_days: List = []
  flowering_days_counter: Optional[Counter] = None

  def get_flowers_per_plant(self):
    self.flowers_per_plant = [generate_positive_sample(self.average_flowers_per_plant, self.standard_deviation_flowers_per_plant) for _ in range(self.total_plants)]
    
  def get_flowering_days(self):
    self.flowering_days = [[generate_positive_sample(self.average_flowering_day, self.standard_deviation_flowering_day) for _ in range(round(flower_count))] for flower_count in self.flowers_per_plant]
  
  def get_flattened_flowering_days(self):
    self.flattened_flowering_days = [round(item) for sublist in self.flowering_days for item in sublist]
  
  def get_flowering_days_counter(self):
    self.flowering_days_counter = Counter(self.flattened_flowering_days)
  