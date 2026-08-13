import ast          # "Bring me the toolkit that turns code-text into trees."
import json         # "Bring me the toolkit that prints data as readable JSON."

variables = {}      # "Set up an empty whiteboard." (labeled boxes → {})
trace = []          # "Set up an empty photo album." (numbered photos → [])


def eval_expr(node):                        # "Job A: given a tree-piece, what is it WORTH?"
    if isinstance(node, ast.Constant):      # "Is it a plain literal, like 4?"
        return node.value                   # "The number is written inside it — hand it back."
    elif isinstance(node, ast.Name):        # "No? Is it a variable name, like p?"
        return variables[node.id]           # "Glance at the whiteboard — hand back what's under that name."
    else:                                   # "Neither?"
        raise Exception(f"...")             # "Never learned this — shout and stop. Never guess quietly."

def run_statement(node, line_number):       # "Job B: given one line, actually DO it."
    if isinstance(node, ast.Assign):        # "Is this line an assignment?"
        var_name = node.targets[0].id       # "Who's being assigned to? First target's name."
        value = eval_expr(node.value)       # "What's the right side worth? Ask Job A."
        variables[var_name] = value         # "Write it on the whiteboard."

        trace.append({                      # "Stick a new photo in the album, showing:"
            "step": len(trace) + 1,         #   "photo number = photos so far, plus one"
            "line": line_number,            #   "which code line just ran"
            "event": "assign",              #   "what kind of thing happened"
            "changed": {var_name: value},   #   "the single marker stroke this line made"
            "variables": dict(variables),   #   "a FROZEN COPY of the whole whiteboard — photo, not mirror"
        })
    else:                                   # "A line shape I don't know?"
        raise Exception(f"...")             # "Shout and stop."


code = "p = 4\nq = p\nr = 7"               # "Here's the program, as text. \n = the Enter key."
tree = ast.parse(code)                      # "Turn the text into a tree."

for line_number, statement in enumerate(tree.body, start=1):
                                            # "For each statement in the tree, counted from 1..."
    run_statement(statement, line_number)   # "...act out that line."

print(json.dumps(trace, indent=2))          # "Print the album, nicely indented."






# #The whole journey in 5 beats
# Day 1–2: Backend (a program that waits and answers at /trace) + frontend (a page that fetches and shows). The trace was fake — typed by hand.
# Day 3: Python can turn code text into a tree (ast.parse): x = 5 becomes Assign(targets=[Name(id='x')], value=Constant(5)) — structure, not text.
# Day 4: Built a tool to look at any code's tree, any time. Trees are looked up, never memorized.
# Day 5 (today): The evaluator — the cook that follows the recipe: reads tree nodes and actually does them, keeping a whiteboard (variables, dict) and a photo album (trace, list), one photo (dict(variables) copy!) per line.
# Testing (today's overlay): decide expected first, run for actual, compare. The comparison caught a real bug; the assert now guards it forever.
# Worked example, every step: a = 10 then b = a
# Step 0 — parse. ast.parse("a = 10\nb = a") gives a tree whose body is a list of 2 statements:

# line 1: Assign(targets=[Name(id='a')], value=Constant(10))
# line 2: Assign(targets=[Name(id='b')], value=Name(id='a')) ← note: the right side is a Name this time, not a Constant!
# Loop, round 1 — run_statement gets line 1's Assign:

# What happens	Result
# Who's assigned to? targets[0].id	'a'
# Right side worth? eval_expr(Constant(10)) → first branch (it's a Constant)	10
# Write on whiteboard	whiteboard: {a: 10}
# Take photo (dict(variables) = frozen copy)	album: photo 1 = {a: 10}
# Loop, round 2 — run_statement gets line 2's Assign:

# What happens	Result
# Who's assigned to?	'b'
# Right side worth? eval_expr(Name(id='a')) → second branch (it's a Name) → glance at whiteboard: what's a?	10
# Write on whiteboard	whiteboard: {a: 10, b: 10}
# Take photo	album: photo 2 = {a: 10, b: 10}
# Final trace: 2 steps. Step 1 variables {a: 10}, step 2 variables {a: 10, b: 10} — and photo 1 still shows only a, because it's a copy, not a mirror.

# Notice this example used both branches of your eval_expr — line 1's right side was a Constant, line 2's was a Name.
# ###