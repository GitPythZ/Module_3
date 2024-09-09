data = (4.5, 8.7, True, "book", 8, 10, -11, [True, False])

s = sum(filter(lambda x: isinstance(x, float), data))
print(s)
s = sum(filter(lambda x: type(x) is int, data))
print(s)
# summa_ = 0
# for x in data:
#     if isinstance(x, float):
#         summa_ += x
# # for x in data:
# #     if isinstance(x, float):
# #         summa_ += x
# # for x in data:
# #     if isinstance(x, str):
# #         summa_ += x
# # for x in data:
# #     if isinstance(x, bool):
# #         summa_ += x
# print(summa_)
