import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_path_crossing, run_is_path_crossing
    from solution import Solution

    return Solution, assert_is_path_crossing, run_is_path_crossing


@app.cell
def _():
    # Example test case
    path = "NESWW"
    expected = True
    return expected, path


@app.cell
def _(Solution, path, run_is_path_crossing):
    result = run_is_path_crossing(Solution, path)
    result
    return (result,)


@app.cell
def _(assert_is_path_crossing, expected, result):
    assert_is_path_crossing(result, expected)
    return


if __name__ == "__main__":
    app.run()
