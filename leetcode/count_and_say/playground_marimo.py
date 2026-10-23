import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_and_say, run_count_and_say
    from solution import Solution

    return Solution, assert_count_and_say, run_count_and_say


@app.cell
def _():
    # Example test case
    n = 4
    expected = "1211"
    return expected, n


@app.cell
def _(Solution, n, run_count_and_say):
    result = run_count_and_say(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_count_and_say, expected, result):
    assert_count_and_say(result, expected)
    return


if __name__ == "__main__":
    app.run()
