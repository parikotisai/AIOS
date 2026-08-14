import ast
import json

variables = {}

trace = []

def eval_expr(node):
    if isinstance(node, ast.Constant):
        # A literal like 5 - the value is stored inside the node
        return node.value

    elif isinstance(node,ast.Name):
        # a variable being read , like x - look up its current value
        return variables[node.id] #node.id → the name as text: "y". variables["y"] → open the variables dict and fetch the value saved under that key, and return it.

    elif isinstance(node,ast.BinOp):
        left_value = eval_expr(node.left)
        right_value = eval_expr(node.right)

        if isinstance(node.op,ast.Add):
            return left_value + right_value
        elif isinstance(node.op,ast.Sub):
            return left_value - right_value
        elif isinstance(node.op,ast.Mult):
            return left_value * right_value
        elif isinstance(node.op,ast.Div):
            return left_value / right_value
        else:
            raise Exception(f"Wrong operation:{node.op}")
        
    else:
        raise Exception(f"Dont know how to evaluate yet:{node.op}")


def run_statement(node , line_number):
    if isinstance(node, ast.Assign):
        var_name = node.targets[0].id
        value = eval_expr(node.value)
        variables[var_name] = value

        trace.append({
            "step":len(trace)+1,
            "line":line_number,
            "event":"assign",
            "changed":{var_name: value},
            #"variables":variables
            # dict(variables) takes a SNAPSHOT (a copy) of the whiteboard.
            # Storing `variables` directly would store a live link instead —
            # every past step would then silently change whenever a later
            # line updates a variable. Our first bug; caught by expected-vs-actual.
            "variables": dict(variables),

        })
    else:
        raise Exception(f"Dont know how to run this yet:{node}")

code = "x = 15\ny = 5\nz = x+y\nz=x-y\nz=x*y\nz=x/y"
tree = ast.parse(code)

for line_number, statement in enumerate(tree.body, start=1):
    run_statement(statement, line_number)

print(json.dumps(trace, indent=2))

#Read it as: "I claim step 1's photo shows exactly x:5 and nothing else. Check it. If I'm wrong, crash loudly with this message."

# assert = "I claim — verify or crash." trace[0] = the first photo in the album (numbered boxes, position 0!).
# If the claim is true → silence, program continues. Silence is a pass.

assert trace[0]["variables"] == {"x": 15}, "step 1 snapshot is wrong"
assert trace[2]["variables"]["z"] == 20, "step 3: x+y  should be 20"
assert trace[5]["variables"]["z"] == 3, "step 5:x/y should be 3.0" # here 3 and 3.0 are same, if we want strict float use below assert

#stricter test also checks the container:
#assert isinstance(trace[5]["variables"]["z"], float)