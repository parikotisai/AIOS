import ast

def show_tree(code):
    print(f'\n---Code: {code}')
    tree=ast.parse(code) # turns the text into tree
    print(ast.dump(tree, indent=2)) # prints that tree so you can see it

show_tree("x = 5")
show_tree("y=x-3")
show_tree("print(y)")
# ast.parse - takes code as text and gives back the tree
# ast.dump  - the tree is a python object you cant read directly; dump prints it so we can read

show_tree('x = "hello"')
show_tree("z= x * y")
show_tree("print(x, y)")

