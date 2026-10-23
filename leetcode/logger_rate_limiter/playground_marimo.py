import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_logger_rate_limiter, run_logger_rate_limiter
    from solution import Logger

    return Logger, assert_logger_rate_limiter, run_logger_rate_limiter


@app.cell
def _():
    # Example test case
    operations = ["Logger", "should_print_message", "should_print_message"]
    inputs = [[], [1, "foo"], [2, "bar"]]
    expected = [None, True, True]
    return expected, inputs, operations


@app.cell
def _(Logger, inputs, operations, run_logger_rate_limiter):
    result, logger = run_logger_rate_limiter(Logger, operations, inputs)
    print(result)
    logger
    return (result,)


@app.cell
def _(assert_logger_rate_limiter, expected, result):
    assert_logger_rate_limiter(result, expected)
    return


if __name__ == "__main__":
    app.run()
