import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_number_of_matches, run_number_of_matches
    from solution import Solution

    return Solution, assert_number_of_matches, run_number_of_matches


@app.cell
def _():
    # Example test case
    n = 7
    expected = 6
    return expected, n


@app.cell
def _(Solution, n, run_number_of_matches):
    result = run_number_of_matches(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_number_of_matches, expected, result):
    assert_number_of_matches(result, expected)
    return


if __name__ == "__main__":
    app.run()
