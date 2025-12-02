# Playing with Unit Tests


# Unit Testing Exercise: Collaborative Meme Builder

## Overview

You will build and test a collaborative meme-building application where multiple users work together to create memes one component at a time. In each round, users submit candidate contributions (top text, bottom text, or image descriptions), everyone votes on their favorite, and the winning contribution gets added to the meme. This exercise will teach you how to write comprehensive unit tests for real-world application logic.

## The Application

### How It Works

The `MemeBuilder` manages collaborative meme creation:

1. **Submission Phase**: Users submit candidate contributions for the next part of the meme
2. **Voting Phase**: Users vote on which submitted contribution they like best  
3. **Selection Phase**: The system determines the winning contribution
4. **Finalization**: The winning contribution is added to the meme, and a new round begins

### Example Scenario
Round 1 - Top Text:

Alice submits: "WHEN YOU FINALLY FIX THE BUG"
Bob submits: "ME EXPLAINING MY CODE TO THE RUBBER DUCK"
Charlie submits: "POV: YOU FORGOT A SEMICOLON"

Voting:

Dave votes for Alice's text
Eve votes for Alice's text
Bob votes for Charlie's text
Charlie votes for Alice's text
Result: Alice's text wins (3 votes) → Added to meme
Meme components: ["WHEN YOU FINALLY FIX THE BUG"]

Round 2 - Image Description:

Bob submits: "Surprised Pikachu"
Eve submits: "Drake pointing approvingly"

Round 3 - Bottom Text:

Alice submits: "BUT IT BREAKS PRODUCTION"


## Starter Code## 

### Part 1: Implement the Methods 

Complete  the stubbed methods in the `MemeBuilder` class according to the specifications in their docstrings. Pay careful attention to the rules for each method.

### Part 2: Write Comprehensive Tests

Create a test file (e.g., `test_meme_builder.py`) with unit tests that verify your implementation. Your test suite should cover:

#### Test Categories

**1. Happy Path Tests** - Normal, expected usage 
- Submitting valid components
- Casting valid votes
- Winning component selection with clear winner
- Round finalization with a winner
- Building a complete 3-component meme
- Checking meme completion status

**2. Edge Cases** - Boundary and special conditions
- Empty or whitespace-only components
- Components at exactly 3 and 200 characters
- Ties in voting
- No votes cast
- Single contribution (no competition)
- Replacing a previous submission
- Meme with 0, 1, 2, or 4 components

**3. Invalid Operations** - Things that should fail
- Voting for non-existent contributions
- Voting twice in same round
- Voting for your own submission
- Finalizing when there's a tie

**4. State Management** - Verify state changes correctly
- Round finalization clears contributions and votes
- Meme history preserved across rounds
- Independent rounds don't interfere with each other

## Test Case Examples to Consider

Here are specific scenarios your tests should cover:

```python
# Example test cases (write these and more!)

def test_submit_valid_component():
    # User successfully submits a component
    
def test_submit_empty_component_rejected():
    # Empty string should return False
    
def test_submit_component_too_short():
    # "NO" (2 chars) should return False
    
def test_submit_component_at_minimum_length():
    # "LOL" (3 chars) should return True
    
def test_submit_component_with_all_caps():
    # "WHEN YOU SEE THE DEADLINE" should work (memes love caps!)
    
def test_submit_component_replaces_previous():
    # Same user submitting twice replaces first submission
    
def test_vote_for_existing_contribution():
    # Valid vote should return True
    
def test_vote_for_own_submission_rejected():
    # User cannot vote for themselves
    
def test_vote_twice_rejected():
    # Second vote attempt should return False
    
def test_vote_for_nonexistent_user():
    # Voting for user who didn't submit should return False
    
def test_get_winner_clear_majority():
    # User with most votes wins
    
def test_get_winner_returns_none_on_tie():
    # Two-way tie should return None
    
def test_get_winner_three_way_tie():
    # Multiple users tied should return None
    
def test_get_winner_no_votes():
    # If no votes cast, should return None
    
def test_single_contribution_can_win():
    # Only one submission can win even with 0 votes
    
def test_finalize_adds_winner_to_meme():
    # Winning component should be added to meme_components
    
def test_finalize_clears_round_state():
    # After finalize, contributions and votes should be empty
    
def test_finalize_preserves_meme_history():
    # Previous meme components should remain after finalization
    
def test_finalize_with_tie_returns_false():
    # Cannot finalize when there's a tie
    
def test_complete_meme_three_rounds():
    # Build a complete meme: top text, image, bottom text
    
def test_is_meme_complete_with_three_components():
    # Should return True when exactly 3 components
    
def test_is_meme_complete_with_two_components():
    # Should return False when only 2 components
    
def test_is_meme_complete_with_four_components():
    # Should return False when more than 3 components
