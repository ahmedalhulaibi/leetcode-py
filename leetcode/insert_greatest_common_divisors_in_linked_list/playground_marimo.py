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
    # 2807. Insert Greatest Common Divisors in Linked List

    **Medium** · Linked List, Math, Number Theory

    Given the `head` of a linked list, return the list after inserting the **greatest common divisor** of each pair of adjacent nodes.

    Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

    The **greatest common divisor** of two numbers is the largest positive integer that evenly divides both numbers.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2023/07/18/ex1_copy.png)

    ```
    Input: head = [18,6,10,3]
    Output: [18,6,6,2,10,1,3]
    Explanation:
    - We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.
    - We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.
    - We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.
    There are no more adjacent nodes, so we return the linked list.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2023/07/18/ex2_copy1.png)

    ```
    Input: head = [7]
    Output: [7]
    Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes.
    There are no pairs of adjacent nodes, so we return the initial linked list.
    ```

    ## Constraints

    - The number of nodes in the list is in the range `[1, 5000]`.
    - `1 <= Node.val <= 1000`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import ListNode

    class Solution:

        def insert_greatest_common_divisors(self, head: ListNode[int] | None) -> ListNode[int] | None:
            raise NotImplementedError('Implement insert_greatest_common_divisors')

    practice_exports = {'ListNode': ListNode, 'Solution': Solution}
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
