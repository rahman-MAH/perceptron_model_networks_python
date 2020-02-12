# This is the perceptron model which was proposed by Rosenblatt.

# It is a more general computational model than MP neuron model.

# This code generates output with respect to only one case at a time.
# Here x1 = first elements of functional bi-polar table
#      x2 = second elements of functional bi-polar table
#      t = targeted output of the functional bi-polar table In
# this code if you want to assign your own weights then you can do it when the output window shows do you wan to
# change weights.
# You can cross verify you weights to check if the new weights are satisfying the whole functional bi-polar table


global x1, x2, t, w1_old, w2_old, b, a, th_val, net_input, activation_function, y, w1_new, w2_new, b_new
x1 = int(input('Enter an element x1 : '))
x2 = int(input('Enter an elements x2: '))
t = int(input('Enter a targeted output : '))
user_input = input('Do you want to enter weights?(Y/N) ')
if user_input == "Y" or "y":
    b = int(input('Enter base b weight : '))
    w1_old = int(input('Assign first weight : '))
    w2_old = int(input('Assign second weight : '))
else:
    b = 0
    w1_old = 0
    w2_old = 0
th_val = int(input('Enter threshold value = '))

print('First input= ', x1)
print('Second input= ', x2)
print('Targeted output= ', t)
print('Assigned weights= ', b, w1_old, w2_old)
print('Threshold value= ', th_val)
x = x1*w1_old
y = x2*w2_old
net_input = b + x + y
print('net input =', net_input)
if net_input > th_val:
    activation_function = 1  # f(net_input) = 1
elif net_input < th_val:
    activation_function = -1  # f(net_input) = -1
else:
    activation_function = 0  # f(net_input) = 0

y = activation_function
print('Activation function =', y)
print('Checking if y=t')
if y == t:
    print(' Checked and no need to change/update weights')
else:
    print('Checked and need to change/update weights')
    a = int(input("Enter learning rate : "))
    w1_new = w1_old + a * t * x1
    w2_new = w2_old + a * t * x2
    b_new = b + a * t
    print('New weights', b_new, w1_new, w2_new)

