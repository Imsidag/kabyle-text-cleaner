from kabyle_cleaner import fix_text, disallowed_in_text, reflow_paragraphs

def test_fix():
    assert fix_text("γğţţ") == "ɣǧṭṭ"

def test_disallowed():
    assert "ξ" in disallowed_in_text("abcξḍ")

def test_reflow():
    txt = "One sentence\nstill same.\nNew para.\n\nAfter empty."
    out = reflow_paragraphs(txt)
    assert "still same." in out.splitlines()[0]
    assert "After empty." in out.splitlines()[-1]
