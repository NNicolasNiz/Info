class test:
  def __init__ (self):
    self.variable ="old"
    self.Change(self.variable)
  def Change(self,var):
    self.variable = 'new'
    
obj =test()
print (obj.variable)   
    