from datetime import datetime

from numplate.models import CarPlate
from extractMod import extractImg

number = extractImg()

car = CarPlate()
car.numplate = number
car.inTime = datetime.now()
car.outTime = datetime.now()
car.save()

