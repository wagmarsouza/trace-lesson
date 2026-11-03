from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "self-improvement"


class PackageTests(unittest.TestCase):
    def test_required_files_exist(self):
        required = [
            SKILL / "SKILL.md",
            SKILL / "references" / "memory-policy.md",
            SKILL / "templates" / "learning-entry.md",
            SKILL / "agents" / "openai.yaml",
            ROOT / "docs" / "opencode.md",
        ]
        for path in required:
            self.assertTrue(path.is_file(), path)

    def test_skill_identity_and_boundaries(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertRegex(text, r"(?m)^name: self-improvement$")
        for phrase in (
            "does not train the model",
            "does not guarantee a write",
            "Do not impose a fixed byte",
            "Permanent deletion requires clear authorization",
        ):
            self.assertIn(phrase, text)

    def test_public_files_have_no_known_private_markers(self):
        forbidden = [
            re.compile("HAL" + "9007", re.I),
            re.compile("wagmarsouza" + "@gmail", re.I),
            re.compile(r"\+?55\s*1[12]\s*\d{4,5}[- ]?\d{4}"),
            re.compile("google_" + r"token\.json", re.I),
            re.compile("API_" + r"Agents\.txt", re.I),
        ]
        for path in ROOT.rglob("*"):
            allowed = {".md", ".yaml", ".yml", ".json", ".py", ".txt"}
            if (
                not path.is_file()
                or ".git" in path.parts
                or "__pycache__" in path.parts
                or (path.suffix.lower() not in allowed and path.name != ".gitignore")
            ):
                continue
            text = path.read_text(encoding="utf-8")
            for pattern in forbidden:
                self.assertIsNone(pattern.search(text), f"{pattern.pattern} in {path}")

    def test_documented_relative_links_resolve(self):
        for rel in (
            "brand/trace-lesson-logo-v2.png",
            "docs/opencode.md",
            "skills/self-improvement/references/memory-policy.md",
            "skills/self-improvement/templates/learning-entry.md",
        ):
            self.assertTrue((ROOT / rel).exists(), rel)


if __name__ == "__main__":
    unittest.main()
