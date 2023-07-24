"""
HXRSnD IPython Shell
"""
import logging
import os  # noqa
import socket
import warnings
from importlib import reload  # noqa
from pathlib import Path  # noqa

# Ignore python warnings (Remove when ophyd stops warning about 'signal_names')
warnings.filterwarnings('ignore')

logger = logging.getLogger(__name__)

try:
    from snd_devices import *  # noqa

    # Success
    logger.debug("Successfully created SplitAndDelay class on '{}'".format(
        socket.gethostname()))
except Exception as e:
    logger.error("Failed to create SplitAndDelay class on '{}'. Got error: "
                 "{}".format(socket.gethostname(), e))
    raise

# Try importing from the scripts file if we succeeded at making the snd object
else:
    try:
        from scripts import *  # noqa
        logger.debug("Successfully loaded scripts.")
    # There was some problem in the file
    except Exception as e:
        logger.warning("Failed to load scripts file, got the following error: "
                       "{}".format(e))
        raise
    # Notify the user that everything went smoothly
    else:
        logger.info("Successfully initialized new SnD session on '{}'".format(
            socket.gethostname()))
