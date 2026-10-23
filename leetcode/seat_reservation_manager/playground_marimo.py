import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_seat_reservation_manager, run_seat_reservation_manager
    from solution import SeatManager

    return (
        SeatManager,
        assert_seat_reservation_manager,
        run_seat_reservation_manager,
    )


@app.cell
def _():
    # Example test case
    operations = [
        "SeatManager",
        "reserve",
        "reserve",
        "unreserve",
        "reserve",
        "reserve",
        "reserve",
        "reserve",
        "unreserve",
    ]
    inputs = [[5], [], [], [2], [], [], [], [], [5]]
    expected = [None, 1, 2, None, 2, 3, 4, 5, None]
    return expected, inputs, operations


@app.cell
def _(SeatManager, inputs, operations, run_seat_reservation_manager):
    result, manager = run_seat_reservation_manager(SeatManager, operations, inputs)
    print(result)
    manager
    return (result,)


@app.cell
def _(assert_seat_reservation_manager, expected, result):
    assert_seat_reservation_manager(result, expected)
    return


if __name__ == "__main__":
    app.run()
