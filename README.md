# LORA-Tech-Application

## Essay:
Linear Regression operates on an assumption that there is a linear relationship between features and the required output, with error being normalised with 0 mean and constant variance. Linear Regression focuses on calculating the parameters that define this linear relationship. The parameters are in the form:
Y = B0 + B1X1 + B2X2 +... .
It is relatively easy to explain a linear model, its assumptions, and why the output is what it is, making it more intuitive to explain to a client. However, it cannot work with complex non-linear relationships.

A Neural Network can work with non-linear relationships. The key difference in a neural network is that each linear calculation for a node is input into a non-linear activation function. Each node in a layer may be caculated in this form:
L1 = a0(W1X1 + W2X2 + W3X3 + ...), with Xi being the value of a node in the previous layer and Wi being a constant weight. A neural network can be made highly parameterised with multiple layers and multiple nodes. Thus, a neural network may give a more accurate result for non-linear models at the cost of increased complexity.

A convoluted neural network is a type of neural network with one or more layers of convolution nodes. A convolution node is a node that can receive an input from multiple nodes (and even all nodes) in the previous layer. These inout units share their weights and form a small neighbourhood. Thus, convoluted nodes are able to consider the context/shared information in the small neighborhoods, making them useful for image, video, text, speech etc. These one-to-many mappings can allow reducing the number of total nodes in the network and reduce parameters. This reduced complexiity can reduce overfitting.