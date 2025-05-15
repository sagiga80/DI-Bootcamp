# # # # def check_keywordedarguments(**kwargs):
# # # #     return kwargs

# # # # print(check_keywordedarguments(fruit='apple', ordered= 2))
# # # # print(check_keywordedarguments())

# # # # # >> {'fruit': 'apple', ordered: 2}


# # # def check(a, b, c):
# # #     print(a, b, c)

# # # a = [1,2,3]
# # # check(*a)
# # # # >> 1 2 3 

# # # # a = {'a':'Sarah', 'b': 24}
# # # # check(**a)
# # # # # >> TypeError: check() missing 1 required positional argument: 'c'

# # # a = {'a':'Sarah', 'b':24, 'c': 180}
# # # check(**a)
# # # # >> Sarah 24 180

# # def tasks_manager(*tasks):
# #     for task in tasks:
# #         print(f"today I need to {task}")

# # tasks_manager("clean", "study")

# def party_planner(*args, **kwargs):
#     if args:
#         print('You need to buy: ')
#         for arg in args:
#             print(arg)
#     else:
#         print('there is no food to buy' )

#     if kwargs:
#         print('Party details: ')

#         for key, value in kwargs.items():
#             print(f' {key} : \n {value}')

# party_planner ("Drinks", "Food", People=20, Price=10)
# party_planner ("Drinks", "Food")
# party_planner (People=20, Price=10)

# party_planner()
