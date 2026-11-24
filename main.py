import os

# The word: Borborygmus - the rumbling sound of the stomach
word = "Borborygmus"

# Write to the output directory
output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
output_path = os.path.join(output_dir, "word.txt")

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Write the word
with open(output_path, "w") as f:
    f.write(word)

print(f"Written: {word}")
