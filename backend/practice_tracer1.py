import ast
import json

variables = {}
trace = []

def eval_expr(node):
    # print("eval_expr called with:", node)

    if isinstance(node,ast.Name):
        return variables[node.id]
    elif isinstance(node,ast.Constant):
        return node.value
    elif isinstance(node,ast.BinOp):
        left_val = eval_expr(node.left)
        right_val = eval_expr(node.right)

        if isinstance(node.op,ast.Add):
            return left_val + right_val
        elif isinstance(node.op,ast.Sub):
            return left_val - right_val
        elif isinstance(node.op,ast.Mult):
            return left_val * right_val
        elif isinstance(node.op,ast.Div):
            return left_val / right_val
        else:
            raise Exception(f"Wrong operation:{node.op}")
    else:
        raise Exception(f"what are you doing{node}")

def run_statement(node , line_number):
    if isinstance(node,ast.Assign):
        var_name = node.targets[0].id
        value = eval_expr(node.value)
        variables[var_name] = value

        trace.append(
            {
                "step":len(trace)+1,
                "line": line_number,
                "event":"assign",
                "changed":{var_name:value},
                "variables":dict(variables),
            }
        )
    else:
        raise Exception(f"Wrong:{node}")


code = "x=5\ny=3\nz=x+y\nz=x-y\nz=x*y\nz=x/y"
tree=ast.parse(code)


for line_number, statement in enumerate(tree.body, start=1):
    run_statement(statement, line_number)

print(json.dumps(trace, indent=2))

assert trace[2]["variables"]["z"] == 8, "step 3: x+y should be 8"
assert trace[5]["variables"]["z"] == 1.6666666666666667, "step 6: x/y wrong"
assert trace[0]["changed"] == {"x": 5}, "step 1 changed should show x"
