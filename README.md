[![CI](https://github.com/michael-hoss/delta-crit/actions/workflows/pytest.yaml/badge.svg)](https://github.com/michael-hoss/delta-crit/actions/workflows/pytest.yaml)


# DeltaCrit

Quantify perception safety by the criticality delta between perceived and reference scene.

## State of project

Under development and not yet available on PyPI. Check out the repo locally to use it.

## Run the code on your own

Install the package editable locally to make absolute imports work
```bash
pip install -e .[dev]
pip install -e ./third_party/commonroad-crime
```

Test the editable installation
```bash
python -m pytest delta_crit
python -m pytest third_party/commonroad-crime  # one test will fail due to a missing icon
```

Compute the criticality delta between two CommonRoad scenes/scenarios.

```bash
# TODO: expose user-friendly interface
```

## Contribute to DeltaCrit

See [CONTRIBUTING.md](CONTRIBUTING.md).
