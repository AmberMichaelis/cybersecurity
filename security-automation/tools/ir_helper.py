import sys
from datetime import datetime


def create_incident_summary(incident_type, affected_system, severity, notes):
    """
    Create a simple incident response summary.

    This tool helps organize basic information an analyst may collect
    during the early stage of an investigation.
    """

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = f"""
Incident Response Helper
----------------------------------------
Timestamp: {timestamp}
Incident Type: {incident_type}
Affected System: {affected_system}
Severity: {severity}

Initial Notes:
{notes}

Recommended First Steps:
1. Confirm the incident details.
2. Preserve relevant logs and evidence.
3. Identify affected users, systems, or accounts.
4. Contain the issue if there is an active threat.
5. Escalate to the appropriate security or IT team.
6. Document all actions taken.
"""

    return report


if __name__ == "__main__":
    # Expected usage:
    # python3 tools/ir_helper.py "<incident_type>" "<affected_system>" "<severity>" "<notes>"

    if len(sys.argv) < 5:
        print('Usage: python3 tools/ir_helper.py "<incident_type>" "<affected_system>" "<severity>" "<notes>"')
        sys.exit(1)

    incident_type = sys.argv[1]
    affected_system = sys.argv[2]
    severity = sys.argv[3]
    notes = sys.argv[4]

    summary = create_incident_summary(
        incident_type,
        affected_system,
        severity,
        notes
    )

    print(summary)
