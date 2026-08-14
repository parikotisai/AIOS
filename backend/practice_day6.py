import ast
import json

variables = {}
trace = []

def eval_expr(node):
    if isinstance(node,ast.Name):
        return variables[node.id]
    elif isinstance(node,ast.Constant):
        return node.value
    elif isinstance(node,ast.BinOp):
        left_value = eval_expr(node.left)
        right_value = eval_expr(node.right)

        if isinstance(node.op,ast.Add):
            return left_value + right_value
        elif isinstance(node.op,ast.Pow):
            return left_value ** right_value
        else:
            raise Exception(f"Not valid operation:{node.op}")
    else:
        raise Exception(f"What ar you doing:{node}")

def run_statement(node , line_number):
    if isinstance(node,ast.Assign):
        # variable name
        var_name = node.targets[0].id
        # value
        val= eval_expr(node.value)
        variables[var_name]=val

        trace.append({
                "step":len(trace)+ 1 ,# since trace starts with 0
                "line": line_number,
                "event":"assign",
                "changed":{var_name:val},
                "variables":dict(variables),
        })
    else:
        raise Exception(f"dont know how to run it{node}")

# declare and define variables
code = 'x = 8\ny = 4\nz = x+y\nz=x**y'
tree = ast.parse(code)

for line_number, statement in enumerate(tree.body,start=1):
    run_statement(statement,line_number)
print(json.dumps(trace, indent=2))

assert trace[0]["variables"]=={"x":8},"step 1 is wrong"

# make the two sides of == the same shape — value vs value, or dict vs dict, never value vs dict.
# assert trace[1]["variables"]["y"] == {"y":4},"y should be present" -> fails

assert trace[1]["variables"]["y"] == 4,"y should be present"
assert trace[2]["variables"]["z"] == 12, "step 3: x+y  should be 12"
assert trace[3]["variables"]["z"] == 4096, "step 4: x**y  should be power"

assert trace[0]["changed"] == {"x": 8}, "step 1 changed should name x"
