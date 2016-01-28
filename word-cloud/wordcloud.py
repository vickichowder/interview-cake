lines = ['After beating the eggs, Dana read the next step:','Add milk and eggs, then add flour and sugar.']

class cloud:
    def __init__(self, data):
        self.data = data
        self.cloud = {}
        self.fluffy()
        
    def fluffy(self):
        for item in self.data:
            self.add(item.split(' '))
    
    def add(self, item):
        for word in item:
        	word = self.clean(word)
        	if word in self.cloud:
        		self.cloud[word] += 1
        	else:
        		self.cloud[word] = 1
    
    def clean(self, word):
    	return word.lower().replace(',', '').replace('.', '').replace(':', '').replace('!', '').replace(';', '').replace('?', '')

clouddata = cloud(lines)
print(clouddata.cloud)
            
