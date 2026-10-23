import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_ambiguous_coordinates, run_ambiguous_coordinates
    from solution import Solution

    return Solution, assert_ambiguous_coordinates, run_ambiguous_coordinates


@app.cell
def _():
    # Example test case
    s = "(123)"
    expected = ["(1, 2.3)", "(1, 23)", "(1.2, 3)", "(12, 3)"]
    return expected, s


@app.cell
def _(Solution, run_ambiguous_coordinates, s):
    result = run_ambiguous_coordinates(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_ambiguous_coordinates, expected, result):
    assert_ambiguous_coordinates(result, expected)
    return


if __name__ == "__main__":
    app.run()
