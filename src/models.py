from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class Crisis:
    crisis_id:str; name:str; category:str; severity:float; evidence_quality:float; customer_impact:float; operational_impact:float; financial_impact:float; cyber_risk:float; technology_risk:float; urgency:float; unknowns:float; options:List[dict]; injects:List[dict]=field(default_factory=list)

@dataclass
class AgentView:
    role:str; option_scores:Dict[str,float]; recommendation:str; confidence:float; rationale:List[str]; objections:List[str]

@dataclass
class CouncilDecision:
    recommended_option:str; consensus_score:float; dissent_score:float; confidence:float; votes:Dict[str,str]; option_scores:Dict[str,float]; dissent_log:List[dict]; red_team_challenges:List[str]; executive_brief:Dict
