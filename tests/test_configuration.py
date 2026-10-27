import os
from pathlib import Path
import subprocess
import unittest
ROOT = Path(__file__).resolve().parents[1]

class DefaultDisabledTests(unittest.TestCase):
    def test_each_playbook_parses_and_refuses_unconfigured_operations(self):
        for playbook in (ROOT / 'playbooks').glob('*.yml'):
            with self.subTest(playbook=playbook.name):
                subprocess.run(['ansible-playbook', '--syntax-check', str(playbook)], check=True, capture_output=True)
                env = dict(os.environ)
                for key in ['AWX_URL', 'AWX_OAUTH_TOKEN', 'AWX_INVENTORY_ID', 'AWX_HOST_PREFIX']: env[key] = ''
                result = subprocess.run(['ansible-playbook', '-i', 'localhost,', '--connection', 'local', str(playbook)], env=env, capture_output=True, text=True, timeout=30)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('Require independently supplied AWX configuration', result.stdout)
                self.assertNotIn('TASK [Import explicitly selected hosts]', result.stdout)

if __name__ == '__main__': unittest.main()
