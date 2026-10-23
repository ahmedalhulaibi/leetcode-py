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
    n = 7
    blacklist = [2, 3, 5]
    seed = 0
    calls = 8
    return blacklist, calls, n, seed


@app.cell
def _(Solution, blacklist, calls, n, run_pick, seed):
    result = run_pick(Solution, n, blacklist, seed, calls)
    print(result)
    result
    return (result,)


@app.cell
def _(assert_pick, blacklist, calls, n, result):
    assert_pick(result, n, blacklist, calls)
    return


if __name__ == "__main__":
    app.run()
