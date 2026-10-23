import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_can_visit_all_rooms, run_can_visit_all_rooms
    from solution import Solution

    return Solution, assert_can_visit_all_rooms, run_can_visit_all_rooms


@app.cell
def _():
    # Example test case
    rooms = [[1], [2], [3], []]
    expected = True
    return expected, rooms


@app.cell
def _(Solution, rooms, run_can_visit_all_rooms):
    result = run_can_visit_all_rooms(Solution, rooms)
    result
    return (result,)


@app.cell
def _(assert_can_visit_all_rooms, expected, result):
    assert_can_visit_all_rooms(result, expected)
    return


if __name__ == "__main__":
    app.run()
