import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimum_semesters, run_minimum_semesters
    from solution import Solution

    return Solution, assert_minimum_semesters, run_minimum_semesters


@app.cell
def _():
    # Example test case
    n = 3
    relations = [[1, 3], [2, 3]]
    expected = 2
    return expected, n, relations


@app.cell
def _(Solution, n, relations, run_minimum_semesters):
    result = run_minimum_semesters(Solution, n, relations)
    result
    return (result,)


@app.cell
def _(assert_minimum_semesters, expected, result):
    assert_minimum_semesters(result, expected)
    return


if __name__ == "__main__":
    app.run()
