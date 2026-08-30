from copy import deepcopy
from .agents import run_agents
from .council import synthesize

def apply_inject(crisis, inject):
    c=deepcopy(crisis)
    for field,delta in inject.get("deltas",{}).items():
        if hasattr(c,field):
            value=float(getattr(c,field))+float(delta)
            setattr(c,field,max(0.0,min(1.0,value)))
    return c

def run_exercise(crisis, profiles):
    stages=[]; current=crisis
    views=run_agents(current,profiles); stages.append({"stage":"initial","decision":synthesize(current,views)})
    for idx,inject in enumerate(crisis.injects,1):
        current=apply_inject(current,inject); views=run_agents(current,profiles)
        stages.append({"stage":f"inject-{idx}","inject":inject.get("name",f"Inject {idx}"),"decision":synthesize(current,views)})
    return stages
