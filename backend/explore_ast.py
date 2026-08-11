import ast

# while True:
#     code = input ('\n Enter python code (or quit):')
#     if code == 'quit':
#         break
#     tree = ast.parse(code)
#     print(ast.dump(tree, indent=5))

# paste when it asked for Enter python code (or quit):
# if x > 3:
#    y = 1
# else:
#    y = 2
# Why it broke: input() reads exactly ONE line. You pasted 4 lines, but your tool only received the first one: if x > 3:. The other 3 never made it in.
# Why this error: ast.parse got an if with a colon but nothing after it. Even though ast.parse never runs code, it still demands complete grammar — an if must have a body. "IndentationError: expected an indented block" is Python saying "you promised me indented lines after that colon, and there aren't any."

# So the tool has outgrown its design: it was built for one-liners, and we now need multi-line code. Comment out above single loop 

# New plan: keep reading lines until you enter an empty line, then glue them together and parse the whole thing. Three new pieces you'll need:

# A list — lines = [] makes an empty container that holds items in order. Like an empty shopping basket.

#.append() — lines.append(line) drops one more item into the basket, at the end.

#"\n".join(lines) — glues all the basket's items back into one text, with a newline character (\n = "press Enter") between each. ["a", "b"] becomes "a\nb".

# And one structural idea: a loop inside a loop. Outer loop = one round per snippet (the cashier serving customers). Inner loop = collecting the lines of one snippet (scanning all items in one customer's basket). A break only exits the loop it's inside — the inner break ends line-collecting, not the whole program.

while True:
    print("Enter python code (empty line to finish, quit to exit):")
    lines=[]
    while True:
        line = input()
        if line =="":
            break
        lines.append(line)

    if lines == ['quit']:
        break
    code = "\n".join(lines)
    tree=ast.parse(code)
    print(ast.dump(tree,indent=2))
        