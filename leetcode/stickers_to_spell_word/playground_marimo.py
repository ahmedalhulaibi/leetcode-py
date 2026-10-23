import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_stickers, run_min_stickers
    from solution import Solution

    return Solution, assert_min_stickers, run_min_stickers


@app.cell
def _():
    # Example test case
    stickers = ["with", "example", "science"]
    target = "thehat"
    expected = 3
    return expected, stickers, target


@app.cell
def _(Solution, run_min_stickers, stickers, target):
    result = run_min_stickers(Solution, stickers, target)
    result
    return (result,)


@app.cell
def _(assert_min_stickers, expected, result):
    assert_min_stickers(result, expected)
    return


if __name__ == "__main__":
    app.run()
