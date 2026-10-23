import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_open_lock, run_open_lock
    from solution import Solution

    return Solution, assert_open_lock, run_open_lock


@app.cell
def _():
    # Example test case
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"
    expected = 6
    return deadends, expected, target


@app.cell
def _(Solution, deadends, run_open_lock, target):
    result = run_open_lock(Solution, deadends, target)
    result
    return (result,)


@app.cell
def _(assert_open_lock, expected, result):
    assert_open_lock(result, expected)
    return


if __name__ == "__main__":
    app.run()
