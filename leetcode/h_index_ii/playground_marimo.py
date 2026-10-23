import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_h_index, run_h_index
    from solution import Solution

    return Solution, assert_h_index, run_h_index


@app.cell
def _():
    # Example test case
    citations = [0, 1, 3, 5, 6]
    expected = 3
    return citations, expected


@app.cell
def _(Solution, citations, run_h_index):
    result = run_h_index(Solution, citations)
    result
    return (result,)


@app.cell
def _(assert_h_index, expected, result):
    assert_h_index(result, expected)
    return


if __name__ == "__main__":
    app.run()
