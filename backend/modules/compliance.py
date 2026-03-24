def check_compliance(desc):
    issues=[]
    if "failed login" in desc.lower():
        issues.append("NIST: Auth Failure")
    return issues