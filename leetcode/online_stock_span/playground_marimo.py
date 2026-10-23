# /// script
# requires-python = ">=3.10"
# dependencies = ["marimo==0.25.2", "leetcode-py-sdk[practice]==0.0.0"]
# [tool.uv.sources]
# leetcode-py-sdk = { path = "../..", editable = true }
# ///

import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell(hide_code=True)
def _():
    import marimo as mo
    from leetcode_py.practice import run_practice_tests

    return mo, run_practice_tests


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # 901. Online Stock Span

    **Medium** · Stack, Design, Monotonic Stack, Data Stream

    Design an algorithm that collects daily price quotes for some stock and returns **the span** of that stock's price for the current day.

    The **span** of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

    - For example, if the prices of the stock in the last four days is `[7,2,1,2]` and the price of the stock today is `2`, then the span of today is `4` because starting from today, the price of the stock was less than or equal `2` for `4` consecutive days.
    - Also, if the prices of the stock in the last four days is `[7,34,1,2]` and the price of the stock today is `8`, then the span of today is `3` because starting from today, the price of the stock was less than or equal `8` for `3` consecutive days.

    Implement the `StockSpanner` class:

    - `StockSpanner()` Initializes the object of the class.
    - `int next(int price)` Returns the **span** of the stock's price given that today's price is `price`.

    ## Examples

    ```
    Input
    ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
    [[], [100], [80], [60], [70], [60], [75], [85]]
    Output
    [null, 1, 1, 1, 2, 1, 4, 6]

    Explanation
    StockSpanner stockSpanner = new StockSpanner();
    stockSpanner.next(100); // return 1
    stockSpanner.next(80);  // return 1
    stockSpanner.next(60);  // return 1
    stockSpanner.next(70);  // return 2
    stockSpanner.next(60);  // return 1
    stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
    stockSpanner.next(85);  // return 6
    ```

    ## Constraints

    - 1 <= price <= 10^5
    - At most 10^4 calls will be made to `next`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class StockSpanner:

        def __init__(self) -> None:
            raise NotImplementedError('Implement __init__')

        def next(self, price: int) -> int:
            raise NotImplementedError('Implement next')

    practice_exports = {'StockSpanner': StockSpanner}
    return (practice_exports,)


@app.cell(hide_code=True)
def _(mo):
    run_tests = mo.ui.run_button(label="Run tests")
    run_tests
    return (run_tests,)


@app.cell(hide_code=True)
def _(mo, practice_exports, run_practice_tests, run_tests):
    mo.stop(not run_tests.value, mo.md("Implement your solution, then run the tests."))
    test_result = run_practice_tests(mo.notebook_dir(), practice_exports)
    mo.vstack([
        mo.md(f"**{test_result.passed} passed · {test_result.failed} failed · "
              f"{test_result.skipped} skipped**"),
        mo.md("**All tests passed.**" if test_result.exit_code == 0 else "**Tests are not passing yet.**"),
        mo.accordion({"Test output": mo.plain_text(test_result.output)}),
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Notes

    Record your approach, complexity, and edge cases here.
    """)
    return


if __name__ == "__main__":
    app.run()
