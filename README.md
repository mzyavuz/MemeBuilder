# What I have done & learn

**1. I learned to navigate test creation with tool support**

I utilized VSCode Autocomplete not just for speed, but as a learning aid. It helped me understand standard naming conventions for test functions and suggested potential edge cases I hadn't initially considered. This process turned "writing tests" into an interactive learning session where I discovered how to structure my code effectively.

**2. I followed a "Start Simple, Then Scale" strategy**

I started with the most basic validation tests, such as `test_submit_component_too_short` and `test_submit_empty_component_rejected`. Once I was confident these small units worked, I increased the complexity to cover full game workflows, eventually writing `test_complete_meme_three_rounds` to verify the entire system lifecycle.

**3. I practiced Test-Driven Development (TDD)**

I refined the application logic based on test failures. When my initial tests failed with `AttributeError` messages because the `MemeBuilder` class lacked necessary accessors, I reacted by implementing the missing or misnamed methods. Specifically:
* I added `get_current_contributions()` when `test_submit_valid_component` failed.
* I added `get_meme()` when `test_complete_meme_workflow` failed.

>FAILED test_meme_builder.py::TestMemeBuilder::test_submit_valid_component - AttributeError: 'MemeBuilder' object has no attribute 'get_current_contributions'. Did you mean: 'curre...
FAILED test_meme_builder.py::TestMemeBuilder::test_complete_meme_workflow - AttributeError: 'MemeBuilder' object has no attribute 'get_meme'

**4. I balanced required scenarios with creative data**

Following my instructor's advice to be careful with test data, I ensured my tests were realistic. I used the specific scenario texts provided in the requirements but also enriched the test suite by creating my own meme content (e.g., "WHEN THE CODE WORKS", "STACKOVERFLOW") to ensure the system handled diverse text inputs correctly.


# MemeBuilder

**MemeBuilder** is a collaborative meme-building application where multiple users work together to create memes one component at a time. Designed as a coding exercise, this project serves as a practical playground for learning and implementing comprehensive unit tests for real-world application logic.

## 📖 Overview

The application manages a game-like process for creating memes. A meme is built in rounds (e.g., Top Text, Image, Bottom Text). In each round:
1.  **Submission Phase:** Users submit candidate contributions.
2.  **Voting Phase:** Everyone votes on their favorite submission.
3.  **Selection Phase:** The system calculates the winner based on votes.
4.  **Finalization:** The winning contribution is permanently added to the meme, and the next round begins.

## 🚀 How It Works

The `MemeBuilder` class manages the state of the game. Here is the lifecycle of a typical round:

1.  **Start Round:** The system accepts submissions for the current component (e.g., Top Text).
2.  **Submit:** Users send their text or image descriptions.
    * *Rule:* A user can replace their own submission by submitting again.
3.  **Vote:** Users cast votes for submissions they like.
    * *Rule:* You cannot vote for yourself.
    * *Rule:* You can only vote once per round.
4.  **Finalize:** The round ends.
    * The submission with the most votes wins.
    * If there is a tie, no winner is selected (the round must continue or be resolved).
    * The winner is added to the final meme.
    * All votes and submissions are cleared for the next round.

### Example Scenario

**Round 1: Top Text**
* **Alice** submits: *"WHEN YOU FINALLY FIX THE BUG"*
* **Bob** submits: *"ME EXPLAINING MY CODE TO THE RUBBER DUCK"*
* **Charlie** submits: *"POV: YOU FORGOT A SEMICOLON"*

**Voting:**
* Dave, Eve, and Charlie vote for **Alice**.
* Bob votes for **Charlie**.

**Result:**
* Alice wins (3 votes).
* Meme so far: `["WHEN YOU FINALLY FIX THE BUG"]`

---

## 🛠️ Development & Testing

This repository is primarily an exercise in **Unit Testing**. The goal is to write tests that cover "Happy Paths," edge cases, and invalid operations.

### Prerequisites
* Python 3.x
* `pytest` (for running tests)

### Installation
1.  Clone the repository:
    ```bash
    git clone [https://github.com/mzyavuz/MemeBuilder.git](https://github.com/mzyavuz/MemeBuilder.git)
    cd MemeBuilder
    ```
2.  Install dependencies:
    ```bash
    pip install pytest
    ```

### Running Tests
To verify the application logic, run the test suite using `pytest`.

**Run all tests:**
```bash
pytest