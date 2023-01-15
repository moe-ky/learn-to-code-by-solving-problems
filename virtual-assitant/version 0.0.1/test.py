lst = [{"id":2}, {"id":1}, {'id':0}]

def return_id(item):
    return item['id']

print(sorted(lst, key=return_id))
