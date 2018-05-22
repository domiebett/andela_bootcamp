class Car(object):

  def __init__(self, name='General', model='GM', vehicle_type=None):
    self.name = name
    self.model = model
    self.vehicle_type = vehicle_type
    self.speed = 0

    #assigns 2 doors to Porshe and Koenigsegg, and 4 to the rest.

    if self.name=="Porshe" or self.name=="Koenigsegg":
      self.num_of_doors = 2
    else:
      self.num_of_doors = 4

    #assigns 8 wheels to trailers, and 4 wheels to saloon cars
    if self.vehicle_type == 'trailer':
      self.num_of_wheels = 8
    else:
      self.num_of_wheels = 4

    #speed assigned to instance of car depending on its moving speed.

  def drive(self, moving_speed):
    if moving_speed == 3:
      self.speed = 1000
    elif moving_speed == 7:
      self.speed = 77

    return self

    #if vehicle_type is not trailer, or is still None, then it is a saloon

  def is_saloon(self):
    if self.vehicle_type is not 'trailer':
        self.vehicle_type == 'saloon'
        return True
    return False

  
