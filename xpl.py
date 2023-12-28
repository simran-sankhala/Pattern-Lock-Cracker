import os
from argparse import ArgumentParser
from binascii import unhexlify
from hashlib import sha1
from itertools import permutations
from time import time

def print_info(message):
	print("\n\033[1;33m[i]\033[0m", message, "\n")

def print_alert(message):
	print("\n\n\033[1;32m[!]\033[0m", message, "\n")

def print_line(num):
	print("-" * 13)
	print(f"| {num[0]} | {num[1]} | { num[2] } |")

def print_gesture_path(positions):
	print("\n\n Found Pattern Sequence: ")

	for x in range(3):
		line = []
		for y in range(3):
			if str(x*3+y + 1) not in positions:
				line.append(" ")
			else:
				line.append(positions[str(x*3+y + 1)])

		print_line(line)

	print("-" * 13, "\n")


def crack_gesture(key):
	cells = list(range(9))
	start = time()

	for length in range(3,10):
		print(f"trying length {length} patterns...", end="")

		for possible_pattern in permutations(cells, r=length):
			pattern = "".join(str(c) for c in possible_pattern)

			hash = sha1(unhexlify("".join("0" + str(pos) for pos in pattern))).hexdigest()

			if hash == key:
				print_alert(f"GESTURE FOUND!!! \033[4m{pattern}\033[24m")

				pattern = ''.join(str(int(i)+1) for i in pattern)

				positions = {}

				for a, b in enumerate(pattern):
					positions[b] = a + 1

				print_gesture_path(positions)
				print_info(f"Time: {time() - start}s")

				exit(0)

		print("  nothing")

	print_info("Nothing found!")


def main():
	parser = ArgumentParser(description="Bruteforce lock pattern on Android phones & CTFs as well")

	parser.add_argument("gesture_file", help="The path to the gesture.key file", type=str, default="./gesture.key")

	args = parser.parse_args()


	with open(args.gesture_file, "rb") as fi:
                key = bytes(fi.read(sha1().digest_size)).hex()

                print_info(f"Looking for key {key}...")


	if len(key) / 2 != sha1().digest_size:
		print_info("Gesture.key file is invalid")
		exit(1)

	crack_gesture(key)



if __name__ == "__main__":
	main()
