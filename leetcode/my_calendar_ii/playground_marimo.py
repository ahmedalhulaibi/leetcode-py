import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_calendar_ops, run_calendar_ops
    from solution import MyCalendarTwo

    return MyCalendarTwo, assert_calendar_ops, run_calendar_ops


@app.cell
def _():
    # Example test case
    operations = ["MyCalendarTwo", "book", "book", "book"]
    inputs = [[], [10, 20], [50, 60], [10, 40]]
    expected = [None, True, True, True]
    return expected, inputs, operations


@app.cell
def _(MyCalendarTwo, inputs, operations, run_calendar_ops):
    result, calendar = run_calendar_ops(MyCalendarTwo, operations, inputs)
    print(result)
    calendar
    return (result,)


@app.cell
def _(assert_calendar_ops, expected, result):
    assert_calendar_ops(result, expected)
    return


if __name__ == "__main__":
    app.run()
