
from collections import deque

def isM(name):
    if name[-1] == "m":
        return True
    else:
        return False

def search():
    pic = {}

    pic["me"] = ["alice", "bob", "claire"]
    pic["alice"] = ["peggy"]
    pic["bob"] = ["anuj", "peggy"]
    pic["claire"] = ["thom", "jonny"]
    pic["anuj"] = []
    pic["peggy"] = []
    pic["hom"] = []
    pic["jonny"] = []

    queue = deque()

    queue += pic.get("me")
    searched = []
    while queue:
        item = queue.popleft()
        if item not in searched:
            if isM(item):
                return item+"是芒果商人"
            else:
                searched.append(item)
                queue += pic.get(item)

    return "没有芒果商人"


print(search())


