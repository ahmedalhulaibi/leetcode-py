import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_twitter, run_twitter
    from solution import Twitter

    return Twitter, assert_twitter, run_twitter


@app.cell
def _():
    # Example test case
    operations = [
        "Twitter",
        "postTweet",
        "getNewsFeed",
        "follow",
        "postTweet",
        "getNewsFeed",
        "unfollow",
        "getNewsFeed",
    ]
    inputs = [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
    expected = [None, None, [5], None, None, [6, 5], None, [5]]
    return expected, inputs, operations


@app.cell
def _(Twitter, inputs, operations, run_twitter):
    result = run_twitter(Twitter, operations, inputs)
    result
    return (result,)


@app.cell
def _(assert_twitter, expected, result):
    assert_twitter(result, expected)
    return


if __name__ == "__main__":
    app.run()
