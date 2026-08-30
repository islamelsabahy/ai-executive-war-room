from dataclasses import asdict

def decision_payload(decision, views=None):
    payload=asdict(decision)
    if views is not None: payload["agent_views"]=[asdict(v) for v in views]
    payload["safety_note"]="Synthetic executive simulation only. No real decision is executed."
    return payload
