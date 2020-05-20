# from imageai.Prediction import ImagePrediction

# import os

# execution_path = os.getcwd()

# prediction = ImagePrediction()

# prediction.setModelTypeAsResNet()

# prediction.setModelPath( "C:\\Users\\cw263\\OneDrive\\Desktop\\NSO_LIFE\\resnet50_weights_tf_dim_ordering_tf_kernels.h5")

# prediction.loadModel()





# predictions, percentage_probabilities = prediction.predictImage("C:\\Users\\cw263\\OneDrive\\Desktop\\image.jpg", result_count=5)

# for index in range(len(predictions)):

#  print(predictions[index] , " : " , percentage_probabilities[index])
#import torch
# from detecto import core, utils, visualize

# image = utils.read_image('C:\\Users\\cw263\\OneDrive\\Desktop\\image.jpg')
# model = core.Model()

# labels, boxes, scores = model.predict_top(image)
# visualize.show_labeled_image(image, boxes, labels)
#print(torch.cuda.is_available())
from detecto import core, utils, visualize
dataset = core.Dataset('images/')
model = core.Model(['chris'])
model.fit(dataset)
image = utils.read_image('images/christopher.jpg')
predictions = model.predict(image)
labels, boxes, scores = predictions
print(labels) 
