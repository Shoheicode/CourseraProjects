# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    queries = [input().split() for _ in range(n)]
    return queries
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    phone_book = {}
    results = []
    
    for query in queries:
        operation = query[0]
        number = query[1]
        
        if operation == "add":
            name = query[2]
            phone_book[number] = name
            
        elif operation == "del":
            if number in phone_book:
                del phone_book[number]
                
        elif operation == "find":
            results.append(phone_book.get(number, "not found"))
    
    return results

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
