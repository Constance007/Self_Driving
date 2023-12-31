from utlis import*
from sklearn.model_selection import train_test_split
# Step 1
path = 'myData'
data = importDataInfo(path)

# Step 2
data = balanceData(data, display=False)

# Step 3
imagesPath, steerings = loadData(path, data)
#print(imagesPath[0], steering[0])

# Step 4
xTrain, xVal, yTrain, yVal = train_test_split(imagesPath, steerings, test_size=0.2, random_state=5)
print('Total Training images: ', len(xTrain))
print('Total Validation images: ', len(xVal))
# Step 5

# Step 6

# Step 7

# Step 8
model = createModel()
model.summary()

