
def translate(n):
    len_n = len(n)
    if n == "0":
        return ["1"]
    elif len(n) % 2 == 0:
        mid = len_n//2
        lh = n[:mid].lstrip("0")
        rh = n[mid:].lstrip("0")
        lh = "0" if not lh else lh
        rh = "0" if not rh else rh
        return [lh, rh]
    else:
        val = int(n) * 2024
        return [format(val)]

def main():
    import tracemalloc
    tracemalloc.start()
    snapshots = []
    input = "0 27 5409930 828979 4471 3 68524 170"
    #input = "125 17"
    ns = input.split(" ")

    for blink in range(37):
        print(blink)
        snapshots.append(tracemalloc.take_snapshot())
        ns = [ item for n in ns for item in translate(n) ]
        snapshots.append(tracemalloc.take_snapshot())
    top_stats = snapshots[-1].compare_to(snapshots[-2], 'lineno')
    for stat in top_stats:
        print(stat)
    print(len(ns))

if __name__ == '__main__':
    main()
    