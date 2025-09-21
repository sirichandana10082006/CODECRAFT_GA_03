import random
import re
from collections import defaultdict

# --- CONFIGURATION ---
ORDER = 2        # How many words define the context (2 = bigram model)
MAX_LENGTH = 15  # Maximum words in a generated sentence

# --- STEP 1: THE CORPUS ---
corpus = """
The cat sat on the mat. The dog chased the cat. The cat meowed loudly at the dog.
A dog and a cat are not always friends. The mat is where the cat sits.
"""

# Tokenize: lowercase + split into words
words = re.findall(r'\b\w+\b', corpus.lower())
print("Tokens:", words[:20], "...")  # show first 20 tokens

# --- STEP 2: BUILD THE MARKOV MODEL ---
markov_model = defaultdict(list)

for i in range(len(words) - ORDER):
    current_state = tuple(words[i : i + ORDER])   # state = 2 words
    next_word = words[i + ORDER]                  # word that follows
    markov_model[current_state].append(next_word)

# --- STEP 3: GENERATE THE TEXT ---
def generate_text(model, max_length=MAX_LENGTH):
    # Pick a random starting pair (state)
    start_words = random.choice(list(model.keys()))
    text = list(start_words)

    # Generate words
    for _ in range(max_length - ORDER):
        current_state = tuple(text[-ORDER:])   # last 2 words
        if current_state in model:
            next_word = random.choice(model[current_state])
            text.append(next_word)
        else:
            break

    return ' '.join(text).capitalize()

# --- RUN THE GENERATOR ---
print("\n--- Text Generation with Markov Chains ---")
print(f"Trained on {len(words)} words with Order {ORDER}.\n")

for i in range(3):
    print(f"Generated Sentence {i+1}: {generate_text(markov_model)}...")
