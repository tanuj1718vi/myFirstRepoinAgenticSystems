import requests
import pandas as pd


def get_clean_data():
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame(data)

    # Basic cleaning
    df = df.rename(columns={"userId": "user_id"})
    df = df.drop(columns=["id"])

    # Create new column
    df["post_length"] = df["body"].apply(len)

    return df


if __name__ == "__main__":
    df = get_clean_data()
    print(df.head())
    print("\nPosts per user:")
    print(df.groupby("user_id").size())