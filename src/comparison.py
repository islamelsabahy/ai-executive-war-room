from .agents import run_agents
from .council import synthesize

def compare_options(crisis, profiles):
    views=run_agents(crisis,profiles)
    decision=synthesize(crisis,views)
    ranking=sorted(decision.option_scores.items(),key=lambda x:x[1],reverse=True)
    return {"scenario":crisis.name,"ranking":[{"option":k,"council_score":v} for k,v in ranking],"role_votes":decision.votes,"consensus_pct":decision.consensus_score,"dissent_pct":decision.dissent_score}
