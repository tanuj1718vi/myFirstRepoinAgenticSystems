# API GitHub Search - Answers

## 1. What is the role of query parameters in this request?

Query parameters are used to send additional information to the API.
They help customize the request.

In this example:
- q=python → searches repositories related to python
- sort=stars → sorts results by number of stars
- order=desc → shows highest stars first
- per_page=5 → limits results to 5 repositories

So, query parameters control what data we get from the API.

---

## 2. Why do we use response.json() instead of response.text?

response.json() is used to convert the API response into a Python dictionary.

- It makes data easy to access using keys (like repo["name"])
- response.text gives raw text (string), which is harder to work with

So, response.json() is more useful for handling API data in Python.