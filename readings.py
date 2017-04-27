import sys
import numpy

def get_filename():
    script = sys.argv[0]
    filename = sys.argv[1]
    return filename

def load_data(filename):
    print('Loading data...')
    return numpy.loadtxt(filename, delimiter=',')

def print_mean(filename):
    print('Printing means...')
    data = load_data(filename)
    for m in numpy.mean(data, axis=1):
        print(m)

if __name__ == '__main__':
    filename = get_filename()
    print_mean(filename)
