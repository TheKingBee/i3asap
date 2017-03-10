# -*- coding: utf-8 -*-

import click
import os
import sys

from datetime import datetime

from helpers import slugify, fetchJSON
from models import AsynkDownloader, DebianLinux
import logging


@click.command()
@click.option('--ok',
              prompt='This program must only be run in live environments as it may '
                     'permanently screw up your system. Are you sure you want to continue?',
              default='yes')
@click.option('--bundle',
              prompt='What bundle do you want to use?',
              help='The bundle to configure your system after',
              default='default')
def main(bundle, ok):
    """
    Console script for i3asap
    """
    start_time = datetime.now()

    # check if it is reasonable to start at all
    if ok != 'yes':
        sys.exit()
    linux = DebianLinux()
    if not linux.verify_os():
        click.echo("Currently this program only supports Kali Linux. Exiting..")
        sys.exit()

    # Setup properties
    bundle = slugify(bundle)
    repository = "https://raw.githubusercontent.com/SteveTabernacle/i3asap/master/bundles/" + bundle + "/"

    # Init logging
    logging.basicConfig(filename='i3asap.log', level=logging.DEBUG)
    logging.debug("Started at "+str(start_time))

    manifest = fetchJSON(repository + "manifest.json")

    # Download all specified files, e.g. dotfiles and wallpaper

    logging.debug("Downloading " + str(manifest["wallpaper"]))
    wallpaper = AsynkDownloader([{"name": manifest["wallpaper"],
                                  "saveAs": "/usr/share/backgrounds/wallpaper.jpg"}],
                                repository + "/bundle/")
    wallpaper.start()

    logging.debug("Downloading " + str(manifest["dotfiles"]))
    dotfiles = AsynkDownloader(manifest["dotfiles"], repository + "/bundle/")
    dotfiles.start()

    click.echo("* Uninstalling " + manifest["uninstall"])
    # Purge specified programs
    if "purge" in manifest and len(manifest["uninstall"]) > 1:
        logging.debug(linux.uninstall(manifest["uninstall"]))

    click.echo("* Installing " + manifest["install"])
    # Install specified programs
    if "install" in manifest and len(manifest["install"]) > 1:
        logging.debug(linux.install(manifest["install"]))

    # Install i3
    click.echo("* Installing " + linux.i3_base_packages())
    logging.debug(linux.install(linux.i3_base_packages()))

    # todo Create new user
    # Wait until downloads are complete
    click.echo("* Waiting for dotfiles to finish downloading..")
    dotfiles.join()
    click.echo("* Dotfiles finished downloading!")

    click.echo("* Waiting for wallpaper to finish downloading..")
    wallpaper.join()
    click.echo("* Wallpaper finished downloading!")

    click.echo("* Done! Time elapsed: " + str(datetime.now() - start_time))

    try:
        input("Press Enter to switch to i3 ..")
    except SyntaxError:
        pass
    linux.switch_wm()

if __name__ == "__main__":
    main()
