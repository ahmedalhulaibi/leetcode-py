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
    mo.md(r"""
    # 375. Guess Number Higher or Lower II

    **Medium** · Math, Dynamic Programming, Minimax, Game Theory

    We are playing the Guessing Game. The game will work as follows:

    <ol>
        <li>I pick a number between <code>1</code> and <code>n</code>.</li>
        <li>You guess a number.</li>
        <li>If you guess the right number, <strong>you win the game</strong>.</li>
        <li>If you guess the wrong number, then I will tell you whether the number I picked is <strong>higher or lower</strong>, and you will continue guessing.</li>
        <li>Every time you guess a wrong number <code>x</code>, you will pay <code>x</code> dollars. If you run out of money, <strong>you lose the game</strong>.</li>
    </ol>

    Given a particular <code>n</code>, return <em>the minimum amount of money you need to <strong>guarantee a win regardless of what number I pick</strong></em>.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/09/10/graph.png)

    ```
    Input: n = 10
    Output: 16
    Explanation: The winning strategy is as follows:
    - The range is [1,10]. Guess 7.
      - If this is my number, your total is $0. Otherwise, you pay $7.
      - If my number is higher, the range is [8,10]. Guess 9.
        - If this is my number, your total is $7. Otherwise, you pay $9.
        - If my number is higher, it must be 10. Guess 10. Your total is $7 + $9 = $16.
        - If my number is lower, it must be 8. Guess 8. Your total is $7 + $9 = $16.
      - If my number is lower, the range is [1,6]. Guess 3.
        - If this is my number, your total is $7. Otherwise, you pay $3.
        - If my number is higher, the range is [4,6]. Guess 5.
          - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $5.
          - If my number is higher, it must be 6. Guess 6. Your total is $7 + $3 + $5 = $15.
          - If my number is lower, it must be 4. Guess 4. Your total is $7 + $3 + $5 = $15.
        - If my number is lower, the range is [1,2]. Guess 1.
          - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $1.
          - If my number is higher, it must be 2. Guess 2. Your total is $7 + $3 + $1 = $11.
    The worst case in all these scenarios is that you pay $16. Hence, you only need $16 to guarantee a win.
    ```

    ```
    Input: n = 1
    Output: 0
    Explanation: There is only one possible number, so you can guess 1 and not have to pay anything.
    ```

    ```
    Input: n = 2
    Output: 1
    Explanation: There are two possible numbers, 1 and 2.
    - Guess 1.
      - If this is my number, your total is $0. Otherwise, you pay $1.
      - If my number is higher, it must be 2. Guess 2. Your total is $1.
    The worst case is that you pay $1.
    ```

    ## Constraints

    - 1 <= n <= 200



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def get_money_amount(self, n: int) -> int:
            raise NotImplementedError('Implement get_money_amount')

    practice_exports = {'Solution': Solution}
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
