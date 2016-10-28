'''
pyio.py

python input output. load data and save data using pickle.

'''
import pickle

def loaddata(filename):
    '''
    load pickle file into python

    filename (string)
    '''
    output = pickle.load(open(filename, 'rb'))

    return output


def savedata(filename, data):
    '''
    save data to pickle file

    filename (string)
    data (list)
    '''

    pickle.dump(data, open(filename, 'wb'))

def writetotext(filename, string):
    '''
    write text string to file
    '''
    f = open(filename, 'w')
    f.write(string)
    f.close()
    return
