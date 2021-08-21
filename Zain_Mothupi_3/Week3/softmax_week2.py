import numpy as np

class Softmax:
    # A standard fully-connected layer with softmax activation


    def __init__(self, input_len, nodes):
        # we divide by input_len to reduce the variance of our initial values

        self.weights = np.random.randn(input_len, nodes)/ input_len

        self.biases = np.zeros(nodes)


    def forward(self, input):
        ''' Performs a forward pass of the softmax layer using the given input.
            Returns a 1d numpy array containing the respective probabillity values.
            - input can be an array with any dimensions '''
        
         # perform forward phase caching (storing current data input as 'last input') to be used in the backpropagation phase
        self.last_input_shape = input.shape
        

        input = input.flatten() # we flatten the input to make it easier to work with since we no longer need its shape
        self.last_input = input #store current flattened input as 'last input' to be used in the backpropagation phase

        input_len, nodes = self.weights.shape

        totals = np.dot(input, self.weights) + self.biases
        self.last_totals = totals #store current totals as 'last_totals' to be used in the bacpropagation phase

        
        exp = np.exp(totals)
        return exp/np.sum(exp, axis=0)


    def backdrop(self, d_L_d_out):

        ''' Performs a backward pass of the softmax layer.
        Returns the loss gradient for this layer's inputs.
        - d_L_d_out is the loss gradient for this layer's inputs
        - learn rate is a float
        (partial derivative of Loss w.r.to the output probability of Softmax forward pass) '''

        # We know only 1 element of d_L_d_out will be nonzero
        for i, gradient in enumerate(d_L_d_out):
            
            if gradient == 0:
                continue

            # e^totals (i.e., w1*x1 + w2*x2 + . . + b)
            t_exp = np.exp(self.last_totals)

            # Sum of all totals
            S = np.sum(t_exp)

            # Gradients of out[i] against totals
            d_out_d_t    = -t_exp[i] * t_exp / (S**2)
            d_out_d_t[i] =  t_exp[i] * (S - t_exp[i]) / (S**2)

            # Gradients of totals against weights/biases/input
            d_t_d_w = self.last_input
            d_t_d_b = 1
            d_t_d_inputs = self.weights
            
            #Gradients of loss against totals
            d_L_d_t = gradient * d_out_d_t

            # Gradients of loss against weights/biases/input
            d_L_d_w = d_t_d_w[np.newaxis].T @ d_L_d_t[np.newaxis]
            d_L_d_b = d_L_d_t * d_t_d_b
            d_L_d_inputs = d_t_d_inputs @ d_L_d_t

            # Update weights/biases

            self.weights -= learn_rate * d_L_d_w
            self.biases -= learn_rate * d_L_d_b
            return d_L_d_inputs.reshape(self.last_input_shape)

            
            
            


        

            
            
            

        
        

    










        
        
