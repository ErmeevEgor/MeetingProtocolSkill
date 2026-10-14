from pathlib import Path
import importlib.util
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'portable-skills' / 'meeting-protocol-storage' / 'scripts' / 'validate_storage.py'
spec = importlib.util.spec_from_file_location('validate_storage', SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)


class StorageFormatTests(unittest.TestCase):
    def test_template_valid(self):
        p = ROOT / 'portable-skills' / 'meeting-protocol-storage' / 'templates' / 'protocol-template.xml'
        module.validate_fragment(p.read_text(encoding='utf-8'))

    def test_example_valid(self):
        p = ROOT / 'portable-skills' / 'meeting-protocol-storage' / 'examples' / 'output' / 'Протокол_2026-10-05_Confluence_Storage_Format.xml'
        module.validate_fragment(p.read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
