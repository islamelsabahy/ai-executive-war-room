def detect_conflicts(views):
    groups={}
    for v in views: groups.setdefault(v.recommendation,[]).append(v.role)
    conflicts=[]
    if len(groups)>1:
        for option,roles in groups.items(): conflicts.append({"option":option,"supporters":roles,"count":len(roles)})
    return conflicts

def dissent_score(views):
    if not views: return 0.0
    counts={}
    for v in views: counts[v.recommendation]=counts.get(v.recommendation,0)+1
    dominant=max(counts.values())
    return round(100*(1-dominant/len(views)),1)
