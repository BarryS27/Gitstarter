import requests

def search_issues(lang):
    url = "https://api.github.com/search/issues"
    default_q = f"is:issue language:{lang} label:\"good first issue\" state:open archived:false -linked:pr no:assignee"

    parameters = {
        "q": default_q,
        "sort": "updated",
        "order": "desc",
        "per_page": 10
    }

    try:
        response = requests.get(url, params=parameters)
        response.raise_for_status()

        data_list = response.json()["items"]
        results = []

        for item in data_list:
            issue_info = {
                "title": item["title"],
                "url": item["html_url"]
            }
            results.append(issue_info)

        return results

    except Exception as e:
        print(f"Error: {e}")
        return []

# --- Test ---
if __name__ == "__main__":
    issues = search_issues("python")
    print(f"找到 {len(issues)} 个 Issue:")
    for issue in issues:
        print(issue)
