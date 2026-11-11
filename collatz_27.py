#!/usr/bin/env python3
"""Compute and print the Collatz sequence starting from 27."""


def collatz_sequence(start):
    """Return the Collatz sequence from start down to 1, inclusive."""
    if start < 1:
        raise ValueError("start must be a positive integer")
    sequence = [start]
    n = start
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence


def main():
    sequence = collatz_sequence(27)
    for value in sequence:
        print(value)
    total_steps = len(sequence) - 1
    print(f"Sequence length: {len(sequence)} values")
    print(f"Total steps: {total_steps}")


if __name__ == "__main__":
    main()
