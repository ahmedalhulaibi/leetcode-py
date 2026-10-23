import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_friend_requests, run_num_friend_requests
    from solution import Solution

    return Solution, assert_num_friend_requests, run_num_friend_requests


@app.cell
def _():
    # Example test case
    ages = [16, 16]
    expected = 2
    return ages, expected


@app.cell
def _(Solution, ages, run_num_friend_requests):
    result = run_num_friend_requests(Solution, ages)
    result
    return (result,)


@app.cell
def _(assert_num_friend_requests, expected, result):
    assert_num_friend_requests(result, expected)
    return


if __name__ == "__main__":
    app.run()
