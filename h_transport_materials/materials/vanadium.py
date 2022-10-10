import h_transport_materials as htm
from h_transport_materials import Diffusivity, Solubility
import h_transport_materials.conversion as c

VANADIUM_MOLAR_VOLUME = 8.34e-6  # m3/mol  https://www.aqua-calc.com/calculate/mole-to-volume-and-weight/substance/vanadium

volk_diffusivity = Diffusivity(
    D_0=2.9e-8,
    E_D=c.kJ_per_mol_to_eV(4.2),
    isotope="H",
    source="volkl_5_1975",
    range=(173, 573),
)

veleckis_solubility = Solubility(
    units="m-3 Pa-1/2",
    isotope="H",
    range=(519, 827),
    S_0=1.38e-1 * htm.avogadro_nb,
    E_S=c.kJ_per_mol_to_eV(-29.0),
    source="veleckis_thermodynamic_1969",
)

# found in Assessment of Database for Interaction of Tritium with ITER Plasma Facing Materials
schober_diffusivity = Diffusivity(
    D_0=5.6e-8,
    E_D=c.kJ_per_mol_to_eV(9.1),
    range=(-150 + 273.15, 200 + 273.15),
    source="schober_h_1990",
    isotope="H",
)  # TODO get data from experimental points, see issue #64

reiter_solubility = Solubility(
    units="m-3 Pa-1/2",
    S_0=2.1e-6 * htm.avogadro_nb / VANADIUM_MOLAR_VOLUME,
    E_S=c.kJ_per_mol_to_eV(-32.2),
    source="reiter_compilation_1996",
    isotope="H",
)

properties = [volk_diffusivity, veleckis_solubility]

for prop in properties:
    prop.material = "vanadium"

htm.database += properties
