from collections import defaultdict
def group_by_owners(d):
    op={}
    for k,v in d.items():
        op[v]=op.get(v,[])
        op[v].append(k)

    return op



dictionary = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
print group_by_owners(dictionary)