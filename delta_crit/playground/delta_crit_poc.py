from commonroad_crime.data_structure.configuration import CriMeConfiguration
from commonroad_crime.data_structure.crime_interface import CriMeInterface
from commonroad_crime.measure import TTC

from delta_crit.crime_utils.crime_utils import get_crime_config
from delta_crit.utils.file_utils import get_local_repo_root

# Note that `CriMeConfiguration.general: GeneralConfiguration` holds all the necessary paths
# for locating the (scenario) files.
config: CriMeConfiguration = get_crime_config("DEU_Gar-1_1_T-1")

crime_interface = CriMeInterface(config)
crime_interface.evaluate_scene(measures=[TTC], time_step=0, vehicle_id=200)
crime_interface.evaluate_scenario([TTC], time_start=0, time_end=20)
crime_interface.visualize(time_step=19)
crime_interface.save_to_file(output_dir=get_local_repo_root())

pass
