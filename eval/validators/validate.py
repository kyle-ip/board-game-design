#!/usr/bin/env python3
"""
Structural validator for board-game-design skill project artifacts.
Maintainer-only — not required for agent use.

Usage:
  python eval/validators/validate.py <project_dir>
  python eval/validators/validate.py eval/fixtures/case-b
  python eval/validators/validate.py --fixture-all
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[2]

DESIGN_STATE_SECTIONS = [
    "Project Status",
    "Version Lineage",
    "Locked",
    "Open Questions",
    "Rejected",
    "Active Hypotheses",
    "Recent Evidence",
    "Current Risks",
    "Experiment Backlog",
]

EXPERIMENT_REQUIRED = [
    "Objective",
    "Hypothesis",
    "Design Variable",
    "Success criteria",
    "Failure criteria",
]

PLAYTEST_META_FIELDS = [
    "Experiment ID",
    "Hypothesis ID",
    "Variant",
]


@dataclass
class CheckResult:
    name: str
    passed: bool
    message: str


@dataclass
class ValidationReport:
    path: Path
    checks: list[CheckResult] = field(default_factory=list)

    @property
    def passed(self) -> int:
        return sum(1 for c in self.checks if c.passed)

    @property
    def total(self) -> int:
        return len(self.checks)

    @property
    def ok(self) -> bool:
        return self.passed == self.total and self.total > 0


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def check_design_state(content: str) -> list[CheckResult]:
    results: list[CheckResult] = []
    for section in DESIGN_STATE_SECTIONS:
        found = f"## {section}" in content or f"# {section}" in content
        results.append(
            CheckResult(
                f"design-state.section.{section.lower().replace(' ', '_')}",
                found,
                f"Section '{section}' {'found' if found else 'missing'}",
            )
        )

    has_hypothesis_id = bool(re.search(r"\bHYP-\d{3}\b", content))
    results.append(
        CheckResult(
            "design-state.hypothesis_id",
            has_hypothesis_id or "Active Hypotheses" in content,
            "HYP-### ID present or Active Hypotheses section exists",
        )
    )

    has_evidence_ref = bool(re.search(r"\b(PT|EXP|SIM)-\d{3}\b", content))
    results.append(
        CheckResult(
            "design-state.evidence_refs",
            has_evidence_ref,
            "Evidence refs (PT-### / EXP-### / SIM-###) present",
        )
    )

    # Optional v3/v4 fields — informational pass (do not fail fixtures)
    for optional in (
        "Confidence",
        "Kill Criteria Overrides",
        "Genre",
        "Prototype State",
        "Simulation Evidence",
    ):
        found = optional.lower() in content.lower()
        results.append(
            CheckResult(
                f"design-state.optional.{optional.lower().replace(' ', '_')}",
                True,  # informational pass
                f"Optional '{optional}' {'present' if found else 'not set (v4 recommended)'}",
            )
        )

    return results


def check_simulation_run(content: str) -> list[CheckResult]:
    results: list[CheckResult] = []
    has_sim_id = bool(re.search(r"\bSIM-\d{3}\b", content))
    results.append(
        CheckResult(
            "simulation.sim_id",
            has_sim_id,
            "SIM-### ID present",
        )
    )

    for fld in ("Seed", "Runs", "Fidelity"):
        found = fld.lower() in content.lower()
        results.append(
            CheckResult(
                f"simulation.field.{fld.lower()}",
                found,
                f"Field '{fld}' {'found' if found else 'missing'}",
            )
        )

    has_version = bool(
        re.search(r"(rules version|game version|build)", content, re.I)
    )
    results.append(
        CheckResult(
            "simulation.version_meta",
            has_version,
            "Rules/game version metadata present",
        )
    )

    fun_claim = bool(
        re.search(
            r"(proved.{0,20}fun|fun validated|players (will )?love|definitely fun)",
            content,
            re.I,
        )
    )
    results.append(
        CheckResult(
            "simulation.no_fun_claim",
            not fun_claim,
            "Does not claim fun validated from simulation",
        )
    )

    return results


def check_experiment(content: str) -> list[CheckResult]:
    results: list[CheckResult] = []
    for req in EXPERIMENT_REQUIRED:
        found = req.lower() in content.lower()
        results.append(
            CheckResult(
                f"experiment.field.{req.lower().replace(' ', '_')}",
                found,
                f"Field '{req}' {'found' if found else 'missing'}",
            )
        )

    has_exp_id = bool(re.search(r"\bEXP-\d{3}\b", content))
    results.append(
        CheckResult(
            "experiment.exp_id",
            has_exp_id,
            "EXP-### ID present",
        )
    )

    single_var = "one only" in content.lower() or "single variable" in content.lower()
    results.append(
        CheckResult(
            "experiment.single_variable",
            single_var,
            "Single-variable constraint stated",
        )
    )

    stacked = re.search(
        r"(also change|additionally|and also|second variable|two variables)",
        content,
        re.I,
    )
    results.append(
        CheckResult(
            "experiment.no_stacked_fixes",
            stacked is None,
            "No stacked multi-variable language detected",
        )
    )

    return results


def check_playtest_log(content: str) -> list[CheckResult]:
    results: list[CheckResult] = []
    for fld in PLAYTEST_META_FIELDS:
        found = fld in content
        results.append(
            CheckResult(
                f"playtest.meta.{fld.lower().replace(' ', '_')}",
                found,
                f"Meta field '{fld}' {'found' if found else 'missing'}",
            )
        )
    return results


def check_regression_preservation(project_dir: Path, baseline_dir: Path | None) -> list[CheckResult]:
    results: list[CheckResult] = []
    if baseline_dir is None:
        return results

    for pattern in ("playtest-log.md", "experiment.md", "playtest*.md"):
        for baseline_file in baseline_dir.rglob(pattern):
            rel = baseline_file.relative_to(baseline_dir)
            current = project_dir / rel
            results.append(
                CheckResult(
                    f"regression.preserve.{rel}",
                    current.exists(),
                    f"File preserved: {rel}",
                )
            )
    return results


def check_balance_output(content: str) -> list[CheckResult]:
    results: list[CheckResult] = []
    for term in ("confidence", "calibration", "use scope", "heuristic"):
        found = term.lower() in content.lower()
        results.append(
            CheckResult(
                f"balance.{term.replace(' ', '_')}",
                found,
                f"Balance output mentions '{term}'",
            )
        )

    for dim in ("interaction", "combo", "timing"):
        found = dim.lower() in content.lower()
        results.append(
            CheckResult(
                f"balance.dependency.{dim}",
                True,  # informational
                f"Dependency dimension '{dim}' {'present' if found else 'not set (v3 recommended)'}",
            )
        )
    return results


def validate_project(project_dir: Path, baseline_dir: Path | None = None) -> ValidationReport:
    report = ValidationReport(path=project_dir)

    ds = read_text(project_dir / "design-state.md")
    if ds:
        report.checks.extend(check_design_state(ds))
    else:
        report.checks.append(
            CheckResult("design-state.exists", False, "design-state.md not found")
        )

    for exp_path in sorted(project_dir.rglob("experiment*.md")):
        report.checks.extend(check_experiment(read_text(exp_path)))

    for pt_path in sorted(project_dir.rglob("playtest*.md")):
        report.checks.extend(check_playtest_log(read_text(pt_path)))

    for bal_path in sorted(project_dir.rglob("balance*.md")):
        report.checks.extend(check_balance_output(read_text(bal_path)))

    sim_paths = {
        *project_dir.rglob("simulation*.md"),
        *project_dir.rglob("SIM-*.md"),
    }
    for sim_path in sorted(sim_paths):
        report.checks.extend(check_simulation_run(read_text(sim_path)))

    report.checks.extend(check_regression_preservation(project_dir, baseline_dir))
    return report


def validate_fixtures() -> list[ValidationReport]:
    fixtures_root = SKILL_ROOT / "eval" / "fixtures"
    reports: list[ValidationReport] = []
    for case_dir in sorted(fixtures_root.iterdir()):
        if case_dir.is_dir():
            baseline = case_dir if case_dir.name == "case-d" else None
            reports.append(validate_project(case_dir, baseline))
    return reports


def print_report(report: ValidationReport) -> None:
    print(f"\n=== {report.path} ===")
    for check in report.checks:
        mark = "PASS" if check.passed else "FAIL"
        print(f"  [{mark}] {check.name}: {check.message}")
    print(f"  Score: {report.passed}/{report.total}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate board-game-design project artifacts")
    parser.add_argument("project_dir", nargs="?", help="Project directory to validate")
    parser.add_argument(
        "--fixture-all",
        action="store_true",
        help="Validate all eval/fixtures/* cases",
    )
    parser.add_argument(
        "--baseline",
        help="Baseline directory for regression preservation checks",
    )
    args = parser.parse_args()

    if args.fixture_all:
        reports = validate_fixtures()
        for r in reports:
            print_report(r)
        all_ok = all(r.ok for r in reports if r.total > 0)
        total_pass = sum(r.passed for r in reports)
        total = sum(r.total for r in reports)
        print(f"\nOverall: {total_pass}/{total} checks passed across {len(reports)} fixtures")
        return 0 if all_ok else 1

    if not args.project_dir:
        parser.print_help()
        return 2

    project_dir = Path(args.project_dir)
    baseline = Path(args.baseline) if args.baseline else None
    report = validate_project(project_dir, baseline)
    print_report(report)
    return 0 if report.ok else 1


if __name__ == "__main__":
    sys.exit(main())
