# Copyright 2019
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
import charms_openstack.charm
import charms.reactive

import charms_openstack.bus
charms_openstack.bus.discover()

charms_openstack.charm.use_defaults(
    'charm.installed',
    'update-status',
    'upgrade-charm',
    'storage-backend.connected',
)


@charms.reactive.when('config.changed.driver-source')
def reinstall():
    with charms_openstack.charm.provide_charm_instance() as msa:
        msa.install()
