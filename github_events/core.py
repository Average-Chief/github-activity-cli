import requests 
from rich import print as rich_print

def fetch_github_events(username: str):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching data from Github API: {response.status_code}")
    
    data = response.json()
    if not data:
        rich_print(f"No events found for the [blue]{username}[/blue].[/yellow]")
        return []
    return data


def format_event(event: dict) -> str:
    event_type = event.get("type")
    repo_name = event.get("repo",{}).get("name", "N/A")
    payload = event.get("payload", {})

    #for push events
    if event_type == "PushEvent":
        commits = payload.get("commits", [])
        return f"Pushed to {len(commits)} commit(s) to {repo_name}."
    
    #for star/watch events
    elif event_type == "WatchEvent":
        action = payload.get("action","starred")
        return f"{action.capitalize()} WatchEvent on {repo_name}."
    
    #for issues
    elif event_type == "IssuesEvent":
        action = payload.get("action","did something with")
        issue = payload.get("issue",{})
        number = issue.get("number","N/A")
        return f"{action.capitalize()} issue #{number} in {repo_name}"
    
    #for pull requests
    elif event_type == "PullRequestEvent":
        action = payload.get("action", "did something with")
        pr = payload.get("pull_request", {})
        num = pr.get("number", "?")
        return f"{action.capitalize()} pull request #{num} in {repo_name}"
    
    #for fork events
    elif event_type == "ForkEvent":
        forkee = payload.get("forkee", {})
        target = forkee.get("full_name", "another repo")
        return f"Forked {repo_name} to {target}"
    
    #fallback for other event types
    return (f"{event_type} on {repo_name}.")
