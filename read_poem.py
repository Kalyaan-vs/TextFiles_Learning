# jabber = open("Jabberwocky.txt", 'r')
# for line in jabber:
#     print(line.strip())
#     # print(line, end="")
# jabber.close()

# with open("Jabberwocky.txt", 'r') as jabber:
#     # for line in jabber:
#         # print(line.rstrip())
#     lines = jabber.readlines()
#
# print(lines)
# print(lines[-1::-1])
#
# for line in reversed(lines):
#     print(line, end="")  # do some processing in reverse order
#
# with open("Jabberwocky.txt") as jabber:
#     # read() returns the characters in a single string
#     text = jabber.read()
#
# print(text)
# # returns the whole string in reverse.
# for line in reversed(text):
#     print(line, end="")

#
# print("*" * 80)
# print()
#
# with open("Jabberwocky.txt") as jabber:
#     for line in jabber:
#         print(line.rstrip())
#         if "jubjub" in line.casefold():
#             break

# with open("Jabberwocky.txt") as jabber:
#     # line = jabber.readline()
#     # while line:
#     #     print(line.rstrip())
#     #     line = jabber.readline()
#     while True:
#         line = jabber.readline()
#         print(line.rstrip())
#         if not line:
#             break
#
# with open("Jabberwocky.txt", encoding="windows-1252") as jabber:
#     for line in jabber:
#         print(line.rstrip())
