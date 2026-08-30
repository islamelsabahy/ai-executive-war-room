import json
from pathlib import Path
from .models import Crisis

ROOT=Path(__file__).resolve().parents[1]

def load_profiles(): return json.loads((ROOT/"config"/"agent-profiles.json").read_text(encoding="utf-8"))

def load_crises():
    raw=json.loads((ROOT/"sample-data"/"crises.json").read_text(encoding="utf-8")); out={}
    for x in raw:
        out[x["crisis_id"]]=Crisis(crisis_id=x["crisis_id"],name=x["name"],category=x["category"],severity=float(x["severity"]),evidence_quality=float(x["evidence_quality"]),customer_impact=float(x["customer_impact"]),operational_impact=float(x["operational_impact"]),financial_impact=float(x["financial_impact"]),cyber_risk=float(x["cyber_risk"]),technology_risk=float(x["technology_risk"]),urgency=float(x["urgency"]),unknowns=float(x["unknowns"]),options=x["options"],injects=x.get("injects",[]))
    return out
