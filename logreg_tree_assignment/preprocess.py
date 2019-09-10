import json
import os

import pandas as pd

DATA_DIR = '../data/tickets'

if __name__ == '__main__':
    assignee = []
    summary = []
    description = []
    comment = []
    team = []
    num_failed = 0
    for filename in os.listdir(DATA_DIR):
        if not filename.endswith('json'):
            continue
        path = os.path.join(DATA_DIR, filename)
        with open(path) as f:
            try:
                ticket_data = json.load(f)
                ticket_assignee = ticket_data['fields']['assignee']['key']
                ticket_summary = ticket_data['fields']['summary']
                ticket_description = ticket_data['fields']['description']
                ticket_team = ticket_data['fields']['customfield_22690']['value']
                ticket_comments = ' '.join(map(lambda x: x['body'], ticket_data['fields']['comment']['comments']))
                assignee.append(ticket_assignee)
                summary.append(ticket_summary)
                description.append(ticket_description)
                comment.append(ticket_comments)
                team.append(ticket_team)
            except Exception:
                num_failed += 1

    print(str(num_failed) + ' is failed')
    ticket_dataframe = pd.DataFrame.from_dict(
        {'assignee': assignee, 'summary': summary, 'description': description, 'comments': comment, 'team': team})
    ticket_dataframe.to_csv(os.path.join(DATA_DIR, 'tickets.csv'))
