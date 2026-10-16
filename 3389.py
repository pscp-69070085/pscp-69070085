"""Smart Trash Collector"""
def main():
    """main"""
    n = int(input())
    names = ["Plastic", "Can", "Glass"]
    for _ in range(n):
        vals = list(map(float, input().split()))
        total = sum(vals)
        parts = [f"{total:.1f}"]
        if total > 50:
            parts.append("Overloaded")
        for name, v in zip(names, vals):
            if v > 20:
                parts.append("Check Type " + name)
        print(", ".join(parts))
main()
