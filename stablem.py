import random

nruns = 10

for i in range(nruns):    #iterate for nruns
  pop = 400               #set population
  
  class woman:  
    def __init__(self, ident, pref):
      self.ident = ident      #identity
      self.pref = pref        #preference list
      self.reject = True      #rejection status
      self.r_count = 0        #which preference is each woman on?
  
  class man:  
    def __init__(self, ident, pref):
      self.ident = ident
      self.pref = pref
      self.tent = None        #tentative partner
      self.prop = []          #proposal list each day
  
  def createWomen(n):
    w = []
    for i in range(n):
      p = random.sample(list(range(n)), k = n   )
      w.append(woman(i,p))    #create women with random preferences
      i += 1
    return w
  
  def createMen(n):
    m = []
    for i in range(n):
      p = random.sample(list(range(n)), k = n   )
      m.append(man(i,p))
      i += 1
    return m
  
  women = createWomen(pop)    #making lists
  men = createMen(pop)
  
  allPaired = False
  
  day = 0
  while not allPaired:
    
    for i in women:     #proposals
      if i.reject == True:    #only rejected women propose
        for j in men:
          if i.pref[i.r_count] == j.ident:
            j.prop.append(    i.ident   )
            j.prop.append(    j.tent    )
      
    for j in men:       #men accept proposal or stay
      for k in j.pref:
        if k in j.prop:
          j.tent = k
          break         #the first proposal in his pref list is assigned
      j.prop = []       #proposals are cleared
    
    
    for i in women:     #rejecting proposals
      i.reject = True   #set every woman to rejected
      for j in men:
        if i.pref[i.r_count] == j.ident and i.ident == j.tent:
          i.reject = False    #rejected if she proposed and is not tentative
      if i.reject == True:
        i.r_count += 1        #after all rejections instruct rejected to move on
    
    for i in women:           #check if all are paired 
      allPaired = False       #assume not
      if i.reject == True:    #if any woman rejected, exit loop
        break
      allPaired = True        #if no woman rejected, loop ends here
      
    day += 1                  #day ends
      
  def printALL(w, m):
    print("Women:")
    for i in w:
      print(i.ident, i.reject, i.r_count)
    #print("\nMen:")
    #for i in m:
      #print(i.ident, i.tent) 
  
  print(day)
  #printALL(women, men)
  
