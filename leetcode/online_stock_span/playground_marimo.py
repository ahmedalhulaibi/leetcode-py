import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_online_stock_span_operations, run_online_stock_span_operations
    from solution import StockSpanner

    return (
        StockSpanner,
        assert_online_stock_span_operations,
        run_online_stock_span_operations,
    )


@app.cell
def _():
    # Example test case
    operations = ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
    inputs = [[], [100], [80], [60], [70], [60], [75], [85]]
    expected = [None, 1, 1, 1, 2, 1, 4, 6]
    return expected, inputs, operations


@app.cell
def _(StockSpanner, inputs, operations, run_online_stock_span_operations):
    result = run_online_stock_span_operations(StockSpanner, operations, inputs)
    result
    return (result,)


@app.cell
def _(assert_online_stock_span_operations, expected, result):
    assert_online_stock_span_operations(result, expected)
    return


if __name__ == "__main__":
    app.run()
