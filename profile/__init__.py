"""Helper functions to access profile data."""

from . import data


def summary():
    """Return a formatted summary string of the developer profile."""
    lines = [
        f"Name: {data.NAME}",
        f"Role: {data.ROLE}",
        f"Experience: {data.YEARS_EXPERIENCE} years",
        "Skills: " + ", ".join(data.SKILLS),
    ]
    return "\n".join(lines)


def get_skills():
    return data.SKILLS


def get_projects():
    return data.PROJECTS
