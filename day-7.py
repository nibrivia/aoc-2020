from utils import *
import parse

rules = read_day(7)

graph = dict()

for r in rules:
    color, cont = r.split(" bags contain ")
    if cont == "no other bags.":
        graph[color] = []
        continue
    for b in cont.replace(".", "").split(","):
        n, bag = parse.parse("{:d} {} bag", b.replace("bags", "bag"))
        cur = graph.get(color, [])
        cur.append((n, bag))
        graph[color] = cur



rev_graph = dict()
for big, conts in graph.items():
    if big not in rev_graph:
        rev_graph[big] = []
    for _, small in conts:
        cur = rev_graph.get(small, [])
        cur.append(big)
        rev_graph[small] = cur

def cont_colors(col):
    cols = set(rev_graph[col])

    new_cols = set()
    for c in cols:
        new_cols.update(cont_colors(c))

    cols.update(new_cols)

    return cols
print(len(cont_colors("shiny gold")))

def bags_cont(top_col):
    cont = graph[top_col]
    top_n = 0
    for n, col in cont:
        top_n += n+n*bags_cont(col)
    return top_n


print(bags_cont("shiny gold"))


print("done")
