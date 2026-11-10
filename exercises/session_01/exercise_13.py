"""Check the trigonometric identity with floating-point tolerance."""

from math import cos, isclose, pi, sin


def main() -> None:
    for label, x in [("pi", pi), ("pi/2", pi / 2), ("4*pi/3", 4 * pi / 3)]:
        result = sin(x)**2 + cos(x)**2
        print(f"x = {label}: {isclose(result, 1.0, rel_tol=1e-9, abs_tol=1e-9)}")


if __name__ == "__main__":
    main()
