"""Fetch and download DAT files."""
import zipfile
from datetime import datetime

from datoso.configuration.folder_helper import Folders
from datoso.configuration.logger import logger
from datoso.helpers.download import DownloadProgress, downloader
from datoso.helpers.file_utils import move_path, remove_folder

from datoso_seed_lostlevel import __prefix__


def fix_xml_files(folder_helper: Folders) -> None:
    """Fix XML files."""
    # Remove "[http://www.logiqx.com/Dats/datafile.dtd]" from <!DOCTYPE datafile PUBLIC "-//Logiqx//DTD ROM Management Datafile//EN" "http://www.logiqx.com/Dats/datafile.dtd"[http://www.logiqx.com/Dats/datafile.dtd]>
    xml_files = folder_helper.dats.glob('**/*.xml')
    for xml_file in xml_files:
        with open(xml_file, 'r', encoding='utf-8') as file:
            content = file.read()
        content = content.replace('[http://www.logiqx.com/Dats/datafile.dtd]', '')
        with open(xml_file, 'w', encoding='utf-8') as file:
            file.write(content)

def download_dat_files(download_url: str, folder_helper: Folders) -> None:
    """Download DAT files."""
    system_tz = datetime.now().astimezone().tzinfo
    destination_file = f'lost-level-archive_{datetime.now(system_tz).strftime("%Y%m%d")}.zip'
    logger.info(f'Downloading DAT files from {download_url} to {folder_helper.download / destination_file}\n')
    with DownloadProgress() as progress:
        downloader(url=download_url, destination=folder_helper.download / destination_file, progress=progress)
    #unzip files to folder_helper.dats
    logger.info(f'Extracting DAT files to {folder_helper.dats / "tmp"}\n')
    with zipfile.ZipFile(folder_helper.download / destination_file, 'r') as zip_ref:
        zip_ref.extractall(folder_helper.dats / 'tmp')
    files = ['DATs', 'Legacy DATs', 'Extra', 'Header Files']
    for file in files:
        move_path(folder_helper.dats / 'tmp' / 'lost-level-archive-main' / file, folder_helper.dats / file)
    logger.info('Cleaning up temporary files\n')
    move_path(folder_helper.download / destination_file, folder_helper.backup)
    remove_folder(folder_helper.dats / 'tmp')
    fix_xml_files(folder_helper)


def fetch() -> None:
    """Fetch and download DAT files."""
    download_url = 'https://github.com/televandalist/lost-level-archive/archive/refs/heads/main.zip'
    folder_helper = Folders(seed=__prefix__)
    folder_helper.clean_dats()
    folder_helper.create_all()
    download_dat_files(download_url, folder_helper)
