import os


def get_local_repo_root() -> str:
    """Get the root directory of the checked-out repository."""

    utils_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(utils_dir, "../.."))

    installed_hints = ["envs", "conda", "venv", "site-packages"]
    for installed_hint in installed_hints:
        if installed_hint in repo_root:
            raise OSError("Repository seems to be non-editable installed."
                          f"Hint: {installed_hint} is in installed path.")
    return repo_root


def get_local_crime_root() -> str:
    crime_root = os.path.join(get_local_repo_root(), "third_party/commonroad-crime")
    return crime_root


def get_package_root() -> str:
    delta_crit_root = os.path.join(get_local_repo_root(), "delta_crit")
    return delta_crit_root


def get_scenarios_dir() -> str:
    delta_crit_root: str = get_package_root()
    return os.path.join(delta_crit_root, "example_data/scenarios")


def get_crime_configs_dir() -> str:
    delta_crit_root: str = get_package_root()
    return os.path.join(delta_crit_root, "example_data/crime_configs")


def get_pem_configs_dir() -> str:
    delta_crit_root: str = get_package_root()
    return os.path.join(delta_crit_root, "example_data/pem_configs")