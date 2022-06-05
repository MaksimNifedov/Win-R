import requests
import json


def countProblems(userHandler: str) -> int:
    response = requests.get('https://codeforces.com/api/user.status?handle=' + userHandler)
    text = json.loads(response.text)
    text = text['result']
    problems = []

    for a in text:
        problems.append(str({a['contestId']: a['problem']['index']}))
    return len(set(problems))


users = input().split()
for user in users:
    print(f'{user} {countProblems(user)}')
