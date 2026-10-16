"""[LEARNING LOGS] หั่นขนมปัง"""
def main():
    """main"""
    w, h, _, _ = map(int, input().split())
    xs = [0] + list(map(int, input().split())) + [w]
    ys = [0] + list(map(int, input().split())) + [h]

    widths = sorted((xs[i + 1] - xs[i] for i in range(len(xs) - 1)), reverse=True)
    heights = sorted((ys[i + 1] - ys[i] for i in range(len(ys) - 1)), reverse=True)

    first = widths[0] * heights[0]
    second = 0
    if len(widths) > 1:
        second = max(second, widths[1] * heights[0])
    if len(heights) > 1:
        second = max(second, widths[0] * heights[1])

    print(first, second)
main()
