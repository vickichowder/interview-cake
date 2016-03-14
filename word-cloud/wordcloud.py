import string, re

class cloud:
    def __init__(self, data):
        self.data = data
        self.cloud = {}
        self.fluffy()
        self.compress()

    def fluffy(self):
        for item in self.data:
            self.add(filter(None, re.split("[, !?:.\?!()&*$/\"#@^%~`]+", item)))

    def add(self, item):
        for word in item:
            if word.lower() not in self.cloud:
                self.cloud[word.lower()] = [0,0]

            self.increment(word)

    def compress(self):
        tempCloud = {}
        for key, value in self.cloud.iteritems():
            if value[0] < value[1]:
                tempCloud[key.capitalize()] = value[0] + value[1]
            else:
                tempCloud[key] = value[0] + value[1]

        self.cloud = tempCloud

    def increment(self, word):
        if word.islower():
            self.cloud[word.lower()][0] += 1
        else:
            self.cloud[word.lower()][1] += 1

def execute():
    lines = [ 'We came, we saw, we conquered...then we ate\
        Bill\'s (Mille-Feuille) "CAKE" CAKE.']
    cloudData = cloud(lines)

    print(cloudData.cloud)

execute()
