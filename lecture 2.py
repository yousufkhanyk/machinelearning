light = input(' Enter the traffic light color (red, yellow, green): ').lower()

  if light == 'red':
     action = 'Stop'
  elif light == 'yellow':
     action = 'Caution'
  elif light == 'green':
     action = 'Go'
else:
action = ' Invalid color'

print(f' The light is {light}. You should {action}.')