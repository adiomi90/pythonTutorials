class TagCloud:

    def __init__(self):
        self.__tags = {}
        

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1
        

    def __getitem__(self,key):
        return self.__tags.get(key.lower(),0)
    

    def __setitem__(self,key, value):
        self.__tags[key.lower()] = value
        

    def __len__(self):
        return len(self.__tags)
    

    def __iter__(self):
        return iter(self.__tags)
    
    
        
    
        

cloud = TagCloud()
cloud.add("particles")
cloud.add("particles")
cloud.add("particles")
cloud.add("particles")
cloud.add("particles")

cloud.add("ink baby")

cloud.add("sick with it")
cloud.add("gold")


particles = cloud["particles"]

cloud["gold"] = 15

print(cloud.__tags)

print("the length ",len(cloud))

print(particles)



for x in cloud.__tags.items():

    print(x)

#accessing private member
# cloud.__dict__