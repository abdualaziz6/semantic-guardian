from validator_rules import rule_check
from validator_llm import llm_check


def orchestrate_validation(data):

    rule_result = rule_check(data)

    if rule_result:
        return {
            "status": "warning",
            "confidence_score": 0.95,
            "message": rule_result,
            "suggestion": "Please review the highlighted response.",
            "source": "rules"
        }

    return llm_check(data)