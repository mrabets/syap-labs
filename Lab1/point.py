class Point:
  def __init__(self, points):
    self.points = points
    
  def find_max(self):
    return max(self.__distances())
  
  def __distances(self):
    distances = []
    
    for p in points: 
      distances.append(abs(p[0] - p[1]))
      
    return distances
    	

points = [[2, 7], [3, 5], [8, 2], [1, 1]]

p = Point(points)
print(p.find_max())

