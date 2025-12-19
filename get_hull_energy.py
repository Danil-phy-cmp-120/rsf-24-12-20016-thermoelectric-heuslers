import numpy as np
import pandas as pd
from mp_api.client import MPRester
from pymatgen.analysis.phase_diagram import PhaseDiagram, PDEntry
from pymatgen.core import Composition
import warnings
warnings.filterwarnings('ignore')

api_key = "V1rF3wsXlckzzSMVDYzjyfyuTmvmVm5K"

def get_phase_diagram(elements: str) -> PhaseDiagram:
    with MPRester(api_key) as mpr:
        entries = mpr.get_entries_in_chemsys(elements, additional_criteria={"thermo_types": ["R2SCAN"]})
    return PhaseDiagram(entries)

e_above = []
df = pd.read_csv('energies_geom_gaps.csv')
for i, row in enumerate(df.itertuples(index=False)):
    comp = Composition(row[1].replace('_',''))
    elements_key = "-".join([element.symbol for element in comp.elements])

    diagram = get_phase_diagram(elements_key)
    target_entry = PDEntry(comp, row[2]*comp.num_atoms)
    e_above.append(diagram.get_e_above_hull(target_entry,
                                       allow_negative=True,
                                       on_error="ignore"))

e_above = np.array(e_above)
e_above_clamped = np.clip(e_above, 0.0, None)
print(e_above_clamped)
np.savetxt("e_above_hull.dat", e_above_clamped)