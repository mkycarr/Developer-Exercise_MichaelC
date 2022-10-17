
from array import array
from email import contentmanager
from email.charset import QP
import math
from examples import simple_example


import pandas as pd

class NearestNeighborIndex:
    """
    TODO give me a decent comment

    NearestNeighborIndex is intended to index a set of provided points to provide fast nearest
    neighbor lookup. For now, it is simply a stub that performs an inefficient traversal of all
    points every time.
    """

    def __init__(self, points):
        """
        takes an array of 2d tuples as input points to be indexed.
        """
        self.points = points

    @staticmethod
    def find_nearest_slow(query_point, haystack):
        """
        find_nearest_slow returns the point that is closest to query_point. If there are no indexed
        points, None is returned.
        """
        min_dist = None
        min_point = None
        for point in haystack:
            deltax = point[0] - query_point[0]
            deltay = point[1] - query_point[1]
            dist = math.sqrt(deltax * deltax + deltay * deltay)

            if min_dist is None or dist < min_dist:
                min_dist = dist
                min_point = point

        return min_point

    def find_nearest(query_point,haystack):
        """
        find nearest returns the closest point to the query point.
        It determines closest points withing a range for x and y axis.
        Then performs calculations.
        """
        #create list for query point and haystack.
        qp= list(query_point)
        hay= list(haystack)
        #create empty list to append filtered values too
        filtered= list()
        #create min/max values for X axis
        x_min=qp[0]-100
        x_max= qp[0]+100
        #create min/max values for Y axis
        y_min= qp[1]-100
        y_max= qp[1]+100
        #filter through haystack to find closest values that would be closest to querypoint
        #append filtered list
        for row in hay:
            if row[0] >= x_min and row[0] <= x_max:
                if row[1] >= y_min and row[1] <= y_max:
                    filtered.append(row)


        #calculate the euclidean distance of filtered points
        #loop through points to find min distance and return min point
        min_dist = None
        min_point = None
        #loop through set of filtered points to determine nearest neighbor.
        for point in filtered:
            deltax = point[0] - qp[0]
            deltay = point[1] - qp[1]
            dist = math.sqrt(deltax * deltax + deltay * deltay)

            if min_dist is None or dist < min_dist:
                min_dist = dist
                min_point = point

        #write the query point and nearest neighbor to csv file.
        content= ('Query Point:',query_point,'Nearest Neighbor:',min_point)
        simple_example.write_file(content)

        return min_point



##below is a nearest neighbor implementation, but ran entirely too slow.
        '''
        #print('newhay:\n',hay)
        # print(hay[:,0])

        df0= pd.DataFrame(qp)
        df1= pd.DataFrame(haystack)
        frames = [df0, df1]
        final = pd.concat(frames).sort_values(by=0, ascending=True)
        get= final[0].where(final[0] == query_point[0])
        l_iter = get[0]
        print(next(l_iter))
        print(final)


        qp= [(query_point[0],query_point[1])]
        print('qp:',qp )
        hay= list(haystack)

        x = min(hay,qp)

        min_dist = None
        min_point = None

        for point in haystack:
            deltax = point[0] - query_point[0]
            deltay = point[1] - query_point[1]
            dist= ((deltax * deltax + deltay * deltay)**.5)
           # dist = math.sqrt(deltax * deltax + deltay * deltay)


            if min_dist is None or dist < min_dist:
                min_dist = dist
                min_point = point

        return min_point


        df = pd.DataFrame( columns=['col1', 'col2','col3'])
        # calculate the Euclidean distance between two vectors
        def euclidean_distance(query_point, haystack):
            col1= (query_point)
            col2= (haystack)
            distance = 0.0

            for i in range(len(query_point)-1):
                dist= distance+ (col1[i] - col2[i])**2
                #dist= math.dist(query_point,haystack)

            return(dist)
            #return(math.sqrt(distance))
        #target point to calculate distance from
        row0 = (query_point[0],query_point[1])

        #get eucl distance from first datapoint to rest in test_points
        coll1= []
        coll2= []
        coll3= []
        min_dist=None
        min_point= None
        for point in haystack:
            coll1.append(row0)
            coll2.append(point)
            dist = euclidean_distance(row0,point)
            coll3.append(dist)
            if min_dist is None or dist < min_dist:
                min_dist = dist
                min_point = point

        #print('col:',coll1)
        #print('col2:',coll2)
        #print('col3',coll3)
        df['col1']= coll1
        df['col2']= coll2
        df['col3']= coll3

        final_df = df.sort_values(by=['col3'], ascending=True)
        print(final_df)
        '''