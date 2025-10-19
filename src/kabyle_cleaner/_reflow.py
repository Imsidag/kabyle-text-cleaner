import re

def reflow_paragraphs(text: str) -> str:
    lines = text.splitlines()
    if not lines:
        return ""
    out = [lines[0]]
    for prev, curr in zip(lines, lines[1:]):
        if not curr.strip():
            out.append(curr)
            continue
        if re.search(r'[.!?…][»"”"]*$', prev):
            out.append(curr)
        else:
            out[-1] += " " + curr
    return "\n".join(re.sub(r" {2,}", " ", ln) for ln in out)
