import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_my_calendar, run_my_calendar
    from solution import MyCalendar

    return MyCalendar, assert_my_calendar, run_my_calendar


@app.cell
def _():
    # Example test case
    bookings = [(10, 20), (15, 25), (20, 30)]
    expected = [True, False, True]
    return bookings, expected


@app.cell
def _(MyCalendar, bookings, run_my_calendar):
    result = run_my_calendar(MyCalendar, bookings)
    result
    return (result,)


@app.cell
def _(assert_my_calendar, expected, result):
    assert_my_calendar(result, expected)
    return


if __name__ == "__main__":
    app.run()
