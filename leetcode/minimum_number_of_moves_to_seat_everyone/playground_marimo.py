import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_moves_to_seat, run_min_moves_to_seat
    from solution import Solution

    return Solution, assert_min_moves_to_seat, run_min_moves_to_seat


@app.cell
def _():
    # Example test case
    seats = [3, 1, 5]
    students = [2, 7, 4]
    expected = 4
    return expected, seats, students


@app.cell
def _(Solution, run_min_moves_to_seat, seats, students):
    result = run_min_moves_to_seat(Solution, seats, students)
    result
    return (result,)


@app.cell
def _(assert_min_moves_to_seat, expected, result):
    assert_min_moves_to_seat(result, expected)
    return


if __name__ == "__main__":
    app.run()
