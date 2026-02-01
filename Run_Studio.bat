@REM POLICY COMPLIANCE REVIEW (Vortex Internal Tooling)
@REM File: Run_Studio.bat
@REM Reviewed: 2026-02-01
@REM Reviewer: Codex
@REM
@REM Compliant:
@REM - [ ] Launches local-only tooling via launcher.py.
@REM - [ ] No embedded credentials or network calls.
@REM
@REM Non-compliant:
@REM - [ ] None noted.
@REM
@REM Needs review:
@REM - [ ] Ensure distribution aligns with approved software request controls.
@REM
@REM Notes / Actions:
@REM - Confirm this launcher is only used in approved internal environments.
@python "%~dp0launcher.py"
