import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_get_max_repetitions, run_get_max_repetitions
    from solution import Solution

    return Solution, assert_get_max_repetitions, run_get_max_repetitions


@app.cell
def _():
    # Example test case
    s1 = "acb"
    n1 = 4
    s2 = "ab"
    n2 = 2
    expected = 2
    return expected, n1, n2, s1, s2


@app.cell
def _(Solution, n1, n2, run_get_max_repetitions, s1, s2):
    result = run_get_max_repetitions(Solution, s1, n1, s2, n2)
    result
    return (result,)


@app.cell
def _(assert_get_max_repetitions, expected, result):
    assert_get_max_repetitions(result, expected)
    return


if __name__ == "__main__":
    app.run()
