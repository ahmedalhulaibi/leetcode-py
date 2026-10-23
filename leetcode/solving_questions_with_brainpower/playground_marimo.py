import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_most_points, run_most_points
    from solution import Solution

    return Solution, assert_most_points, run_most_points


@app.cell
def _():
    # Example test case
    questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
    expected = 5
    return expected, questions


@app.cell
def _(Solution, questions, run_most_points):
    result = run_most_points(Solution, questions)
    result
    return (result,)


@app.cell
def _(assert_most_points, expected, result):
    assert_most_points(result, expected)
    return


if __name__ == "__main__":
    app.run()
