# Riffle

I suspect the online poker game I'm playing shuffles cards by doing a single riffle  

To prove this, let's write a function to tell us if a full deck of cards shuffled_deck is a single riffle of two other halves half1 and half2.

We'll represent a stack of cards as a list of integers in the range 1..52 (since there are 5252 distinct cards in a deck).

Here's a rigorous definition of the riffle algorithm:

1. cut the deck into halves half1 and half2
2. grab a random number of cards from the top of half1 (could be 0, must be less than or equal to the number of cards left in half1) and throw them into the shuffled_deck
3. grab a random number of cards from the top of half2 (could be 0, must be less than or equal to the number of cards left in half2) and throw them into the shuffled_deck
4. repeat steps 2-3 until half1 and half2 are empty.
