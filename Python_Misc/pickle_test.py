import pickle

class Company(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

with open('company_data.pkl', 'wb') as outp:
    company1 = Company('banana', 40)
    pickle.dump(company1, outp, pickle.HIGHEST_PROTOCOL)

    company2 = Company('spam', 42)
    pickle.dump(company2, outp, pickle.HIGHEST_PROTOCOL)

del company1
del company2

with open('company_data.pkl', 'rb') as inp:
    company1 = pickle.load(inp)
    print(company1.name)  # -> banana
    print(company1.value)  # -> 40

    company2 = pickle.load(inp)
    print(company2.name) # -> spam
    print(company2.value)  # -> 42

def save_object(obj, filename):
    with open(filename, 'wb') as outp:  # Overwrites any existing file.
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)

# sample usage
save_object(company1, 'company1.pkl')
save_object(company2, 'company1.pkl')
