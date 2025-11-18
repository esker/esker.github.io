import sys
from pathlib import Path

try:
    from PyPDF2 import PdfReader
except Exception as e:
    print("PyPDF2 not installed. Please `pip install PyPDF2` and re-run.")
    raise

base = Path(__file__).resolve().parents[1] / 'Resume'
files = ['ig_resume.pdf', 'IG_Producer.pdf']

for fname in files:
    path = base / fname
    if not path.exists():
        print(f"Missing: {path}")
        continue
    reader = PdfReader(str(path))
    out_lines = []
    for i, page in enumerate(reader.pages):
        try:
            text = page.extract_text() or ''
        except Exception as e:
            text = ''
        out_lines.append(text)
    out = '\n\n---PAGE BREAK---\n\n'.join(out_lines)
    out_path = base / (fname.replace('.pdf', '.txt'))
    out_path.write_text(out, encoding='utf-8')
    print(f"Wrote: {out_path} (chars: {len(out)})")

print('Done')

