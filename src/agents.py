from .models import AgentView

DIMENSIONS = ["customer_impact","operational_impact","financial_impact","cyber_risk","technology_risk","urgency"]

def _option_score(crisis, option, profile):
    benefit = option.get("benefit", {})
    risk = option.get("risk", {})
    score = 0.0

    for dim, weight in profile["weights"].items():
        crisis_pressure = float(getattr(crisis, dim))
        reduction = float(benefit.get(dim, 0))
        added_risk = float(risk.get(dim, 0))
        score += weight * (crisis_pressure * reduction - added_risk)

    score += .10 * float(option.get("reversibility", .5))
    score += .08 * float(option.get("speed", .5))
    score -= .08 * float(option.get("cost", .5))
    score -= .06 * max(0, float(option.get("irreversibility",0)) - profile["risk_appetite"])
    return round(score,4)

def analyze(role, crisis, profile):
    scores={o["id"]:_option_score(crisis,o,profile) for o in crisis.options}
    recommendation=max(scores,key=scores.get)
    evidence_factor=.55+.45*crisis.evidence_quality
    uncertainty_penalty=.35*crisis.unknowns
    spread=max(scores.values())-min(scores.values()) if len(scores)>1 else .2
    confidence=max(.05,min(.98,evidence_factor+.20*spread-uncertainty_penalty))
    rationale=[f"{role} prioritized {', '.join(profile['priorities'][:2])}.",f"Highest-scoring option: {recommendation}.",f"Evidence quality: {crisis.evidence_quality:.2f}; unknowns: {crisis.unknowns:.2f}."]
    objections=[]
    selected=next(o for o in crisis.options if o["id"]==recommendation)
    if selected.get("irreversibility",0)>.7: objections.append("Preferred option has high irreversibility.")
    if selected.get("cost",0)>.75 and role=="CFO": objections.append("Preferred option carries high cost.")
    if crisis.cyber_risk>.7 and role=="CISO" and selected.get("benefit",{}).get("cyber_risk",0)<.45: objections.append("Cyber containment benefit may be insufficient.")
    if crisis.customer_impact>.7 and role=="Product" and selected.get("benefit",{}).get("customer_impact",0)<.45: objections.append("Customer-impact reduction may be insufficient.")
    return AgentView(role=role,option_scores=scores,recommendation=recommendation,confidence=round(confidence,2),rationale=rationale,objections=objections)

def run_agents(crisis, profiles):
    return [analyze(role,crisis,profile) for role,profile in profiles.items()]
