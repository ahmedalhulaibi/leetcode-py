import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_clean_room, run_clean_room
    from solution import Solution

    return Solution, assert_clean_room, run_clean_room


@app.cell
def _():
    # Example test case
    room = [[1, 1], [1, 0]]
    row = 0
    col = 0
    expected = 3
    return col, expected, room, row


@app.cell
def _(Solution, col, room, row, run_clean_room):
    result = run_clean_room(Solution, room, row, col)
    result
    return (result,)


@app.cell
def _(assert_clean_room, expected, result):
    assert_clean_room(result, expected)
    return


if __name__ == "__main__":
    app.run()
