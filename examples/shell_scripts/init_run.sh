#!/bin/bash

MPGADGET_REPO=$HOME/MP-Gadget


FG_RED=$'\033[0;31m'
FG_GREEN=$'\033[0;32m'
FG_YELLOW=$'\033[0;33m'
FG_RESET=$'\033[0m'

echo "MP-Gadget repo dir: ${FG_YELLOW}$MPGADGET_REPO${FG_RESET}"


# Detect current conda environment
# --------------------------------------------------------------
if [ -z "$CONDA_PREFIX" ]; then
    echo "Conda Environment: ${FG_RED}No conda environment detected.${FG_RESET}"
    exit 1
else
    echo "Conda Environment: ${FG_GREEN}$(basename $CONDA_PREFIX)${FG_RESET}"
fi


# Check if python is available in the current conda environment
# --------------------------------------------------------------
if command -v python >/dev/null 2>&1; then
    echo "Python Interpreter: ${FG_GREEN}$(python --version 2>&1)${FG_RESET}"
else
    echo "Python Interpreter: ${FG_RED}Not detected in the current conda environment.${FG_RESET}"
    exit 1
fi


# Check if classy is installed in the current conda environment
# --------------------------------------------------------------
# change to 'conda' or 'pip' depending on how classy was installed 
version=$(conda list '^classy$' | awk '!/^#/ {print $2}')
if [ -n "$version" ]; then
    echo "classy is installed : ${FG_GREEN}Yes (version $version)${FG_RESET}"
else
    echo "classy is installed : ${FG_RED}No${FG_RESET}"
    exit 1
fi


# Ask user if soft link required files from the MP-Gadget example directory
# --------------------------------------------------------------
read -p "Do you want to soft link the required cooling files from the MP-Gadget example directory? (y/n) :" answer
if [[ "$answer" == "y" ]]; then
    echo "Creating soft link - ${FG_YELLOW}$MPGADGET_REPO/examples/TREECOOL_fg_june11${FG_RESET}"
    ln -s $MPGADGET_REPO/examples/TREECOOL_fg_june11 . || { echo "${FG_RED}Error: Failed.${FG_RESET}"; exit 1; }
    echo "Creating soft link - ${FG_YELLOW}$MPGADGET_REPO/examples/cooling_metal_UVB.hdf5${FG_RESET}"
    ln -s $MPGADGET_REPO/examples/cooling_metal_UVB.hdf5 . || { echo "${FG_RED}Error: Failed.${FG_RESET}"; exit 1; }
    echo "Creating soft link - ${FG_YELLOW}$MPGADGET_REPO/examples/cooling_metal_UVB${FG_RESET}"
    ln -s $MPGADGET_REPO/examples/cooling_metal_UVB . || { echo "${FG_RED}Error: Failed.${FG_RESET}"; exit 1; }
else
    echo "Skipping soft linking required files from the MP-Gadget example directory."
fi


# Ask user if generate initial conditions with classy
# --------------------------------------------------------------
read -p "Do you want to generate initial power spectrum with classy? (y/n) :" answer
if [[ "$answer" == "y" ]]; then
    # Check if paramfile.genic exists
    if [ ! -f "./paramfile.genic" ]; then
        echo "${FG_RED}Error: paramfile.genic not found in the current directory.${FG_RESET}"
        exit 1
    else
        echo "Found paramfile.genic, proceeding to generate initial power spectrum with classy."
        python $MPGADGET_REPO/tools/make_class_power.py ./paramfile.genic || { echo "${FG_RED}Error: Failed to generate initial power spectrum with classy.${FG_RESET}"; exit 1; }
    fi
fi
