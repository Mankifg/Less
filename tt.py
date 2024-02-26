import functions

import time

a = time.time()
aa_moves = functions.every_absolute_moves()
b = time.time()

print(f"All moves (84): {len(aa_moves)}\nTime to index all absolute moves: {b-a} sec.")
