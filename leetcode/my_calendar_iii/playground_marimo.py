import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_calendar_ops, run_calendar_ops
    from solution import MyCalendarThree

    return MyCalendarThree, assert_calendar_ops, run_calendar_ops


@app.cell
def _():
    # Example test case
    operations = ["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
    inputs = [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
    expected = [None, 1, 1, 2, 3, 3, 3]
    return expected, inputs, operations


@app.cell
def _(MyCalendarThree, inputs, operations, run_calendar_ops):
    result, calendar = run_calendar_ops(MyCalendarThree, operations, inputs)
    print(result)
    calendar
    return (result,)


@app.cell
def _(assert_calendar_ops, expected, result):
    assert_calendar_ops(result, expected)
    return


if __name__ == "__main__":
    app.run()
