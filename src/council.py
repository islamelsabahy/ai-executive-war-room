from .models import CouncilDecision
from .conflict import dissent_score
from .red_team import challenge

def synthesize(crisis, views):
    aggregate={o["id"]:0.0 for o in crisis.options}; weights_total=0.0
    for view in views:
        weight=.6+.4*view.confidence; weights_total+=weight
        for option,score in view.option_scores.items(): aggregate[option]+=weight*score
    if weights_total: aggregate={k:round(v/weights_total,4) for k,v in aggregate.items()}
    leading=max(aggregate,key=aggregate.get)
    votes={v.role:v.recommendation for v in views}
    vote_support=sum(1 for x in votes.values() if x==leading)
    consensus=round(100*vote_support/max(1,len(votes)),1)
    dissent=dissent_score(views)
    red=challenge(crisis,views,leading)
    mean_conf=sum(v.confidence for v in views)/max(1,len(views))
    confidence=max(.05,min(.98,.45*mean_conf+.25*crisis.evidence_quality+.20*(consensus/100)+.10*(1-crisis.unknowns)))
    dissent_log=[]
    for v in views:
        if v.recommendation!=leading or v.objections:
            dissent_log.append({"role":v.role,"preferred_option":v.recommendation,"objections":v.objections or [f"Preferred {v.recommendation} over {leading}."]})
    brief={"crisis":crisis.name,"recommended_option":leading,"consensus_pct":consensus,"decision_confidence_pct":round(confidence*100,1),"top_tradeoff":"Balance immediate impact reduction against reversibility, cost, and residual risk.","executive_review_required":crisis.severity>=.7 or dissent>=40 or confidence<.65,"next_actions":["Confirm decision owner.","Validate evidence gaps before irreversible action.","Define success and rollback criteria.","Set next executive review checkpoint."]}
    return CouncilDecision(recommended_option=leading,consensus_score=consensus,dissent_score=dissent,confidence=round(confidence,2),votes=votes,option_scores=aggregate,dissent_log=dissent_log,red_team_challenges=red,executive_brief=brief)
