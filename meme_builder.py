class MemeBuilder:
    def __init__(self):
        self.meme_components = []
        self.current_contributions = {}  # Maps user -> component text
        self.votes = {}  # Maps voter -> author they voted for

    def submit_component(self, user, component):
        """
        Allows a user to submit a component (text or description).
        Replaces previous submission if user submits again.
        """

        if not isinstance(component, str):
            return False
        
        if not component or not component.strip():
            return False
        
        if len(component) < 3:
            return False
            
        self.current_contributions[user] = component
        return True

    def cast_vote(self, voter, author):
        """
        Allows a user to vote for a specific author's contribution.
        """
        # Check if author exists in current contributions
        if author not in self.current_contributions:
            return False
            
        # User cannot vote for themselves
        if voter == author:
            return False
            
        # User cannot vote twice
        if voter in self.votes:
            return False
            
        self.votes[voter] = author
        return True
    
    def get_current_contributions(self):
        """
        Returns the current contributions for the round.
        """
        return self.current_contributions
    
    def get_meme(self):
        """
        Returns the completed meme components.
        """
        return self.meme_components

    def get_winner(self):
        """
        Determines the winner of the current round.
        Returns the username of the winner, or None if there is a tie or no clear winner.
        """
        if not self.current_contributions:
            return None
            
        # Special case: Single contribution wins automatically even with 0 votes
        if len(self.current_contributions) == 1:
            return list(self.current_contributions.keys())[0]

        # Count votes
        vote_counts = {user: 0 for user in self.current_contributions}
        for voted_author in self.votes.values():
            if voted_author in vote_counts:
                vote_counts[voted_author] += 1
        
        # If no votes were cast but multiple contributions exist, it's a tie (0 vs 0)
        if not self.votes:
            return None

        # Find max votes
        max_votes = max(vote_counts.values())
        
        # Find all authors with max_votes
        winners = [user for user, count in vote_counts.items() if count == max_votes]
        
        if len(winners) == 1:
            return winners[0]
        else:
            return None  # Tie

    def finalize_round(self):
        """
        Finalizes the round, adds the winning component to the meme,
        and clears the round state.
        """
        winner = self.get_winner()
        
        if winner is None:
            return False
            
        winning_component = self.current_contributions[winner]
        self.meme_components.append(winning_component)
        
        # Clear round state
        self.current_contributions = {}
        self.votes = {}
        
        return True

    def is_meme_complete(self):
        """
        Checks if the meme has exactly 3 components.
        """
        return len(self.meme_components) == 3