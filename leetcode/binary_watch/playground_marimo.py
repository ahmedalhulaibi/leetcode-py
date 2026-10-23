import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_read_binary_watch, run_read_binary_watch
    from solution import Solution

    return Solution, assert_read_binary_watch, run_read_binary_watch


@app.cell
def _():
    # Example test case
    turned_on = 1
    expected = ["0:01", "0:02", "0:04", "0:08", "0:16", "0:32", "1:00", "2:00", "4:00", "8:00"]
    return expected, turned_on


@app.cell
def _(Solution, run_read_binary_watch, turned_on):
    result = run_read_binary_watch(Solution, turned_on)
    result
    return (result,)


@app.cell
def _(assert_read_binary_watch, expected, result):
    assert_read_binary_watch(result, expected)
    return


if __name__ == "__main__":
    app.run()
