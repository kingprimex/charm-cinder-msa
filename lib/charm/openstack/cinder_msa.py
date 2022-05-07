import os
import shutil
import base64
import subprocess

import charms_openstack.charm

charms_openstack.charm.use_defaults('charm.default-select-release')


class CinderMSACharm(
        charms_openstack.charm.CinderStoragePluginCharm):

    name = 'cinder_msa'
    # There is no python-storops package. Just use python3-cinder.
    version_package = 'python3-cinder'
    release = 'xena'
    packages = ["multipath-tools", "sg3-utils", "sysfsutils", "python3-pip"]
    release_pkg = 'cinder-common'
    stateless = True
    # Specify any config that the user *must* set.
    mandatory_config = [
        'san-ip', 'san-login', 'san-password']

    def _ensure_unit_cfg_dir(self):
        basedir = "/etc/cinder"
        unit_cfg_dir = os.path.join(basedir, self.service_name)
        if os.path.isdir(unit_cfg_dir) is False:
            os.makedirs(unit_cfg_dir, 0o0711)
        shutil.chown(unit_cfg_dir, user="cinder", group="cinder")
        return unit_cfg_dir

    def install(self):
        super().install()
        subprocess.check_output(["sudo", "pip3", "install", "storops"])
        self.assess_status()

    def cinder_configuration(self):
        hpmsa_verify_certificate = self.config.get('hpmsa_verify_certificate', False)

        volumedriver = 'cinder.volume.drivers.san.hp.hpmsa_iscsi.HPMSAISCSIDriver'
        driver_options = [
            ('hpmsa_backend_name', self.config.get('hpmsa_backend_name')),
            ('hpmsa_pool_name', self.config.get('hpmsa_pool_name')),
            ('volume_driver', volumedriver),
            ('volume_backend_name', self.config.get('volume_backend_name')),
            ('san_ip', self.config.get('san-ip')),
            ('san_login', self.config.get('san-login')),
            ('san_password', self.config.get('san-password')),
            ('driver_use_ssl', self.config.get('driver_use_ssl')),
            ('hpmsa_verify_certificate', hpmsa_verify_certificate),
        ]
        
        hpmsa_iscsi_ips = self.config.get('hpmsa_iscsi_ips')
        if hpmsa_iscsi_ips:
            pool_names = [i for i in hpmsa_iscsi_ips.split(" ") if i]
            driver_options.append(
                ('hpmsa_iscsi_ips', ", ".join(pool_names))
            )

        return driver_options
