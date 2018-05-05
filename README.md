# openAI Experiments

Experiments to try the openAI environments with the gym tool

## Getting Started

### Prerequisites

What things you need to install the software and how to install them
    
#### Ubuntu

```
$ sudo apt-get install golang python3-dev python-dev libcupti-dev libjpeg-turbo8-dev make tmux htop chromium-browser git cmake zlib1g-dev libjpeg-dev xvfb libav-tools xorg-dev python-opengl libboost-all-dev libsdl2-dev swig
```

```
$ wget https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh
$ bash Anaconda3-4.2.0-Linux-x86_64.sh
```
- Add anaconda to the PATH
- Install Docker

```
$ conda create --name universe python=3.5 anaconda
$ source activate universe
```
In (universe) env:

```
$ conda install pip six libgcc swig
$ conda install opencv
$ pip install --upgrade tensorflow
$ pip install --upgrade tensorflow-gpu
```
```
$ git clone https://github.com/openai/gym.git
$ cd gym
$ pip install -e '.[all]'
```
```
$ git clone https://github.com/openai/universe.git
$ cd universe
$ pip install -e .
```
