import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_log_storage, run_log_storage
    from solution import LogSystem

    return LogSystem, assert_log_storage, run_log_storage


@app.cell
def _():
    # Example test case
    operations = ["LogSystem", "put", "retrieve"]
    inputs = [[], [1, "2017:01:01:23:59:59"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"]]
    expected = [None, None, [1]]
    return expected, inputs, operations


@app.cell
def _(LogSystem, inputs, operations, run_log_storage):
    result, log_system = run_log_storage(LogSystem, operations, inputs)
    print(result)
    log_system
    return (result,)


@app.cell
def _(assert_log_storage, expected, result):
    assert_log_storage(result, expected)
    return


if __name__ == "__main__":
    app.run()
