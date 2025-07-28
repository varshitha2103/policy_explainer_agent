import requests

url = "http://localhost:8000/explain_policy"
payload = {"query": "What is the Affordable Care Act?"}
response = requests.post(url, json=payload)

print("=== Simplified Explanation ===")
print(response.json()["simplified"])
print("\n=== Examples ===")
print(response.json()["examples"])
