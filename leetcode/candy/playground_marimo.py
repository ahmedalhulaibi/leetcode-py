import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_candy, run_candy
    from solution import Solution

    return Solution, assert_candy, run_candy


@app.cell
def _():
    # Example test case
    ratings = [1, 0, 2]
    expected = 5
    return expected, ratings


@app.cell
def _(Solution, ratings, run_candy):
    result = run_candy(Solution, ratings)
    result
    return (result,)


@app.cell
def _(assert_candy, expected, result):
    assert_candy(result, expected)
    return


if __name__ == "__main__":
    app.run()
