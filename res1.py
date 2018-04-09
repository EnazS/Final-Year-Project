import csv
import matplotlib.pyplot as plt

def initial_data_graph():
    x = []
    y = []
    k = []
    z = []
    f = open('data/crimeRate_predict_n.csv')
    reader_demo = csv.DictReader(f)
    for row in reader_demo:
        x.append(int(row['Community #']))
        y.append((row['crime_rate']))
	k.append((row['Linear']))
	z.append((row['NegativeB']))
        plt.ylim(0,0.5)
        plt.xlim(1,77)
    plt.xlabel('CommunityArea#')
    plt.ylabel('CrimeRate')
    plt.plot(x,y,color='r')
    plt.plot(x,k,color='g')
    plt.plot(x,z,color='b')
    plt.show()

if __name__ == '__main__':
    initial_data_graph()
