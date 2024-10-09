from googleapiclient import discovery

import json

API_KEY="AIzaSyBnysQ4Le2Du1i7nPN9S0mF537NRQAkzuQ"

client = discovery.build(
    "commentanalyzer",
    "v1alpha1",
    developerKey=API_KEY,
    discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest",
    static_discovery=False,
)

analyze_request = {
    'comment': {'text': 'I hate you!'},
    'requestedAttributes': {'TOXICITY': {}},
}

response = client.comments().analyze(body=analyze_request).execute()
print(json.dumps(response, indent=2))

