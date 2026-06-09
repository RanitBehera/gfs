## Links
- Anaconda Home: https://www.anaconda.com/
- Miniconda Getting started: https://www.anaconda.com/docs/getting-started/miniconda/main
- Installing Miniconda: https://www.anaconda.com/docs/getting-started/miniconda/install/overview#windows-guides

  For Linux
  ```
  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
  ```
- VS Code: https://code.visualstudio.com/
- MP-Gadget Repository: https://github.com/MP-Gadget/MP-Gadget
  ```
  git clone https://github.com/MP-Gadget/MP-Gadget.git
  ```
- NINJA Repository: https://github.com/RanitBehera/ninja

  For MPI support, contact authors.
## Commands

> **IMPORTANT!!! - Double check the commands before you run them.**

- Windows Subsystem for Linux (WSL)
  
  To check available distro online
  ```
  wsl --list --online
  ```
  To install a distro
  ```
  wsl --install <distro_name>

  ```
  To shutdown wsl
  ```
  wsl --shutdown
  ```
  To remove a distro
  ```
  wsl --unregister <distro_name>
  ```
- MP-Gadget (only use the line you want)
  ```
  git clone https://github.com/MP-Gadget/MP-Gadget
  sudo apt update
  sudo apt install make
  sudo apt install build-essential
  sudo apt install openmpi-bin libopenmpi-dev
  sudo apt install libgsl-dev pkg-config
  make -j
  ```
- local directory creation (if needed)
  ```
  cd ~
  mkdir .local
  cd .local
  mkdir bin include lib
  cd bin
  ln -s ~/MP-Gadget/gadget/MP-Gadget ./
  ln -s ~/MP-Gadget/genic/MP-GenIC ./
  ```
  Add .local to PATH (if needed)
  ```
  export PATH="$HOME/.local/bin:$PATH"
  ```
  Source updated bashrc
  ```
  source ~/.bashrc
  ```
- Conda Commands (only use the line you want)
  ```
  conda env list
  conda create -n gfs python=3.11
  conda activate gfs
  which python
  python --version
  conda install -c conda-forge numpy scipy astropy matplotlib
  ```
  To deactivate a environment
  ```
  conda deactivate
  ```
  To remove an environemnt in conda
  ```
  conda env remove -n gfs
  ```

- bigfile
  ```
  pip install bigfile
  ```
  if `pip` not installed (in same env)
  ```
  conda install pip
  ```
- classy
  ```
  pip install 
  ```
  if `curl` not installed
  ```
  sudo apt install curl
  ```