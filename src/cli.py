import json, sys
from dataclasses import asdict
from .loader import load_crises, load_profiles
from .agents import run_agents
from .council import synthesize
from .reporting import decision_payload
from .comparison import compare_options
from .exercise import run_exercise

def serialize_stage(stage):
    out=dict(stage); out["decision"]=asdict(stage["decision"]); return out

def main():
    args=sys.argv[1:] or ["run","platform-outage"]
    crises=load_crises(); profiles=load_profiles()
    command=args[0]; crisis_id=args[1] if len(args)>1 else "platform-outage"
    if crisis_id not in crises: raise SystemExit(f"Unknown crisis: {crisis_id}")
    crisis=crises[crisis_id]
    if command=="run":
        views=run_agents(crisis,profiles); decision=synthesize(crisis,views)
        print(json.dumps(decision_payload(decision,views),indent=2)); return
    if command=="compare":
        print(json.dumps(compare_options(crisis,profiles),indent=2)); return
    if command=="exercise":
        stages=run_exercise(crisis,profiles)
        print(json.dumps({"crisis":crisis.name,"stages":[serialize_stage(s) for s in stages]},indent=2)); return
    raise SystemExit("Commands: run <crisis> | compare <crisis> | exercise <crisis>")

if __name__=="__main__": main()
