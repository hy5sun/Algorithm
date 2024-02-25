def solution(data, ext, val_ext, sort_by):
    answer = []
    name = ['code', 'date', 'maximum', 'remain']
    for d in data:
        idx = name.index(ext)
        if d[idx] < val_ext:
            answer.append(d)
            
    answer.sort(key=lambda x: x[name.index(sort_by)])
    return answer