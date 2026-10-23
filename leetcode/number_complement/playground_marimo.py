import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_complement, run_find_complement
    from solution import Solution

    return Solution, assert_find_complement, run_find_complement


@app.cell
def _():
    # Example test case
    num = 5
    expected = 2
    return expected, num


@app.cell
def _(Solution, num, run_find_complement):
    result = run_find_complement(Solution, num)
    result
    return (result,)


@app.cell
def _(assert_find_complement, expected, result):
    assert_find_complement(result, expected)
    return


if __name__ == "__main__":
    app.run()
