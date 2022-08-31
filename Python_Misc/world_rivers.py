class River:
    def __init__(self, name, continent, length):
        self.name = name
        self.continent = continent
        self.length = length

    def __str__(self):
        return ('The ' + str(self.name) + ' is a river in ' + str(self.continent)\
                + ' having length ' + str(self.length) + ' km.')

nile = River('Nile', 'Africa', 6690)
amazon = River('Amazon', 'South America', 6296)
mississippi = River('Mississippi', 'North America', 5970)
yangtze = River('Yangtze', 'Asia', 5797)
ob = River('Ob', 'Asia', 5567)
columbia = River('Columbia', 'North America', 1983)

def by_continent(lst, continent):
    new_list = []
    for r in lst:
        if r.continent == continent:
            new_list.append(r)
    return new_list
        
