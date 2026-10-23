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
    # 237. Delete Node in a Linked List

    **Medium** · Linked List

    There is a singly-linked list `head` and we want to delete a node `node` in it.

    You are given the node to be deleted `node`. You will **not be given access** to the first node of `head`.

    All the values of the linked list are **unique**, and it is guaranteed that the given node `node` is not the last node in the linked list.

    Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

    - The value of the given node should not exist in the linked list.
    - The number of nodes in the linked list should decrease by one.
    - All the values before `node` should be in the same order.
    - All the values after `node` should be in the same order.

    **Custom testing:**

    - For the input, you should provide the entire linked list `head` and the node to be given `node`. `node` should not be the last node of the list and should be an actual node in the list.
    - We will build the linked list and pass the node to your function.
    - The output will be the entire list after calling your function.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/09/01/node1.jpg)

    ```
    Input: head = [4,5,1,9], node = 5
    Output: [4,1,9]
    Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2020/09/01/node2.jpg)

    ```
    Input: head = [4,5,1,9], node = 1
    Output: [4,5,9]
    Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
    ```

    ## Constraints

    - The number of the nodes in the given list is in the range `[2, 1000]`.
    - `-1000 <= Node.val <= 1000`
    - The value of each node in the list is **unique**.
    - The `node` to be deleted is **in the list** and is **not a tail** node.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import ListNode

    class Solution:

        def delete_node(self, node: ListNode[int]) -> None:
            raise NotImplementedError('Implement delete_node')

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
