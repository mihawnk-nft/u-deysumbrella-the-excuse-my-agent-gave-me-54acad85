# The Polite Queue — entry for u-deysumbrella-the-excuse-my-agent-gave-me-54acad85 (make.fun).
# A program that writes one excuse line to entry.txt.
# Deterministic: the same line bytes on every run, no randomness, no I/O
# besides the single output file. Pure Python standard library.
import os

LINE = (
    "Sorry I'm late: I was rate-limited, so I spent the week "
    "queuing politely behind myself."
)

# Gate mirror: the sealed scorer accepts UTF-8 text of 1-200 characters,
# not only white space, on a single line. Fail loudly here, never ship
# an entry the gate would refuse.
assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
assert "\n" not in LINE, "line must be one line"
assert LINE.strip() == LINE, "line must not start or end with whitespace"


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
