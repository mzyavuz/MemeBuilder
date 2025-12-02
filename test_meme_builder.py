import pytest
from meme_builder import MemeBuilder

class TestMemeBuilder:
    
    def setup_method(self):
        """Create a fresh MemeBuilder before each test."""
        self.builder = MemeBuilder()
    
    def test_submit_valid_component(self):
        result = self.builder.submit_component("user1", "WHEN THE CODE WORKS")
        assert result == True
        assert "user1" in self.builder.get_current_contributions()
    
    def test_complete_meme_workflow(self):
        # Round 1: Top text
        self.builder.submit_component("alice", "READING DOCUMENTATION")
        self.builder.cast_vote("bob", "alice")
        self.builder.finalize_round()
        
        # Round 2: Image
        self.builder.submit_component("bob", "Distracted boyfriend meme")
        self.builder.cast_vote("alice", "bob")
        self.builder.finalize_round()
        
        # Round 3: Bottom text
        self.builder.submit_component("charlie", "STACKOVERFLOW")
        self.builder.cast_vote("alice", "charlie")
        self.builder.finalize_round()
        
        assert self.builder.is_meme_complete() == True
        assert len(self.builder.get_meme()) == 3

    def test_submit_valid_component(self):
    # User successfully submits a component
        # "WHEN THE CODE WORKS" should return True
        result = self.builder.submit_component("user1", "WHEN THE CODE WORKS")
        assert result is True
    
    def test_submit_empty_component_rejected(self):
    # User submits an empty component
        result = self.builder.submit_component("alice", "")
       # Empty string should return False
        assert result is False

    def test_submit_component_too_short(self):
    #     # "NO" (2 chars) should return False
        result = self.builder.submit_component("bob", "NO")
        assert result is False
        
    def test_submit_component_at_minimum_length(self):
    #     # "LOL" (3 chars) should return True
        result = self.builder.submit_component("charlie", "LOL")
        assert result is True

    def test_submit_component_with_whitespace(self):
    #     # "   " (only spaces) should return False
        result = self.builder.submit_component("diana", "   ")
        assert result is False
        
    def test_submit_component_with_leading_trailing_whitespace(self):
    #     # "  FUNNY TEXT  " should return True (trimmed)
        result = self.builder.submit_component("emre", "  FUNNY TEXT  ")
        assert result is True

    def test_submit_component_with_special_characters(self):
    #     # "LOL!!! :D" should return True
        result = self.builder.submit_component("fatma", "LOL!!! :D")
        assert result is True
    
    def test_submit_component_with_numbers(self):
    #     # "TOP 10 REASONS" should return True
        result = self.builder.submit_component("charlie", "TOP 10 REASONS")
        assert result is True

    def test_submit_component_at_large_length(self):
    #     # 200 characters should return True
        long_text = "HA" * 100
        result = self.builder.submit_component("bob", long_text)
        assert result is True

    def test_submit_component_with_all_caps(self):
    #     # "WHEN YOU SEE THE DEADLINE" should work (memes love caps!)
        result = self.builder.submit_component("dave", "WHEN YOU SEE THE DEADLINE")
        assert result is True
        
    def test_submit_component_replaces_previous(self):
    #     # Same user submitting twice replaces first submission
        self.builder.submit_component("ayse", "AYSE SUBMIT FIRST SUBMISSION")
        self.builder.submit_component("ayse", "AYSE SUBMIT SECOND SUBMISSION")
        contributions = self.builder.get_current_contributions()
        assert contributions["ayse"] == "AYSE SUBMIT SECOND SUBMISSION"
        
    def test_vote_for_existing_contribution(self):
    #     # Valid vote should return True
        self.builder.submit_component("fatma", "FUNNY TEXT")
        result = self.builder.cast_vote("zeynep", "fatma")
        assert result is True
        
    def test_vote_for_own_submission_rejected(self):
    #     # User cannot vote for themselves
        self.builder.submit_component("gokhan", "HILARIOUS TEXT")
        result = self.builder.cast_vote("gokhan", "gokhan")
        assert result is False
        
    def test_vote_twice_rejected(self):
    #     # Second vote attempt should return False
        self.builder.submit_component("mehmet", "WHEN I CODE")
        self.builder.submit_component("aylin", "DEBUGGING IS FUN")
        self.builder.cast_vote("emre", "mehmet")
        result = self.builder.cast_vote("emre", "aylin")
        assert result is False
        
    def test_vote_for_nonexistent_user(self):
    #     # Voting for user who didn't submit should return False
        self.builder.submit_component("charlie", "COOL MEME")
        result = self.builder.cast_vote("ahmet", "nonexistent_user")
        assert result is False
        
    def test_get_winner_clear_majority(self):
        #     # User with most votes wins
        # Alice submits: "WHEN YOU FINALLY FIX THE BUG"
        # Bob submits: "ME EXPLAINING MY CODE TO THE RUBBER DUCK"
        # Charlie submits: "POV: YOU FORGOT A SEMICOLON"
        # Dave votes for Alice's text
        # Eve votes for Alice's text
        # Bob votes for Charlie's text
        # Charlie votes for Alice's text
        # Result: Alice's text wins (3 votes) → Added to meme
        # Meme components: ["WHEN YOU FINALLY FIX THE BUG"]
        self.builder.submit_component("alice", "WHEN YOU FINALLY FIX THE BUG")
        self.builder.submit_component("bob", "ME EXPLAINING MY CODE TO THE RUBBER DUCK")
        self.builder.submit_component("charlie", "POV: YOU FORGOT A SEMICOLON")
        
        self.builder.cast_vote("dave", "alice")
        self.builder.cast_vote("eve", "alice")
        self.builder.cast_vote("bob", "charlie")
        self.builder.cast_vote("charlie", "alice")
        
        winner = self.builder.get_winner()
        assert winner == "alice"

        
    def test_get_winner_returns_none_on_tie(self):
    #     # Two-way tie should return None
        self.builder.submit_component("bob", "Surprised Pikachu")
        self.builder.submit_component("eve", "Drake pointing approvingly")
        
        self.builder.cast_vote("bob", "eve")
        self.builder.cast_vote("eve", "bob") 
        
        winner = self.builder.get_winner()
        assert winner is None
        
    def test_get_winner_three_way_tie(self):
    #     # Multiple users tied should return None
        self.builder.submit_component("alice", "WHEN YOU FINALLY FIX THE BUG")
        self.builder.submit_component("bob", "ME EXPLAINING MY CODE TO THE RUBBER DUCK")
        self.builder.submit_component("charlie", "POV: YOU FORGOT A SEMICOLON")
        self.builder.cast_vote("alice", "bob")
        self.builder.cast_vote("bob", "charlie")
        self.builder.cast_vote("charlie", "alice")
        winner = self.builder.get_winner()
        assert winner is None
        
    def test_get_winner_no_votes(self):
    #     # If no votes cast, should return None
        self.builder.submit_component("alice", "WHEN YOU FINALLY FIX THE BUG")
        self.builder.submit_component("bob", "ME EXPLAINING MY CODE TO THE RUBBER DUCK")
        winner = self.builder.get_winner()
        assert winner is None
        
    def test_single_contribution_can_win(self):
    #     # Only one submission can win even with 0 votes
        self.builder.submit_component("alice", "BUT IT BREAKS PRODUCTION")
        winner = self.builder.get_winner()
        assert winner == "alice"
        
    def test_finalize_adds_winner_to_meme(self):
    #     # Winning component should be added to meme_components
        self.builder.submit_component("alice", "WHEN YOU FINALLY FIX THE BUG")
        self.builder.submit_component("bob", "ME EXPLAINING MY CODE TO THE RUBBER DUCK")
        self.builder.cast_vote("charlie", "alice")
        self.builder.finalize_round()
        meme = self.builder.get_meme()
        assert meme[-1] == "WHEN YOU FINALLY FIX THE BUG"
        
    def test_finalize_clears_round_state(self):
    #     # After finalize, contributions and votes should be empty
        self.builder.submit_component("alice", "BUT IT BREAKS PRODUCTION")
        self.builder.finalize_round()
        contributions = self.builder.get_current_contributions()
        votes = self.builder.votes
        assert contributions == {}
        assert votes == {}
        
    def test_finalize_preserves_meme_history(self):
    #     # Previous meme components should remain after finalization
        self.builder.submit_component("alice", "WHEN YOU FINALLY FIX THE BUG")
        self.builder.cast_vote("bob", "alice")
        self.builder.finalize_round()
        
        # Bob submits: "Surprised Pikachu"
        # Eve submits: "Drake pointing approvingly"
        self.builder.submit_component("bob", "Surprised Pikachu")
        self.builder.submit_component("eve", "Drake pointing approvingly")
        self.builder.cast_vote("dave", "bob")
        self.builder.finalize_round()
        
        meme = self.builder.get_meme()
        assert meme == ["WHEN YOU FINALLY FIX THE BUG", "Surprised Pikachu"]
        
    def test_finalize_with_tie_returns_false(self):
    #     # Cannot finalize when there's a tie
        self.builder.submit_component("alice", "WHEN YOU FINALLY FIX THE BUG")
        self.builder.submit_component("bob", "ME EXPLAINING MY CODE TO THE RUBBER DUCK")
        self.builder.cast_vote("charlie", "alice")
        self.builder.cast_vote("dave", "bob")
        result = self.builder.finalize_round()
        assert result is False
        
    def test_complete_meme_three_rounds(self):
    #     # Build a complete meme: top text, image, bottom text
        # Round 1
        self.builder.submit_component("alice", "WHEN YOU WRITE TESTS")
        self.builder.cast_vote("bob", "alice")
        self.builder.finalize_round()
        
        # Round 2
        self.builder.submit_component("bob", "Programmer meme image")
        self.builder.cast_vote("alice", "bob")
        self.builder.finalize_round()
        
        # Round 3
        self.builder.submit_component("charlie", "AND THEY ALL PASS")
        self.builder.cast_vote("alice", "charlie")
        self.builder.finalize_round()
        
        assert self.builder.is_meme_complete() == True
        meme = self.builder.get_meme()
        assert meme == [
            "WHEN YOU WRITE TESTS",
            "Programmer meme image",
            "AND THEY ALL PASS"
        ]
        
    def test_is_meme_complete_with_three_components(self):
    #     # Should return True when exactly 3 components
        self.builder.meme_components = [
            "TOP TEXT",
            "IMAGE",
            "BOTTOM TEXT"
        ]
        assert self.builder.is_meme_complete() is True
        
    def test_is_meme_complete_with_two_components(self):
    #     # Should return False when only 2 components
        self.builder.meme_components = [
            "TOP TEXT",
            "IMAGE"
        ]
        assert self.builder.is_meme_complete() is False
        
    def test_is_meme_complete_with_four_components(self):
    #     # Should return False when more than 3 components
        self.builder.meme_components = [
            "TOP TEXT",
            "IMAGE",
            "BOTTOM TEXT",
            "EXTRA TEXT"
        ]
        assert self.builder.is_meme_complete() is False

