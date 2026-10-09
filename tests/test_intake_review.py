"""Synthetic-only tests: no Observatory/Dropbox personal archive material."""
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from intake_review import screen


class IntakeReviewTests(unittest.TestCase):
    def test_same_name_variant_is_review_not_auto_merge(self):
        result = screen([{"name": "The Magnetic-Field Mapper prototype"}],
                        [{"Candidate": "Magnetic Field Mapper"}])[0]
        self.assertTrue(result["review_required"])
        self.assertEqual(len(result["possible_matches"]), 1)
        self.assertIn("normalized-name match", result["possible_matches"][0]["reasons"])

    def test_distinct_names_same_doi(self):
        result = screen([{"name": "New paper name", "source": "https://doi.org/10.1234/ABC.12"}],
                        [{"name": "Prior paper name", "doi": "10.1234/abc.12"}])[0]
        self.assertEqual(result["possible_matches"][0]["reasons"], ["DOI match"])

    def test_source_url_match(self):
        result = screen([{"name": "A", "source": "https://github.com/org/project/"}],
                        [{"name": "B", "source": "https://github.com/org/project.git"}])[0]
        self.assertEqual(result["possible_matches"][0]["reasons"], ["source URL match"])

    def test_unmatched_is_not_novelty(self):
        result = screen([{"name": "Totally different"}], [{"name": "Existing object"}])[0]
        self.assertEqual(result["possible_matches"], [])
        self.assertIn("NOT a novelty finding", result["result"])
        self.assertIn("not checked", result["archive_coverage"].lower())

    def test_missing_name_holds(self):
        result = screen([{"source": "https://example.org/a"}], [])[0]
        self.assertEqual(result["error"], "missing candidate name")
        self.assertTrue(result["review_required"])


if __name__ == "__main__":
    unittest.main()
