### work with synthetic data
num_user = 500
num_item = 500
ratings = np.zeros((num_user,num_item))
for u in range(num_user):
    au  = np.random.normal(3,1,1)
    bu = np.random.normal(0.5,0.5, 1)
    for i in range(num_item):
        ti = np.random.normal(0.1,1,1)
        eij = np.random.normal(0,1,1)

        a= au+bu*ti+eij
        ratings[u][i]= max(min(round(a),5),1)

column_names=['item'+str(j) for j in range(ratings.shape[1])]
indexes = ['user'+str(i) for i in range(ratings.shape[0])]
Data = pd.DataFrame(ratings,index=indexes,columns=column_names)


Time_range = 40  ## split the ratings into 40 time range
column_names=['item'+str(j) for j in range(ratings.shape[1])]
indexes = ['user'+str(i) for i in range(ratings.shape[0])]
rated_time = np.random.randint(1,Time_range,size=(ratings.shape[0],ratings.shape[1]))
Rated_Time = pd.DataFrame(rated_time,index=indexes,columns=column_names)
Data_with_time = Rated_Time
