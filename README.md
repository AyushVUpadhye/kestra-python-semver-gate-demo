# Python Release SemVer Gate demo

A tiny Python package used to demonstrate the Kestra **Python Release SemVer Gate** blueprint (`python-release-semver-gate`). The blueprint compares the public API of a package at two commits, statically, and checks that the version bump follows Semantic Versioning.

The import name is `semver_demo` and the code lives in `src/semver_demo`. The public API is re-exported from a private module, `_greeting.py`.

## Commits

| Tag | Commit | Version | Change |
| --- | --- | --- | --- |
| `v1.0.0` | `cbe742eeb13641ad1bf66a5403b60a6e7d8e94b4` | 1.0.0 | `greet(name)` and `Greeter` |
| `v1.1.0` | `f3359619076dc692e700e1f0a504e8282e644012` | 1.1.0 | adds `farewell(name)` |
| `v2.0.0` | `a941ede3257832f02b8c692b603b9465203b0fa1` | 2.0.0 | `greet()` and `Greeter.greet()` now require a `language` argument |
| branch `breaking-as-minor` | `656f53ff6ceb99af2e3d9d570e64c03830febfbd` | 1.2.0 | the 2.0.0 change on top of 1.1.0, released as a minor version |

## Expected verdicts

Inputs: `repo_url: https://github.com/AyushVUpadhye/kestra-python-semver-gate-demo`, `package: semver_demo`, `project_path: .`. Versions are read from `pyproject.toml`.

| `base_commit` | `candidate_commit` | Verdict | Why |
| --- | --- | --- | --- |
| `v1.0.0` | `v1.1.0` | PASS | new API in a minor release (the blueprint's default inputs) |
| `v1.1.0` | `v2.0.0` | PASS | breaking change in a major release |
| `v1.1.0` | `breaking-as-minor` | BLOCK: `BREAKING_CHANGE_REQUIRES_MAJOR` | breaking change in a minor release |
| `v1.0.0` | `v2.0.0` | PASS | breaking change and new API in a major release |

Use the full commit SHAs from the table above; the blueprint does not accept tag or branch names. The `__version__` change in every release is reported as informational and never forces a bump.
