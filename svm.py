import matplotlib.pyplot as plt 
from matplotlib import style 
import numpy as np

style.use('ggplot')

class Support_Vector_Machine:
    def __init__(self,visualization=True):
        self.visualization=visualization
        self.colors = {1:'r',-1:'b'}#Allow 2 hyperplanes to set with diff col
        if self.visualization:
            self.fig=plt.figure()
            self.ax=self.fig.add_subplot(1,1,1)
    #Training data, data means feasures : x
    def fit(self, data):
        self.data =data
        #{ ||w||:[w,b]}
        opt_dict = {}#Set our dictionary for saving w and b
        transforms = [[1,1], [1,-1],[-1,-1],[-1,1]]
        all_data = []
        for yi in self.data:
            for feasureset in self.data[yi]:
                for feasure in feasureset:
                    all_data.append(feasure)
        self.max_feasure_value = max(all_data)
        self.min_feasure_value = min(all_data)
        all_data = None

        step_sizes = [self.max_feasure_value*0.1,
                      self.max_feasure_value*0.01,
                      self.max_feasure_value*0.001]
        #Extremely expensive
        b_range_multiple = 5
        #
        b_multiple = 5

        latest_optimum = self.max_feasure_value*10
        for step in step_sizes:
            w = np.array([latest_optimum,latest_optimum])
            #We can do this because convex
            optimized = False
            while not optimized: 
                for b in np.arange(-1*(self.max_feasure_value*b_range_multiple),
                                   self.max_feasure_value*b_range_multiple,
                                   step*b_multiple):
                    for transformation in transforms:
                        w_t = w*transformation
                        found_option = True
                        # weakest link in the SVM fundamentally
                        # SMO attempts to fix this a bit
                        # yi(xi.w+b) >= 1
                        # 
                        # #### add a break here later..
                        for i in self.data:
                            for xi in self.data[i]:
                                yi=i
                                if not yi*(np.dot(w_t,xi)+b) >= 1:
                                    found_option = False
                                    
                        if found_option:
                            opt_dict[np.linalg.norm(w_t)] = [w_t,b]

                if w[0] < 0:
                    optimized = True
                    print('Optimized a step.')
                else:
                    w = w - step

            norms = sorted([n for n in opt_dict])
            #||w|| : [w,b]
            opt_choice = opt_dict[norms[0]]
            self.w = opt_choice[0]
            self.b = opt_choice[1]
            latest_optimum = opt_choice[0][0]+step*2
    # sign(x.w+b). 
    # Feasures represents the values to classify; We don't know w and b yet
    def predict(self,feasures):
        classification = np.sign(np.dot(np.array(feasures),self.w)+self.b)
        if classification !=0 and self.visualization:
            self.ax.scatter(feasures[0],feasures[1],s=200,marker='*', c=self.colors[classification])
        return classification
    def visualize(self):
        [[self.ax.scatter(x[0],x[1],s=100,color=self.colors[i]) for x  in data_dict[i]] for i in data_dict]
        #hyperplate = 
        def hyperplanes(x,w,b,v):
            return (-w[0]*x-b+v)/w[1]
        datarange = (self.min_feasure_value*0.9, self.max_feasure_value*1.1)
        hyp_x_min = datarange[0]
        hyp_x_max = datarange[1]

        psv1 = hyperplanes(hyp_x_min,self.w,self.b,1)
        psv2 = hyperplanes(hyp_x_max,self.w,self.b,1)
        self.ax.plot([],[hyp_x_min, hyp_x_max],[psv1,psv2])

        nsv1 = hyperplanes(hyp_x_min,self.w,self.b,1)
        nsv2 = hyperplanes(hyp_x_max,self.w,self.b,1)
        self.ax.plot([],[hyp_x_min, hyp_x_max],[nsv1,nsv2])

        db1 = hyperplanes(hyp_x_min,self.w,self.b,1)
        db2 = hyperplanes(hyp_x_max,self.w,self.b,1)
        self.ax.plot([],[hyp_x_min, hyp_x_max],[db1,db2])

        plt.show()

#Set the dataset we'll be using for both -1 and 1 classes
data_dict = {-1:np.array([[1,7],
                         [2,8],
                         [3,8],]),
            1:np.array([[5,1],
                        [6,-1],
                        [7,3],])}

svm = Support_Vector_Machine()
svm.fit(data = data_dict)
svm.visualize()