# pylint: skip-file
"""
Extension that intercepts mobile captive-portal checks and triggers HTTP redirects to our phishing page.
This runs purely on the HTTP server side; no 802.11 packets are crafted.
"""
import logging
from collections import defaultdict
import wifiphisher.common.extensions as extensions

logger = logging.getLogger(__name__)

class Captiveportalredirect(object):
    """
    Empty extension to activate captive portal redirect in the HTTP handler.
    """
    def __init__(self, data):
        """
        :param data: shared_data from WifiphisherEngine (includes args, gateway IP, etc.)
        :type data: namedtuple
        """
        self.data = data

    def get_packet(self, pkt):  # noqa: U100
        """
        No Wi-Fi packets are crafted by this extension.
        """
        return defaultdict(list)

    def send_output(self):  # noqa: U100
        """
        No console output; captive-portal redirect happens in HTTP server.
        """
        return []

    def send_channels(self):  # noqa: U100
        """
        No channel hopping needed.
        """
        return []

    def on_exit(self):  # noqa: U100
        """
        Nothing to clean up.
        """
        pass 