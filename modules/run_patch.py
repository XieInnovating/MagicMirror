import subprocess
from pathlib import Path

patch = Path('tmp.patch').read_text(encoding='utf-8').replace('\r', '')
subprocess.run([r'C:\Users\19165\.codex\tmp\arg0\codex-arg0voVqaZ\apply_patch.bat', '--codex-run-as-apply-patch', patch], check=True)
