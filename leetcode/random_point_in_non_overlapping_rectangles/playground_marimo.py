import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_pick, run_pick
    from solution import Solution

    return Solution, assert_pick, run_pick


@app.cell
def _():
    # Example test case
    rects = [[-2, -2, 1, 1], [2, 2, 4, 6]]
    seed = 0
    n = 20
    return n, rects, seed


@app.cell
def _(Solution, n, rects, run_pick, seed):
    result = run_pick(Solution, rects, seed, n)
    print(result)
    result
    return (result,)


@app.cell
def _(assert_pick, n, rects, result):
    assert_pick(result, rects, n)
    return


if __name__ == "__main__":
    app.run()
