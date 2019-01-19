A little docker demo for secconf

    $ docker built -t test
    $ docker run --rm -it --security-opt seccomp=${PWD}/profiles/seccomp\_centos\_default.json test
    $ docker run --rm -it --security-opt seccomp=${PWD}/profiles/seccomp\_centos\_no\_uname.json test

