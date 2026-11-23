import torch
import torch.nn as nn

# dropout_layer = nn.Dropout(p=0.5)

# t1 = torch.Tensor([1,2,3])
# t2 = dropout_layer(t1)
# print(t2) #tensor([2., 0., 6.]) tensor([2., 4., 0.]) 随机

# dropout_layer2 = nn.Dropout(p=0.3)
# t3 = dropout_layer(t1)
# print(t3) #tensor([0., 4., 0.]) tensor([2., 4., 6.])  tensor([2., 0., 0.])随机

# layer = nn.Linear(in_features=3, out_features=5, bias=True)
# t1 = torch.Tensor([1,2,3]) #shape(3, )

# t2 = torch.Tensor([[1,2,3]]) # shape: (1,3)

# output2 = layer(t2)
# print(output2) #tensor([[-2.2133,  1.5173,  0.3434,  1.3548,  0.6632]],

# t = torch.tensor([[1,2,3,4,5,6],[7,8,9,10,11,12]]) #[2,6]
# t_view1 = t.view(3,4)
# print(t_view1)
# t_view2 = t.view(4,3)
# print(t_view2)

# '''
# tensor([[ 1,  2,  3,  4],
#         [ 5,  6,  7,  8],
#         [ 9, 10, 11, 12]])
# tensor([[ 1,  2,  3],
#         [ 4,  5,  6],
#         [ 7,  8,  9],
#         [10, 11, 12]])
# '''

# t1 = torch.Tensor([[1,2,3],[4,5,6]]) #[2,3]
# t1 = t1.transpose(0,1)
# print(t1)
# '''
# tensor([[1., 4.],
#         [2., 5.],
#         [3., 6.]])
# '''

# x = torch.tensor([[1,2,3],[4,5,6],[7,8,9]])
# print(torch.triu(x))
# '''
# tensor([[1, 2, 3],
#         [0, 5, 6],
#         [0, 0, 9]])
# '''

# print(torch.triu(x, diagonal=1))
# '''
# tensor([[0, 2, 3],
#         [0, 0, 6],
#         [0, 0, 0]])
# '''

# x = torch.arange(1,7)
# y = torch.reshape(x,(2,3))
# print(y)
# '''
# tensor([[1, 2, 3],
#         [4, 5, 6]])
# '''
# z = torch.reshape(x,(3,-1))
# print(z)
# '''
# tensor([[1, 2],
#         [3, 4],
#         [5, 6]])
# '''
