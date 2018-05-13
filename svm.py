import matplotlib.pyplot as plt 
from matplotlib import style 
import numpy as np

style.use('ggplot')

class Support_Vector_Machine:
    def __init__(self,visualization=True):
        self.visualization=visualization
        self.colors = {1:'r',-1:'b'}
        if self.visualization:
            self.fig=plt.figure()
            self.ax=self.fig.add_subplot(1,1,1)
    #Train
    def fit(self, data):
        self.data =data
        pass
    # sign(x.w+b). 
    # Feasures represents the values to classify; We don't know w and b yet
    def predict(self,feasures):
        classification = np.sign(np.dot(np.array(feasures),self.w)+self.b)
        return classification

#Set the dataset we'll be using for both -1 and 1 classes
data_dict = {-1:np.array([[1,7],
                         [2,8],
                         [3,8],]),
            1:np.array([[5,1],
                        [6,-1],
                        [7,3],])}