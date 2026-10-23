import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_browser_history_operations, run_browser_history_operations
    from solution import BrowserHistory

    return (
        BrowserHistory,
        assert_browser_history_operations,
        run_browser_history_operations,
    )


@app.cell
def _():
    # Example test case
    operations = [
        "BrowserHistory",
        "visit",
        "visit",
        "visit",
        "back",
        "back",
        "forward",
        "visit",
        "forward",
        "back",
        "back",
    ]
    inputs = [
        ["leetcode.com"],
        ["google.com"],
        ["facebook.com"],
        ["youtube.com"],
        [1],
        [1],
        [1],
        ["linkedin.com"],
        [2],
        [2],
        [7],
    ]
    expected = [
        None,
        None,
        None,
        None,
        "facebook.com",
        "google.com",
        "facebook.com",
        None,
        "linkedin.com",
        "google.com",
        "leetcode.com",
    ]
    return expected, inputs, operations


@app.cell
def _(BrowserHistory, inputs, operations, run_browser_history_operations):
    result, history = run_browser_history_operations(BrowserHistory, operations, inputs)
    print(result)
    history
    return (result,)


@app.cell
def _(assert_browser_history_operations, expected, result):
    assert_browser_history_operations(result, expected)
    return


if __name__ == "__main__":
    app.run()
