#!/usr/bin/env python3
# Copyright 2022 capricorn
# See LICENSE file for licensing details.
#
# Learn more at: https://juju.is/docs/sdk

"""Charm the service.

Refer to the following post for a quick-start guide that will help you
develop a new k8s charm using the Operator Framework:

    https://discourse.charmhub.io/t/4208
"""

import logging

from ops.charm import CharmBase
from ops.main import main
from ops.model import ActiveStatus

logger = logging.getLogger(__name__)


class GowikicharmCharm(CharmBase):
    """Charm the service."""


    def __init__(self, *args):
        super().__init__(*args)
        self.framework.observe(self.on.gowiki_pebble_ready, self._on_gowiki_pebble_ready)
       


    def _on_gowiki_pebble_ready(self, event):
        """Define and start a workload using the Pebble API.

        TEMPLATE-TODO: change this example to suit your needs.
        You'll need to specify the right entrypoint and environment
        configuration for your specific workload. Tip: you can see the
        standard entrypoint of an existing container using docker inspect

        Learn more about Pebble layers at https://github.com/canonical/pebble
        """
        # Get a reference the container attribute on the PebbleReadyEvent
        container = event.workload
        # Define an initial Pebble layer configuration
        pebble_layer = {
            "summary": "gowiki layer",
            "description": "pebble config layer for gowiki",
            "services": {
                "gowiki": {
                    "override": "replace",
                    "summary": "gowiki",
                    "command": "/gowiki",
                    "startup": "enabled",
                    # "environment": {"thing": self.model.config["thing"]},
                }
            },
        }
        # Add initial Pebble config layer using the Pebble API
        container.add_layer("gowiki", pebble_layer, combine=True)
        # Autostart any services that were defined with startup: enabled
        container.autostart()
        # Learn more about statuses in the SDK docs:
        # https://juju.is/docs/sdk/constructs#heading--statuses
        self.unit.status = ActiveStatus()



if __name__ == "__main__":
    main(GowikicharmCharm)
