def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reported_count = [0] * len(id_list)
    report = list(set(report))
    report_new = dict()
    
    for r in report:
        reporter, reported = r.split(' ')
        reported_count[id_list.index(reported)] += 1
        
        if reported in report_new:
            report_new[reported].append(reporter)
        else:
            report_new[reported] = list()
            report_new[reported].append(reporter)
    
    for i in range(len(reported_count)):
        if reported_count[i] >= k:
            reporters = report_new.get(id_list[i])
            for rr in reporters:
                answer[id_list.index(rr)] += 1
    
    return answer
        