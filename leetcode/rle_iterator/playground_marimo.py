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
    # 900. RLE Iterator

    **Medium** · Array, Design, Counting, Iterator

    We can use run-length encoding (i.e., RLE) to encode a sequence of integers. In a run-length encoded array of even length `encoding` (0-indexed), for all even `i`, `encoding[i]` tells us the number of times that the non-negative integer value `encoding[i + 1]` is repeated in the sequence.

    - For example, the sequence `arr = [8,8,8,5,5]` can be encoded to be `encoding = [3,8,2,5]`. `encoding = [3,8,0,9,2,5]` and `encoding = [2,8,1,8,2,5]` are also valid RLE of `arr`.

    Given a run-length encoded array, design an iterator that iterates through it.

    Implement the `RLEIterator` class:

    - `RLEIterator(int[] encoded)` Initializes the object with the encoded array `encoded`.
    - `int next(int n)` Exhausts the next `n` elements and returns the last element exhausted in this way. If there is no element left to exhaust, return `-1` instead.

    ## Examples

    ```
    Input
    ["RLEIterator", "next", "next", "next", "next"]
    [[[3, 8, 0, 9, 2, 5]], [2], [1], [1], [2]]
    Output
    [null, 8, 8, 5, -1]

    Explanation
    RLEIterator rLEIterator = new RLEIterator([3, 8, 0, 9, 2, 5]); // This maps to the sequence [8,8,8,5,5].
    rLEIterator.next(2); // exhausts 2 terms of the sequence, returning 8. The remaining sequence is now [8, 5, 5].
    rLEIterator.next(1); // exhausts 1 term of the sequence, returning 8. The remaining sequence is now [5, 5].
    rLEIterator.next(1); // exhausts 1 term of the sequence, returning 5. The remaining sequence is now [5].
    rLEIterator.next(2); // exhausts 2 terms, returning -1. This is because the first term exhausted was 5, but the second term did not exist. Since the last term exhausted does not exist, we return -1.
    ```

    ## Constraints

    - `2 <= encoding.length <= 1000`
    - `encoding.length` is even.
    - `0 <= encoding[i] <= 10^9`
    - `1 <= n <= 10^9`
    - At most `1000` calls will be made to `next`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class RLEIterator:

        def __init__(self, encoding: list[int]) -> None:
            raise NotImplementedError('Implement __init__')

        def next(self, n: int) -> int:
            raise NotImplementedError('Implement next')

    practice_exports = {'RLEIterator': RLEIterator}
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
