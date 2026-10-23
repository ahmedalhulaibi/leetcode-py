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
    # 382. Linked List Random Node

    **Medium** · Linked List, Math, Reservoir Sampling, Randomized

    Given a singly linked list, return a random node's value from the linked list. Each node must have the **same probability** of being chosen.

    Implement the `Solution` class:

    - `Solution(ListNode head)` Initializes the object with the head of the singly-linked list `head`.
    - `int getRandom()` Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/03/16/getrand-linked-list.jpg)

    ```
    Input
    ["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
    [[[1, 2, 3]], [], [], [], [], []]
    Output
    [null, 1, 3, 2, 2, 3]

    Explanation
    Solution solution = new Solution([1, 2, 3]);
    solution.getRandom(); // return 1
    solution.getRandom(); // return 3
    solution.getRandom(); // return 2
    solution.getRandom(); // return 2
    solution.getRandom(); // return 3
    // getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
    ```

    ```
    Input
    ["Solution", "getRandom", "getRandom"]
    [[[7]], [], []]
    Output
    [null, 7, 7]

    Explanation
    Solution solution = new Solution([7]);
    solution.getRandom(); // return 7, the only node in the list.
    ```

    ## Constraints

    - The number of nodes in the linked list will be in the range `[1, 10^4]`.
    - `-10^4 <= Node.val <= 10^4`
    - At most `10^4` calls will be made to `getRandom`.

    **Follow up:**

    - What if the linked list is extremely large and its length is unknown to you?
    - Could you solve this efficiently without using extra space?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    import random
    from leetcode_py import ListNode

    class Solution:

        def __init__(self, head: ListNode[int] | None) -> None:
            raise NotImplementedError('Implement __init__')

        def get_random(self) -> int:
            raise NotImplementedError('Implement get_random')

    practice_exports = {'random': random, 'ListNode': ListNode, 'Solution': Solution}
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
