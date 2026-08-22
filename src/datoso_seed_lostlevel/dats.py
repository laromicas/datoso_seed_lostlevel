"""DAT files for Lostlevel."""
import os

from datoso.configuration import config
from datoso.repositories.dat_file import XMLDatFile  # noqa: F401


class LostLevelDat(XMLDatFile):
    """Lost Level DAT file."""

    seed: str = 'lost_level'

    def initial_parse(self) -> list:
        """Parse the dat file."""
        name_array = self.full_name.split(' - ')
        self.company = name_array[0] if len(name_array) > 1 else None
        self.system = ' - '.join(name_array[1:]) if len(name_array) > 1 else name_array[0]
        find_system = self.overrides()
        self.extra_configs(find_system)

        self.suffixes = ['Lost Level']
        if self.suffix is not None and self.suffix not in self.suffixes:
            self.suffixes.append(self.suffix)

        self.suffix = os.path.join(*self.suffixes) # noqa: PTH118

        self.date = self.header.get('version', '').removeprefix('v').strip()
        if self.modifier or self.system_type:
            self.prefix = config.get('PREFIXES', self.modifier or self.system_type, fallback='')
        else:
            self.prefix = None

        return [self.prefix, self.company, self.system, self.suffix, self.get_date()]

    def get_date(self) -> str:
        """Get the date from the dat file."""
        return self.date

class LostLevelExtraDat(LostLevelDat):
    """Lost Level Extra DAT file."""

    seed: str = 'lost_level_extra'

    def initial_parse(self) -> list:
        """Parse the dat file."""
        name_array = self.full_name.split(' - ')
        self.company = name_array[0] if len(name_array) > 1 else None
        self.system = ' - '.join(name_array[1:]) if len(name_array) > 1 else name_array[0]
        if '(Extras)' in self.system:
            self.system = self.system.replace(' (Extras)', '')
        if ' - Extras' in self.system:
            self.system = self.system.replace(' - Extras', '')
        self.suffix = ''
        find_system = self.overrides()
        self.extra_configs(find_system)

        self.suffixes = ['Lost Level']
        if self.suffix is not None and self.suffix not in self.suffixes:
            self.suffixes.append(self.suffix)


        if 'Extras' not in self.suffixes:
            self.suffixes.append('Extras')

        # Remove empty suffixes
        self.suffixes = [suf for suf in self.suffixes if suf]


        self.suffix = os.path.join(*self.suffixes) # noqa: PTH118

        self.date = self.header.get('version', '').removeprefix('v').strip()
        if self.modifier or self.system_type:
            self.prefix = config.get('PREFIXES', self.modifier or self.system_type, fallback='')
        else:
            self.prefix = None

        return [self.prefix, self.company, self.system, self.suffix, self.get_date()]


    def get_date(self) -> str:
        """Get the date from the dat file."""
        return self.date
