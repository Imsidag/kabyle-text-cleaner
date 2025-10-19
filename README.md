# kabyle text cleaner

Command-line utility and Python library to normalise Kabyle text
(non-standard Greek/Latin look-alikes → proper Latin-derived letters)
and optionally reflow paragraphs.

## Installation

```bash
pip install kabyle-text-cleaner
```

## CLI usage
```bash

# only check
kabtxtcleaner text.txt
```

# fix + reflow
```bash
kabtxtcleaner text.txt --fix -o clean.txt
```

```bash
kabtxtcleaner text.txt --fix --reflow -o clean.txt
```

## Library usage
```Python

from kabyle_cleaner import fix_text, reflow_paragraphs

clean = fix_text("γğţţ")
print(clean)            # ɣǧṭṭ
```

## License

MIT License
Copyright (c) 2025 Athmane MOKRAOUI
