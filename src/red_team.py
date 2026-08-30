def challenge(crisis, views, leading_option):
    challenges=[]; option=next(o for o in crisis.options if o["id"]==leading_option)
    if crisis.evidence_quality<.65: challenges.append("Decision may be overconfident relative to evidence quality.")
    if crisis.unknowns>.55: challenges.append("Material unknowns remain unresolved.")
    if option.get("irreversibility",0)>.65: challenges.append("Leading option creates material irreversible exposure.")
    if option.get("cost",0)>.75: challenges.append("Leading option has high cost relative to other responses.")
    if option.get("speed",0)<.45 and crisis.urgency>.7: challenges.append("Leading option may be too slow for crisis urgency.")
    votes={v.recommendation for v in views}
    if len(votes)==1: challenges.append("Full consensus may indicate insufficient alternative exploration.")
    if not challenges: challenges.append("No major structural challenge detected; validate execution assumptions.")
    return challenges
