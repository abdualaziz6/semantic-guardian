def rule_check(data):

    if data.get("age", 0) < 18 and data.get("employment_type") == "Full-time":
        return "Age inconsistent with employment type"

    if data.get("education") == "PhD" and data.get("age", 0) < 22:
        return "Education level unlikely for age"

    return None