import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_read, run_read
    from solution import Solution

    return Solution, assert_read, run_read


@app.cell
def _():
    # Example test case
    file = "abc"
    queries = [1, 2, 1]
    expected = [1, 2, 0]
    return expected, file, queries


@app.cell
def _(Solution, file, queries, run_read):
    result = run_read(Solution, file, queries)
    result
    return (result,)


@app.cell
def _(assert_read, expected, result):
    assert_read(result, expected)
    return


if __name__ == "__main__":
    app.run()
