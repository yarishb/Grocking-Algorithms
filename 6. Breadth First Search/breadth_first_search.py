from collections import deque

def person_is_seller(name):
     return name[-1] == 'm'

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def search(person):
     search_queue = deque()
     search_queue += graph["you"]
     
     searched = []
     
     while search_queue:
          person = search_queue.popleft()
          
          if person not in searched:
               if person_is_seller(person):
                    print(person + " is a mango seller")
                    return True
               else:
                    search_queue += graph[person]
                    searched.append(person)
     return False

search("you")