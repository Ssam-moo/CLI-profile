#!/usr/bin/env python3
"""Developer profile CLI."""

import argparse
from profile import summary, get_skills, get_projects

__version__ = "0.1.0"


def main(args=None):
    parser = argparse.ArgumentParser(description="Developer profile CLI")
    parser.add_argument("--version", action="version", version=__version__)

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    subparsers.add_parser("summary", help="Show developer summary")
    subparsers.add_parser("skills", help="List skills")
    subparsers.add_parser("projects", help="List projects")

    parsed = parser.parse_args(args)

    if parsed.command == "summary":
        print(summary())
    elif parsed.command == "skills":
        print("Skills:\n- " + "\n- ".join(get_skills()))
    elif parsed.command == "projects":
        for name, desc in get_projects().items():
            print(f"{name}: {desc}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
