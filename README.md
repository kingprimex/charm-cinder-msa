# Cinder MSA subordinate charm

Acest charm integrează MSA ca backend in Cinder


## Building the charm

Instalăm comanda ```charm```:

```bash
sudo snap insttall --classic charm
```

Clonăm repo-ul:

```bash
git clone git@github.com:kingprimex/charm-cinder-msa.git
```

Dăm build:

```bash
cd charm-cinder-msa
export CHARM_BUILD_DIR=$HOME/deployment/build
charm build
```

Varianta finală a charmului va fi în: $HOME/deployment/build/cinder-msa
