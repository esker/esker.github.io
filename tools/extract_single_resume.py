from pathlib import Path
from PyPDF2 import PdfReader

base = Path(__file__).resolve().parents[1] / 'Resume'
file_in = base / 'Isaac_Gibbs_Resume.pdf'
file_out = base / 'Isaac_Gibbs_Resume.txt'

if not file_in.exists():
    print(f'Missing {file_in}')
    raise SystemExit(1)

reader = PdfReader(str(file_in))
texts = []
for p in reader.pages:
    t = p.extract_text() or ''
    texts.append(t)

out = '\n\n---PAGE BREAK---\n\n'.join(texts)
file_out.write_text(out, encoding='utf-8')
print(f'Wrote {file_out} (chars={len(out)})')

