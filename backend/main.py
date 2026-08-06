# from the fastapi toolbox we installed, bring in the FastAPI tool. without this python has no idea  what FastAPI means — installing a package makes it available, importing makes it usable in this file.

from fastapi import FastAPI

# middleware is the code that sits in the middle - it inspects/modifies every request coming in and every response going out, before endpoint code ever sees it.
# Analogy: the receptionist at an office — every visitor passes them first, regardless of which room they're visiting.

from fastapi.middleware.cors import CORSMiddleware


# this creates your backend program. Right now app is an empty backend - it answers nothing has no doors. everything we add will gets attached to this app object. 
# The * is a wildcard meaning "anything." This is the actual CORS permission: tomorrow, when the React app on port 5173 calls us on port 8000, this is what stops the browser from silently blocking it. (["*"] is fine on your own machine; a production app would list only its real frontend address here — we'll tighten it when we deploy around Day 16–20.) 

# allow_methods=["*"] / allow_headers=["*"] — allow any request type (GET, POST...) and any extra metadata. Same wildcard idea.

app = FastAPI()

# app.add_middleware(...) — attach this receptionist to our app
# allowed_origins - accept requests from any address , 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# @ is decorator - it attaches a label to the function directly below it. this line say when someone send GET request to /trace, run this function
# GET request type means "just give me the data"(its what browser does when you visit a url)
# def get_trace(): plain python function. get_trace() is the function name.
# return - python list [...] - 3 items of dictionaries ({..}, labeled data). Each dictionary is one fake trace step
# step : step number line : which code line ran event : what kind of thing happened, changed : what this step changed, variables: everything in memory after the step
# FastAPI convert this to JSON automatically. 

@app.get("/trace")
def get_trace():
    return [
        {"step":1,"line":1,"event":"assign","changed":{"x":5},"variables":{"x":5}},
        {"step":2,"line":2,"event":"assign","changed":{"y":8},"variables":{"x":5,"y":8}},
        {"step":3,"line":3,"event":"print","changed":{},"variables":{"x":5,"y":8}},
    ]