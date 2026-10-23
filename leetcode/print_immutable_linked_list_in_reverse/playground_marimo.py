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
    # 1265. Print Immutable Linked List in Reverse

    **Medium** · Stack, Recursion, Linked List, Two Pointers

    You are given an immutable linked list, print out all values of each node in reverse with the help of the following interface:

    - `ImmutableListNode`: An interface of immutable linked list, you are given the head of the list.

    You need to use the following functions to access the linked list (you **can't** access the `ImmutableListNode` directly):

    - `ImmutableListNode.printValue()`: Print value of the current node.
    - `ImmutableListNode.getNext()`: Return the next node.

    The input is only given to initialize the linked list internally. You must solve this problem without modifying the linked list. In other words, you must operate the linked list using only the mentioned APIs.

    The Python harness models the judge: each `print_value()` call records the node value, and the recorded values are compared with the expected reversed sequence.

    ## Examples

    ```
    Input: head = [1,2,3,4]
    Output: [4,3,2,1]
    ```

    ```
    Input: head = [0,-4,-1,3,-5]
    Output: [-5,3,-1,-4,0]
    ```

    ```
    Input: head = [-2,0,6,4,4,-6]
    Output: [-6,4,4,6,0,-2]
    ```

    ## Constraints

    - The length of the linked list is between `[1, 1000]`.
    - The value of each node in the linked list is between `[-1000, 1000]`.

    **Follow up:**

    - Could you solve this problem in constant space complexity?
    - Could you solve this problem in linear time complexity and less than linear space complexity?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from typing import ClassVar

    class ImmutableListNode:
        printed: 'ClassVar[list[int]]' = []

        def __init__(self, value: 'int', next_node: 'ImmutableListNode | None'=None) -> 'None':
            self.value = value
            self.next_node = next_node

        def get_next(self) -> 'ImmutableListNode | None':
            return self.next_node

        def print_value(self) -> 'None':
            ImmutableListNode.printed.append(self.value)

    class Solution:

        def print_linked_list_in_reverse(self, head: 'ImmutableListNode') -> 'None':
            raise NotImplementedError('Implement print_linked_list_in_reverse')

    practice_exports = {'ClassVar': ClassVar, 'ImmutableListNode': ImmutableListNode, 'Solution': Solution}
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
