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
    # 430. Flatten a Multilevel Doubly Linked List

    **Medium** · Linked List, Depth-First Search, Doubly-Linked List

    You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional **child pointer**. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a **multilevel data structure** as shown in the example below.

    Given the `head` of the first level of the list, **flatten** the list so that all the nodes appear in a single-level, doubly linked list. Let `curr` be a node with a child list. The nodes in the child list should appear **after** `curr` and **before** `curr.next` in the flattened list.

    Return the head of the flattened list. The nodes in the list must have all of their child pointers set to `null`.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/11/09/flatten11.jpg)

    ```
    Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
    Output: [1,2,3,7,8,11,12,9,10,4,5,6]
    Explanation: The multilevel linked list in the input is shown.
    After flattening the multilevel linked list it becomes:
    ```

    ![Flattened list](https://assets.leetcode.com/uploads/2021/11/09/flatten12.jpg)

    ![Example 2](https://assets.leetcode.com/uploads/2021/11/09/flatten2.1jpg)

    ```
    Input: head = [1,2,null,3]
    Output: [1,3,2]
    Explanation: The multilevel linked list in the input is shown.
    After flattening the multilevel linked list it becomes:
    ```

    ![Flattened list](https://assets.leetcode.com/uploads/2021/11/24/list.jpg)

    ```
    Input: head = []
    Output: []
    Explanation: There could be empty list in the input.
    ```

    ## Constraints

    - The number of Nodes will not exceed 1000.
    - 1 <= Node.val <= 10^5

    **How the multilevel linked list is represented in test cases:**

    We use the multilevel linked list from Example 1 above:

    ```
     1---2---3---4---5---6--NULL
             |
             7---8---9---10--NULL
                 |
                 11--12--NULL
    ```

    The serialization of each level is as follows:

    ```
    [1,2,3,4,5,6,null]
    [7,8,9,10,null]
    [11,12,null]
    ```

    To serialize all levels together, we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:

    ```
    [1,    2,    3, 4, 5, 6, null]
                 |
    [null, null, 7,    8, 9, 10, null]
                       |
    [            null, 11, 12, null]
    ```

    Merging the serialization of each level and removing trailing nulls we obtain:

    ```
    [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
    ```

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Node:

        def __init__(self, val: 'int'=0, prev: 'Node | None'=None, next: 'Node | None'=None, child: 'Node | None'=None) -> 'None':
            self.val = val
            self.prev = prev
            self.next = next
            self.child = child

    class Solution:

        def flatten(self, head: 'Node | None') -> 'Node | None':
            raise NotImplementedError('Implement flatten')

    practice_exports = {'Node': Node, 'Solution': Solution}
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
