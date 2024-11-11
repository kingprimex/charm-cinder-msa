# Cinder MSA Subordinate Charm

This charm integrates MSA as a backend for Cinder for OpenStack.

## Building the Charm

### Step 1: Install the Charm Tool

To get started, install the `charm` tool using the following command:

```bash
sudo snap install --classic charm
```

### Step 2: Clone the Repository

Next, clone the repository to your local machine:

```bash
git clone git@github.com:kingprimex/charm-cinder-msa.git
```

### Step 3: Build the Charm

Navigate to the cloned directory and set the build directory environment variable:

```bash
cd charm-cinder-msa
export CHARM_BUILD_DIR=$HOME/deployment/build
charm build
```

The final version of the charm will be located in: $HOME/deployment/build/cinder-msa
