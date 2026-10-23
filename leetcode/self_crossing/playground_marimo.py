import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_self_crossing, run_is_self_crossing
    from solution import Solution

    return Solution, assert_is_self_crossing, run_is_self_crossing


@app.cell
def _():
    # Example test case
    distance = [2, 1, 1, 2]
    expected = True
    return distance, expected


@app.cell
def _(Solution, distance, run_is_self_crossing):
    result = run_is_self_crossing(Solution, distance)
    result
    return (result,)


@app.cell
def _(assert_is_self_crossing, expected, result):
    assert_is_self_crossing(result, expected)
    return


if __name__ == "__main__":
    app.run()
