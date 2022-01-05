# Gradient Descent

The descent of the gradient allows to optimize a function, that is, to find the minimum of a cost function. Gradient descent can be applied in different measurements, however in this example only 2 will be used for practical purposes.

![image](https://user-images.githubusercontent.com/78567418/148282379-1c4a2a88-e668-4455-aeb7-277cf7f72459.png)

## Cartesian plane

![image](https://user-images.githubusercontent.com/78567418/148282501-bc6be9d8-22d2-4fc1-a1ec-01c3f8b2a219.png)

## Considerations

If the learning rate is very small, the algorithm requires more iterations to reduce the cost function, which means that it will take more time.

![image](https://user-images.githubusercontent.com/78567418/148282651-593bfc9b-13c6-4050-ac36-d4c43c186561.png)

If the Learning Rate is very high, it is possible that it will jump above the minimum value and end up at another point, possibly higher than before, which means that you will not find a good solution.

![image](https://user-images.githubusercontent.com/78567418/148283588-a4f68820-dfce-41e3-a384-f25f26ae36b5.png)

## Principal Disvantage

The method of Gradient Descent just return the local minimum of function, in this particular case it's easy to say which it's the minimum values.

# Execution

## Function

f(x,y) = x^2 + y^2

![image](https://user-images.githubusercontent.com/78567418/148285167-86183748-31b8-455b-9a6d-07e0052e06d4.png)

## Gradient Descent

![image](https://user-images.githubusercontent.com/78567418/148285692-e2a8abbd-6c42-4e24-be17-e4c07e13b24c.png)

