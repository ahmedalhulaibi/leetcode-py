import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_distinct_names, run_distinct_names
    from solution import Solution

    return Solution, assert_distinct_names, run_distinct_names


@app.cell
def _():
    # Example test case
    ideas: list[str] = ["coffee", "donuts", "time", "toffee"]
    expected = 6
    return expected, ideas


@app.cell
def _(Solution, ideas: list[str], run_distinct_names):
    result = run_distinct_names(Solution, ideas)
    result
    return (result,)


@app.cell
def _(assert_distinct_names, expected, result):
    assert_distinct_names(result, expected)
    return


if __name__ == "__main__":
    app.run()
