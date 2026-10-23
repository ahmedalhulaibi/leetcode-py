import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_loud_and_rich, run_loud_and_rich
    from solution import Solution

    return Solution, assert_loud_and_rich, run_loud_and_rich


@app.cell
def _():
    # Example test case
    richer = [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]]
    quiet = [3, 2, 5, 4, 6, 1, 7, 0]
    expected = [5, 5, 2, 5, 4, 5, 6, 7]
    return expected, quiet, richer


@app.cell
def _(Solution, quiet, richer, run_loud_and_rich):
    result = run_loud_and_rich(Solution, richer, quiet)
    result
    return (result,)


@app.cell
def _(assert_loud_and_rich, expected, result):
    assert_loud_and_rich(result, expected)
    return


if __name__ == "__main__":
    app.run()
