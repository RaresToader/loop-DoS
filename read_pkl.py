import pickle
import pprint

f = open('ntp_ALL_identified_cycles.pkl', 'rb')
d = pickle.load(f)
pprint.pprint(d)