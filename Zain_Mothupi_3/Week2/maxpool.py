import numpy as np


class MaxPool2:
    # A max pooling layer using a pool size of 2

    def iterate_regions(self, image):
        '''

        Generates non-overlapping 2x2 image regions to pool over. 
        - image is a 2d numpy array '''

        h,w, _ = image.shape # extract height and width of the convolved image input for a specified kth filter
        new_h = h//2 # the // is a floor division which is normal division except it returns the largest whole number. eg 15/1.19 = 12.605 while 15// 1.19 =12 --notices there is no rounding up
        
        new_w = w//2

        # loop over the cut-by-half (h/2,w/2) due to pooling
        # the new_h and new_w represent the indices of the 2x2 pool square to be scanned across the image
        for i in range(new_h):
            for j in range(new_w):
                # define the im_region as that of the original image size sliced into the (ith, jth) 2x2portions of the original image.
                #access the them via the selection of image array elements in height and width which correspond to the pool
                # the syntax [h1:h2, w1:w2] represent the range in height and widththat define a pool square of 2x2
                im_region = image[(i * 2):(i * 2 + 2), (j * 2):(j * 2 + 2)]
                yield im_region, i, j



    def forward(self, input):
        ''' Performs a forward pass of the maxpool layer using the given input.
            Returns a 3d numpy array with dimensions (h/2, w/2, num_filters)
            - input is a 3d numpy array with dimensions (h, w, num_filters) '''

        h, w, num_filters = input.shape
        output = np.zeros((h//2, w//2, num_filters))

        # loop over each 2x2 pool at the (i,j) location of the image and extract the max value out of said 2x2 pool
        for im_region, i, j in self.iterate_regions(input):
            #extract the max value of the 2x2 pool at the (i,j) location of the image
            #axis = (0,1) -> (h,w) is specified to only find the maximum along the first 2 dimension(h,w) and not a third (num_filters)
            output[i, j] = np.amax(im_region, axis=(0,1))

        return output
