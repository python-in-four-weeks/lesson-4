# Lesson 4 Independent Challenges

## Challenge 1: `is_palindrome` and `test_is_palindrome_with_valid_palindrome` (5 points)

| Function parameter(s)     | Function return(s)                                              |
|---------------------------|-----------------------------------------------------------------|
| `text`, the starting text | Whether or not the text is the same forwards as it is backwards |

A function called `is_palindrome` has been partially written for you. An example test called `test_is_palindrome_with_invalid_palindrome` has also been written, which already passes and can be used as an example. You need to complete the test called `test_is_palindrome_with_valid_palindrome` (which should fail at first) and then add a suitable implementation of `is_palindrome` to make your new test pass. Note that the existing test, `test_is_palindrome_with_invalid_palindrome`, should not break.

A palindrome is a piece of text which reads the same forwards as it does backwards. Your `is_palindrome` function should return a boolean value (`True` or `False`) to indicate whether the given text is a palindrome.

## Challenge 2: `is_palindrome` and `test_is_palindrome_parametrized` (5 points)

| Function parameter(s)     | Function return(s)                                              |
|---------------------------|-----------------------------------------------------------------|
| `text`, the starting text | Whether or not the text is the same forwards as it is backwards |

An improved test for `is_palindrome` has been written called `test_is_palindrome_parametrized`. It is just missing a valid palindrome test case: the invalid palindrome test case has already been added, along with the test implementation and your function implementation from the previous challenge. You should add a suitable valid palindrome test case in the right location.

## Challenge 3: `sum_of_numbers_up_to_n` and `test_sum_of_numbers_up_to_n` (10 points)

| Function parameter(s)                       | Function return(s)                       |
|---------------------------------------------|------------------------------------------|
| `n`, the upper limit of the sum (inclusive) | The sum of all the numbers from 0 to `n` |

A function called `sum_of_numbers_up_to_n` and a test called `test_sum_of_numbers_up_to_n` have been partially written for you. You need to add at least one new test case, and add a suitable implementation of `sum_of_numbers_up_to_n` to make your new test case(s) pass.

Your `sum_of_numbers_up_to_n` function should return the total of all the integers from 0 to `n` inclusive.

## Challenge 4: `is_numeric` and `test_is_numeric` (10 points)

| Function parameter(s)     | Function return(s)                                |
|---------------------------|---------------------------------------------------|
| `text`, the starting text | Whether or not the text represents a valid number |

A function called `is_numeric` has been partially written for you, and some test cases have been provided for a test called `test_is_numeric`. You need to implement the test itself as well as the function.

Your `is_numeric` function should return a boolean value (`True` or `False`) to indicate whether the given text can be converted to a float without error.

## Challenge 5: `is_sorted` and `test_is_sorted` (20 points)

| Function parameter(s)            | Function return(s)                                       |
|----------------------------------|----------------------------------------------------------|
| `numbers`, a sequence of numbers | Whether or not the sequence is sorted in ascending order |

A function called `is_sorted` and a test called `test_is_sorted` have been partially written for you. You need to provide some test cases and implement the test and the function.

Your `is_sorted` function should return a boolean value (`True` or `False`) to indicate whether the given sequence of numbers is sorted in ascending order.

## Challenge 6: `login` and `test_login` (20 points)

A function called `login` and a test called `test_login` have been partially written for you. You need to provide some test cases and implement the test and the function.

Your `login` function should ask the user for a single response: what the password is. If they type the correct password (which is `Python123`), the function should return `True`. Otherwise, the function should return `False`.

**Note: you may find it helpful to look at the tests for the lesson 2 challenges for a reminder of how to mock the `input` function.**

## Challenge 7: `should_visit_moon` and `test_should_visit_moon` (30 points)

| Function parameter(s) | Function return(s) |
|-----------------------|--------------------|
| None                  | None               |

A function called `should_visit_moon` and a test called `test_should_visit_moon` have been partially written for you. You need to provide some test cases and implement the test and the function.

Your `should_visit_moon` function should firstly ask the user for a single response: whether they would like to visit the moon. If their response is the exact word `yes`, ask them a further question: whether they can afford to visit the moon. If their response is the exact word `yes` again, print the following exact text:

```
You should visit the moon.
```

Otherwise, if their response to the second question is the exact word `no`, print the following exact text instead:

```
You shouldn't visit the moon if you can't afford to.
```

Otherwise, if their response to the second question matches neither word, print the following exact text:

```
I'm not sure whether you should visit the moon - it depends whether you can afford to.
```

Back to the original question, if their response to whether they want to visit the moon is the exact word `no`, print the following exact text:

```
You shouldn't visit the moon if you don't want to.
```

Finally, if their response to the original question was neither `yes` nor `no`, print the following exact text:

```
I'm not sure whether you should visit the moon - it depends whether you want to.
```

**Note: you may find it helpful to look at the tests for the lesson 2 challenges for a reminder of how to mock the `input` and `print` functions.**
