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
    # 1472. Design Browser History

    **Medium** · Array, Linked List, Stack, Design, Doubly-Linked List, Data Stream

    You have a **browser** of one tab where you start on the `homepage` and you can visit another `url`, get back in the history number of `steps` or move forward in the history number of `steps`.

    Implement the `BrowserHistory` class:

    - `BrowserHistory(string homepage)` Initializes the object with the `homepage` of the browser.
    - `void visit(string url)` Visits `url` from the current page. It clears up all the forward history.
    - `string back(int steps)` Move `steps` back in history. If you can only return `x` steps in the history and `steps > x`, you will return only `x` steps. Return the current `url` after moving back in history **at most** `steps`.
    - `string forward(int steps)` Move `steps` forward in history. If you can only forward `x` steps in the history and `steps > x`, you will forward only `x` steps. Return the current `url` after forwarding in history **at most** `steps`.

    ## Examples

    ```
    Input
    ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
    [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
    Output
    [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]
    ```

    **Explanation:**
    ```
    BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
    browserHistory.visit("google.com");   // You are in "leetcode.com". Visit "google.com"
    browserHistory.visit("facebook.com"); // You are in "google.com". Visit "facebook.com"
    browserHistory.visit("youtube.com");  // You are in "facebook.com". Visit "youtube.com"
    browserHistory.back(1);               // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
    browserHistory.back(1);               // You are in "facebook.com", move back to "google.com" return "google.com"
    browserHistory.forward(1);            // You are in "google.com", move forward to "facebook.com" return "facebook.com"
    browserHistory.visit("linkedin.com"); // You are in "facebook.com". Visit "linkedin.com"
    browserHistory.forward(2);            // You are in "linkedin.com", you cannot move forward any steps.
    browserHistory.back(2);               // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
    browserHistory.back(7);               // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
    ```

    ## Constraints

    - `1 <= homepage.length <= 20`
    - `1 <= url.length <= 20`
    - `1 <= steps <= 100`
    - `homepage` and `url` consist of `'.'` or lower case English letters.
    - At most `5000` calls will be made to `visit`, `back`, and `forward`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class BrowserHistory:

        def __init__(self, homepage: str) -> None:
            raise NotImplementedError('Implement __init__')

        def visit(self, url: str) -> None:
            raise NotImplementedError('Implement visit')

        def back(self, steps: int) -> str:
            raise NotImplementedError('Implement back')

        def forward(self, steps: int) -> str:
            raise NotImplementedError('Implement forward')

    practice_exports = {'BrowserHistory': BrowserHistory}
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
