import argparse
from rich import print as rich_print
from .core import fetch_github_events, format_event

def main():
    parser = argparse.ArgumentParser(description="Fetch and display recent GitHub events for a user.")
    parser.add_argument(
    "username",
    type=str,
    help="GitHub username to fetch events for."
    )

    args = parser.parse_args()
    try: 
        events = fetch_github_events(args.username)
    except Exception as e:
        rich_print(f"[red]Error:[/red] {e}")
        return
    
    if not events:
        return
    
    rich_print(f"[green]Recent events for [blue]{args.username}[/blue]:[/green]")
    for event in events:
        formatted = format_event(event)
        rich_print(f"- {formatted}")